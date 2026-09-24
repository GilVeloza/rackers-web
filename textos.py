"""El texto de la web, idioma por idioma.

No sale del catálogo de la app: esto es márketing, no interfaz. Cada idioma
tiene su archivo en `textos/`, con el código que usa la tienda por nombre
(`es-ES.py`, `ja.py`…), y dentro un único `TEXTO`. Los que no estén escritos
todavía no se publican: la web solo saca las páginas que tienen texto.

Las variantes por país no se escriben dos veces. El inglés británico sale del
americano, el mexicano del español y el portugués de Portugal del de Brasil,
con las mismas reglas que usa la app (`tools/loc.py`): así la web dice
«canchas» donde la app dice «canchas». Lo que una regla no puede saber —los
precios de cada tienda, sobre todo— se escribe en `PARCHES`.

Las capturas vienen hechas y en su idioma, de `design/app-store/idiomas/`.

En `legal/` va el texto de Privacidad, Condiciones y Soporte, con un archivo
por idioma igual que en `textos/`. Son las páginas que App Store Connect pide
por URL: la de privacidad es obligatoria y la de soporte también.
"""

from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

AQUI = Path(__file__).parent
sys.path.insert(0, str(AQUI.parent / "tools"))

# Qué captura de la app usa cada bloque de funciones.
CAPTURAS = {
    "inicio": "1-inicio",
    "evolucion": "2-estadisticas",
    "salud": "3-salud",
    "partidos": "4-partidos",
    "entrenador": "5-entrenador",
    "torneos": "6-torneo",
}

# Y la de cada uno de los tres pasos, en orden: apuntar, medir y mejorar. Para
# apuntar va el marcador del reloj, que es el único marcador de las capturas.
# Las funciones que salen aquí ya no repiten su captura más abajo.
PASOS = ["reloj", "partidos", "entrenador"]

# De qué idioma sale cada variante.
VARIANTES = {
    "en-GB": "en-US",
    "en-CA": "en-US",
    "en-AU": "en-US",
    "es-MX": "es-ES",
    "pt-PT": "pt-BR",
    "fr-CA": "fr-FR",
}

# Lo que las reglas no pueden saber: cómo se llama cada variante y lo que
# cuesta Pro en cada tienda. `_precios` cambia las cifras estén donde estén,
# también dentro de las preguntas.
#
# Las cifras de fuera de la eurozona son las del escalón de precio que toca en
# cada tienda; cuando estén fijadas en App Store Connect, se cambian aquí.
PARCHES = {
    "en-GB": {
        "idioma": "English (UK)",
        "_precios": [("$4.99", "£4.99"), ("$7.99", "£7.99"), ("$29.99", "£29.99"), ("$79.99", "£79.99"),
                     ("$49.99", "£49.99"), ("$0", "£0")],
    },
    "en-CA": {
        "idioma": "English (Canada)",
        "_precios": [("$4.99", "CA$6.99"), ("$7.99", "CA$10.99"), ("$29.99", "CA$39.99"), ("$79.99", "CA$109.99"),
                     ("$49.99", "CA$69.99"), ("$0", "CA$0")],
    },
    "en-AU": {
        "idioma": "English (Australia)",
        "_precios": [("$4.99", "A$7.99"), ("$7.99", "A$11.99"), ("$29.99", "A$44.99"), ("$79.99", "A$119.99"),
                     ("$49.99", "A$74.99"), ("$0", "A$0")],
    },
    "es-MX": {
        "idioma": "Español (México)",
        "_precios": [("4,99 €", "99 MXN"), ("7,99 €", "159 MXN"), ("29,99 €", "599 MXN"), ("79,99 €", "1.599 MXN"),
                     ("49,99 €", "999 MXN"), ("0 €", "0 MXN")],
    },
    "pt-PT": {
        "idioma": "Português (Portugal)",
        "_precios": [("R$ 24,90", "4,99 €"), ("R$ 39,90", "7,99 €"), ("R$ 149,90", "29,99 €"), ("R$ 399,90", "79,99 €"),
                     ("R$ 249,90", "49,99 €"), ("R$ 0", "0 €")],
    },
    "fr-CA": {
        "idioma": "Français (Canada)",
        "_precios": [("4,99 €", "6,99 $"), ("7,99 €", "10,99 $"), ("29,99 €", "39,99 $"), ("79,99 €", "99,99 $"),
                     ("49,99 €", "69,99 $"), ("0 €", "0 $")],
    },
}


def _modulo(archivo: Path, nombre: str):
    spec = importlib.util.spec_from_file_location(nombre, archivo)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def _cargar(codigo: str) -> dict | None:
    """El texto de un idioma: el de la portada y, si está, el de las páginas
    legales. Van en carpetas distintas porque no son lo mismo —una es
    márketing y la otra hay que leerla con lupa— pero viajan juntas, y así las
    variantes por país las heredan con las mismas reglas."""
    archivo = AQUI / "textos" / f"{codigo}.py"
    if not archivo.exists():
        return None
    limpio = codigo.replace("-", "_")
    texto = dict(_modulo(archivo, f"texto_{limpio}").TEXTO)
    legal = AQUI / "legal" / f"{codigo}.py"
    if legal.exists():
        texto.update(_modulo(legal, f"legal_{limpio}").TEXTO)
    return texto


def _regionalizar(valor, reglas):
    """Pasa las reglas del país por cualquier cosa: texto, lista o tupla."""
    from loc import regionalizar
    if isinstance(valor, str):
        return regionalizar(valor, reglas)
    if isinstance(valor, list):
        return [_regionalizar(v, reglas) for v in valor]
    if isinstance(valor, tuple):
        return tuple(_regionalizar(v, reglas) for v in valor)
    return valor


def _cambiar_precios(valor, precios):
    """Cambia las cifras de una tienda por las de otra, todas de una pasada.

    De una en una no vale: en Australia «$4.99» pasa a «A$7.99», y la regla
    siguiente, la de «$7.99», volvía a picar dentro de lo ya cambiado y salía
    «AA$11.99». Con una sola pasada, lo sustituido ya no se vuelve a tocar.
    Las más largas van primero, para que «$79.99» gane a «$7.99»."""
    if isinstance(valor, str):
        if not precios:
            return valor
        mapa = dict(precios)
        patron = re.compile("|".join(re.escape(k) for k in sorted(mapa, key=len, reverse=True)))
        return patron.sub(lambda m: mapa[m.group(0)], valor)
    if isinstance(valor, list):
        return [_cambiar_precios(v, precios) for v in valor]
    if isinstance(valor, tuple):
        return tuple(_cambiar_precios(v, precios) for v in valor)
    return valor


def _variante(codigo: str, base: dict) -> dict:
    from loc import REGLAS
    texto = {clave: _regionalizar(valor, REGLAS[codigo]) for clave, valor in base.items()}
    parches = dict(PARCHES.get(codigo, {}))
    precios = parches.pop("_precios", [])
    if precios:
        texto = {clave: _cambiar_precios(valor, precios) for clave, valor in texto.items()}
    texto.update(parches)
    return texto


def _todos() -> dict[str, dict]:
    textos = {}
    for archivo in sorted((AQUI / "textos").glob("*.py")):
        cargado = _cargar(archivo.stem)
        if cargado:
            textos[archivo.stem] = cargado
    for codigo, origen in VARIANTES.items():
        if codigo not in textos and origen in textos:
            textos[codigo] = _variante(codigo, textos[origen])
    return textos


TEXTOS = _todos()
