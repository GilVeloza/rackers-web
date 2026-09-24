"""La web de Rackers, en todos los idiomas de la app.

Saca una página por idioma en `publico/<idioma>/`, con las capturas de la app
en ese mismo idioma (las de `design/app-store/idiomas/`, que ya están hechas) y
los textos de `textos.py`.

    python3 web/build.py             # todos los idiomas que tengan texto
    python3 web/build.py es-ES en-US # solo esos
    python3 web/build.py --servir    # los genera y los sirve en localhost:8000

Solo usa la librería estándar. Las imágenes se reducen con `sips`, que viene
con macOS: las capturas de la tienda son de 1320 px de ancho y en la web con
520 sobra.
"""

import hashlib
import http.server
import os
import re
import shutil
import socketserver
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from textos import CAPTURAS, PASOS, TEXTOS  # noqa: E402

AQUI = Path(__file__).parent
RAIZ = AQUI.parent
SALIDA = AQUI / "publico"
ESTATICO = SALIDA / "static"
FICHA = RAIZ / "design/app-store/idiomas"
LOGO = RAIZ / "design/logo/final"
MARCOS = RAIZ / "design/marcos"
# Las raquetas de las tarjetas de deportes, una por vídeo. Las saca con
# Blender design/video/deportes/build.py.
DEPORTES_ORIGEN = RAIZ / "design/video/deportes"

# De derecha a izquierda.
RTL = {"ar", "he", "ur"}

# Los archivos de las seis raquetas, en el orden en que se enseñan los
# deportes. El nombre traducido sale de `deportes` en cada idioma.
RAQUETAS = ["padel", "tenis", "pickleball", "squash", "tenis-de-mesa", "badminton"]

# Las páginas que App Store Connect pide por URL. El trozo de URL va en
# español, como el resto del proyecto (`publico/`, `textos/`), y el título de
# cada una sale traducido de `footer_legal`.
PAGINAS = ["privacidad", "condiciones", "soporte"]

# A dónde escribe quien necesita ayuda. Va aquí y en un solo sitio: es lo que
# se pone también en App Store Connect como correo de soporte.
#
# RESPONSABLE es quién trata los datos, que el RGPD pide identificar con
# nombre y forma de contacto. Rackers va a nombre de Gil Veloza como autónomo.
CORREO = "hello@rackers.app"
RESPONSABLE = "Gil Veloza"

ANCHO_CAPTURA = 520
# La pantalla del reloj se ve a 172 px: 360 es holgado para pantalla retina.
ANCHO_RELOJ = 360

# Los marcos de Apple, al doble de lo que se ven, para pantalla retina.
ANCHO_MARCO_MOVIL = 760
ANCHO_MARCO_RELOJ = 620

# El cuadrado de cada deporte se ve a unos 365 px en la rejilla de tres: el
# vídeo es de 720, el doble, para pantalla retina. Aquí solo se le anuncia al
# navegador; el tamaño de verdad lo decide LADO en design/video/deportes/build.py.
ANCHO_DEPORTE = 720

# Dónde cae la pantalla dentro de cada marco, medido sobre el PNG de Apple:
# el iPhone 17 Pro Max tiene el hueco de 1320 × 2868 en (75, 66) de 1470 × 3000,
# y el Apple Watch Series 11 de 46 mm el de 416 × 496 en (72, 192) de 560 × 880.
HUECO_MOVIL = (75 / 1470, 66 / 3000, 1320 / 1470, 2868 / 3000)
HUECO_RELOJ = (72 / 560, 192 / 880, 416 / 560, 496 / 880)


# ---------------------------------------------------------------- imágenes

def reducir(origen: Path, destino: Path, ancho: int) -> None:
    """Una copia más pequeña, si no está ya hecha y al día.

    Las capturas van en JPEG: son 51 idiomas por seis pantallas, y en PNG la
    web pesaría setenta megas. El logo sigue en PNG, que necesita el fondo
    transparente."""
    if destino.exists() and destino.stat().st_mtime >= origen.stat().st_mtime:
        return
    destino.parent.mkdir(parents=True, exist_ok=True)
    formato = (["--setProperty", "format", "jpeg", "--setProperty", "formatOptions", "78"]
               if destino.suffix == ".jpg" else [])
    subprocess.run(["sips", "--resampleWidth", str(ancho)] + formato + [str(origen), "--out", str(destino)],
                   check=True, capture_output=True)


def preparar_deportes() -> None:
    """Las seis raquetas, cada una en su vídeo y con su cartel.

    Los vídeos no se recodifican a propósito: design/video/deportes/build.py
    ya los saca como los quiere un navegador —H.264, sin pista de sonido y con
    la cabecera al principio—, así que cualquier pasada por ffmpeg solo les
    quitaría calidad. El cartel es lo que se ve mientras cargan, y lo único que
    ve quien pide menos movimiento."""
    for nombre in RAQUETAS:
        origen = DEPORTES_ORIGEN / f"{nombre}.mp4"
        destino = ESTATICO / f"deportes/{nombre}.mp4"
        cartel = ESTATICO / f"deportes/{nombre}.jpg"
        if not origen.exists():
            sys.exit(f"Falta el vídeo: {origen}. Se saca con python3 design/video/deportes/build.py")
        if (destino.exists() and cartel.exists()
                and destino.stat().st_mtime >= origen.stat().st_mtime):
            continue
        destino.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(origen, destino)
        primer_fotograma(origen, cartel)


def primer_fotograma(video: Path, cartel: Path) -> None:
    """El primer fotograma, para que el hueco no salga negro mientras carga."""
    if not shutil.which("ffmpeg"):
        sys.exit("Hace falta ffmpeg para sacar el cartel de los vídeos: brew install ffmpeg")
    subprocess.run([
        "ffmpeg", "-v", "error", "-y", "-i", str(video),
        "-frames:v", "1", "-q:v", "4", str(cartel)], check=True)


def preparar_imagenes(idiomas: list[str]) -> None:
    reducir(LOGO / "rackers-icono-sin-fondo.png", ESTATICO / "rackers.png", 180)
    reducir(LOGO / "rackers-logotipo.png", ESTATICO / "rackers-logotipo.png", 520)
    # Los marcos oficiales de Apple (Apple Design Resources). Van encima de la
    # captura como una capa, no pegados a ella: así un solo PNG sirve para los
    # 51 idiomas y las seis pantallas, en vez de 306 imágenes compuestas.
    reducir(MARCOS / "iphone.png", ESTATICO / "marco-iphone.png", ANCHO_MARCO_MOVIL)
    reducir(MARCOS / "reloj.png", ESTATICO / "marco-reloj.png", ANCHO_MARCO_RELOJ)
    for idioma in idiomas:
        for captura in CAPTURAS.values():
            origen = FICHA / idioma / "app" / f"{captura}.png"
            if origen.exists():
                reducir(origen, ESTATICO / f"capturas/{idioma}/{captura}.jpg", ANCHO_CAPTURA)
        reloj = FICHA / idioma / "reloj" / "marcador.png"
        if reloj.exists():
            reducir(reloj, ESTATICO / f"capturas/{idioma}/reloj.jpg", ANCHO_RELOJ)


def capturas_de(idioma: str) -> Path:
    """Las de ese idioma, o las españolas si todavía no están sacadas."""
    return FICHA / idioma / "app"


# ---------------------------------------------------------------- piezas

def movil(idioma: str, captura: str, clase: str = "") -> str:
    """Una captura dentro del marco de iPhone de Apple.

    El marco es un PNG con el hueco de la pantalla transparente, así que la
    captura va debajo y el marco encima. La captura se redondea por las
    esquinas: el hueco de Apple es un *squircle* y una captura cuadrada
    asomaría en pico por las cuatro puntas."""
    izq, arr, anc, alt = (round(v * 100, 3) for v in HUECO_MOVIL)
    return f'''<div class="movil {clase}">
      <div class="marco">
        <img class="pantalla-app" src="../static/capturas/{idioma}/{CAPTURAS[captura]}.jpg"
             style="left:{izq}%;top:{arr}%;width:{anc}%;height:{alt}%"
             loading="lazy" alt="">
        <img class="bisel" src="../static/marco-iphone.png"
             width="{ANCHO_MARCO_MOVIL}" height="{round(ANCHO_MARCO_MOVIL * 3000 / 1470)}"
             loading="lazy" alt="">
      </div>
    </div>'''


def reloj(idioma: str) -> str:
    """El marcador del reloj dentro del marco de Apple Watch, con el mismo
    truco que el móvil: la captura debajo y el marco encima."""
    izq, arr, anc, alt = (round(v * 100, 3) for v in HUECO_RELOJ)
    return f'''<div class="marco-reloj">
        <img class="pantalla-app" src="../static/capturas/{idioma}/reloj.jpg"
             style="left:{izq}%;top:{arr}%;width:{anc}%;height:{alt}%"
             loading="lazy" alt="">
        <img class="bisel" src="../static/marco-reloj.png"
             width="{ANCHO_MARCO_RELOJ}" height="{round(ANCHO_MARCO_RELOJ * 880 / 560)}"
             loading="lazy" alt="">
      </div>'''


def pieza(idioma: str, captura: str) -> str:
    """La captura de un paso: el marcador del reloj o una del móvil."""
    return reloj(idioma) if captura == "reloj" else movil(idioma, captura)


def marca(raiz: str = "") -> str:
    """El logotipo entero —la raqueta y RACKERS en Unbounded—, no el icono con
    el nombre escrito al lado: así la barra lleva la tipografía de la marca y
    no la del sistema. El PNG es 520 × 88, o sea 2,6× de lo que se ve.

    `raiz` es a dónde vuelve el logo y desde dónde cuelga `static/`: en la
    portada basta con subir al ancla, y en las legales hay que salir de su
    carpeta."""
    destino = "#arriba" if raiz == "" else raiz
    return (f'<a class="marca" href="{destino}">'
            f'<img src="{raiz}../static/rackers-logotipo.png" width="201" height="34" alt="Rackers">'
            '</a>')


def enlaces_legales(t: dict, raiz: str) -> str:
    """Privacidad · Condiciones · Soporte, enlazadas. `raiz` es lo que hay que
    subir para llegar a la carpeta del idioma: nada desde la portada, un nivel
    desde una legal."""
    # Solo se enlaza lo que existe: un idioma sin texto legal todavía no debe
    # mandar a nadie a un 404.
    return " · ".join(f'<a href="{raiz}{slug}/">{nombre}</a>'
                      for slug, nombre in zip(PAGINAS, t["footer_legal"])
                      if f"{slug}_titulo" in t)


def documento(idioma: str, t: dict, slug: str) -> str:
    """Una página de texto: Privacidad, Condiciones o Soporte. Cuelga de
    `publico/<idioma>/<slug>/`, así que todo lo de `static/` sube dos niveles.

    Son las que pide App Store Connect: la de privacidad es obligatoria para
    publicar y la de soporte va en la ficha, donde la ve cualquiera."""
    raiz = "../"
    titulo = t[f"{slug}_titulo"]
    dir_ = "rtl" if idioma in RTL else "ltr"
    def relleno(texto: str) -> str:
        """`{responsable}` y `{correo}` los pone la plantilla: así el nombre y
        la dirección viven en un solo sitio y no hay que repetirlos en los 33
        idiomas ni cambiarlos 33 veces."""
        return texto.replace("{responsable}", RESPONSABLE).replace("{correo}", CORREO)

    secciones = "".join(
        f'<section class="apartado reveal"><h2>{nombre}</h2>'
        + "".join(f"<p>{relleno(parrafo)}</p>" for parrafo in parrafos)
        + "</section>"
        for nombre, parrafos in t[f"{slug}_secciones"])
    # El soporte enseña el correo en grande: es a lo que viene la gente.
    correo = ""
    if slug == "soporte":
        correo = (f'<section class="apartado correo reveal"><h2>{t["soporte_correo_titulo"]}</h2>'
                  f'<p><a class="correo-enlace" href="mailto:{CORREO}">{CORREO}</a></p>'
                  f'<p>{t["soporte_correo_nota"]}</p></section>')
    return f'''<!doctype html>
<html lang="{idioma}" dir="{dir_}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} · Rackers</title>
<meta name="description" content="{t[f"{slug}_entrada"]}">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#0B1322">
<link rel="icon" href="{raiz}../static/rackers.png">
<link rel="stylesheet" href="{raiz}../static/rackers.css?v={VERSION_CSS}">
</head>
<body id="arriba">
<div class="ambiente" aria-hidden="true"><span class="luz lima"></span><span class="luz rosa"></span></div>

<header class="cabecera">
  <nav>
    {marca(raiz)}
    <div class="acciones"><a class="volver" href="{raiz}">{t["legal_volver"]}</a></div>
  </nav>
</header>

<main class="documento">
  <h1 class="reveal">{titulo}</h1>
  <p class="entrada reveal">{t[f"{slug}_entrada"]}</p>
  <p class="nota reveal">{t["legal_actualizado"]}</p>
  {correo}
  {secciones}
</main>

<footer>
  <div class="pie">
    {marca(raiz)}
    <p class="nota">{t["footer_nota"]}</p>
    <div class="pie-legal">{enlaces_legales(t, raiz)}</div>
  </div>
  <p class="copyright">© Rackers</p>
</footer>

<script src="{raiz}../static/rackers.js?v={VERSION_JS}" defer></script>
</body>
</html>
'''


def selector(idioma: str) -> str:
    opciones = "".join(
        f'<option value="{codigo}"{" selected" if codigo == idioma else ""}>{datos["idioma"]}</option>'
        for codigo, datos in sorted(TEXTOS.items(), key=lambda p: p[1]["idioma"]))
    return f'<select class="idiomas" aria-label="Idioma" onchange="location.href=\'../\'+this.value+\'/\'">{opciones}</select>'


def boton(texto: str, clase: str = "principal") -> str:
    """El cartel del App Store. Mientras la app no esté publicada no es un
    enlace: mandar a una ficha que no existe es peor que no mandar a nada."""
    return (f'<span class="boton {clase} pronto">'
            f'<svg viewBox="0 0 16 20" width="16" height="20" aria-hidden="true">'
            f'<path d="M11.2 10.6c0-2 1.6-3 1.7-3-0.9-1.4-2.4-1.5-2.9-1.6-1.2-0.1-2.4 0.7-3 0.7s-1.6-0.7-2.6-0.7'
            f'c-1.3 0-2.6 0.8-3.3 2-1.4 2.4-0.4 6 1 8 0.7 1 1.5 2.1 2.5 2 1 0 1.4-0.6 2.6-0.6s1.5 0.6 2.6 0.6'
            f'c1.1 0 1.8-1 2.4-2 0.8-1.1 1.1-2.2 1.1-2.3 0 0-2.1-0.8-2.1-3.1zM9.3 4.2c0.5-0.7 0.9-1.6 0.8-2.6'
            f'-0.8 0-1.8 0.5-2.4 1.2-0.5 0.6-0.9 1.6-0.8 2.5 0.9 0.1 1.8-0.4 2.4-1.1z" fill="currentColor"/></svg>'
            f'{texto}</span>')


def seccion_funcion(idioma: str, indice: int, funcion: tuple) -> str:
    captura, titulo, texto, puntos = funcion
    lado = "izquierda" if indice % 2 == 0 else "derecha"
    lista = "".join(f"<li>{p}</li>" for p in puntos)
    return f'''<article class="funcion {lado} reveal">
      <div class="funcion-texto">
        <h3>{titulo}</h3>
        <p>{texto}</p>
        <ul class="marcas">{lista}</ul>
      </div>
      {movil(idioma, captura, "flota")}
    </article>'''


def tarjeta_funcion(funcion: tuple) -> str:
    """Una función sin móvil, porque su captura ya sale en los pasos."""
    _, titulo, texto, puntos = funcion
    lista = "".join(f"<li>{p}</li>" for p in puntos)
    return f'''<article class="funcion-suelta reveal">
        <h3>{titulo}</h3>
        <p>{texto}</p>
        <ul class="marcas">{lista}</ul>
      </article>'''


def bloque_funciones(idioma: str, funciones: list) -> str:
    """Las funciones en su orden. Las que tienen captura propia van con su
    móvil, a un lado y al otro por turnos; las que ya la enseñan en los pasos
    se juntan en tarjetas de texto, de dos en dos, en su sitio de la lista."""
    bloques, sueltas, lado = [], [], 0
    for funcion in funciones:
        if funcion[0] in PASOS:
            sueltas.append(tarjeta_funcion(funcion))
            continue
        if sueltas:
            bloques.append(f'<div class="funciones-sueltas">{"".join(sueltas)}</div>')
            sueltas = []
        bloques.append(seccion_funcion(idioma, lado, funcion))
        lado += 1
    if sueltas:
        bloques.append(f'<div class="funciones-sueltas">{"".join(sueltas)}</div>')
    return "".join(bloques)


# ---------------------------------------------------------------- la página

def pagina(idioma: str, t: dict) -> str:
    dir_ = "rtl" if idioma.split("-")[0] in RTL else "ltr"
    pasos = "".join(
        f'<li class="paso reveal" style="--retraso: {i * 90}ms"><span class="numero">{i + 1}</span>'
        f'<h3>{titulo}</h3><p>{texto}</p>'
        f'<div class="paso-pieza" aria-hidden="true">{pieza(idioma, PASOS[i])}</div></li>'
        for i, (titulo, texto) in enumerate(t["pasos"]))
    # Sin autoplay a propósito: las arranca el JavaScript, las seis a la vez.
    deportes = "".join(
        f'<li class="deporte reveal" style="--retraso: {i * 70}ms">'
        f'<video src="../static/deportes/{RAQUETAS[i]}.mp4" poster="../static/deportes/{RAQUETAS[i]}.jpg"'
        f' width="{ANCHO_DEPORTE}" height="{ANCHO_DEPORTE}" muted loop playsinline preload="none"'
        f' disablepictureinpicture aria-hidden="true"></video>'
        f'<h3>{nombre}</h3></li>'
        for i, nombre in enumerate(t["deportes"]))
    funciones = bloque_funciones(idioma, t["funciones"])
    reloj_puntos = "".join(f"<li>{p}</li>" for p in t["reloj_puntos"])
    faq = "".join(
        f'<details class="reveal"><summary>{p}</summary><p>{r}</p></details>'
        for p, r in t["faq"])
    nav = "".join(f'<a href="#{ancla}">{texto}</a>' for ancla, texto in
                  zip(["funciones", "reloj", "precio", "preguntas"], t["nav"]))

    def plan(datos: tuple, destacado: bool = False, precio=None) -> str:
        """Una tarjeta de plan. `precio` cambia solo la cifra: las ventajas
        del plan son las mismas se pague al mes o al año."""
        nombre, suyo, puntos = datos
        precio = precio or suyo
        lista = "".join(f"<li>{p}</li>" for p in puntos)
        return (f'<div class="plan{" destacado" if destacado else ""} reveal">'
                f'<h3>{nombre}</h3><p class="precio">{precio}</p>'
                f'<ul class="marcas">{lista}</ul></div>')

    legal = enlaces_legales(t, "")
    alternativos = "".join(f'<link rel="alternate" hreflang="{c}" href="../{c}/">' for c in TEXTOS)

    return f'''<!doctype html>
<html lang="{idioma}" dir="{dir_}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t["titulo_pagina"]}</title>
<meta name="description" content="{t["descripcion"]}">
<meta property="og:title" content="{t["titulo_pagina"]}">
<meta property="og:description" content="{t["descripcion"]}">
<meta property="og:type" content="website">
<meta property="og:image" content="../static/rackers.png">
<meta name="theme-color" content="#0B1322">
<link rel="icon" href="../static/rackers.png">
<link rel="stylesheet" href="../static/rackers.css?v={VERSION_CSS}">
{alternativos}
</head>
<body id="arriba">
<div class="ambiente" aria-hidden="true"><span class="luz lima"></span><span class="luz rosa"></span></div>

<header class="cabecera">
  <nav>
    {marca()}
    <div class="enlaces">{nav}</div>
    <div class="acciones">{selector(idioma)}{boton(t["pronto_corto"], "pequeno")}</div>
  </nav>
</header>

<main>
  <section class="hero">
    <div class="hero-texto">
      <h1>{"<br>".join(t["hero_titulo"])}</h1>
      <p class="entrada">{t["hero_texto"]}</p>
      <div class="hero-botones">{boton(t["pronto"])}
        <a class="enlace-suave" href="#funciones">{t["hero_enlace"]} <span aria-hidden="true">↓</span></a>
      </div>
      <p class="nota">{t["hero_nota"]}</p>
    </div>
    <div class="hero-pieza">
      {movil(idioma, "inicio", "hero-movil")}
    </div>
  </section>

  <section class="deportes" id="deportes">
    <h2 class="reveal">{t["deportes_titulo"]}</h2>
    <p class="entrada reveal">{t["deportes_texto"]}</p>
    <ul class="rejilla-deportes">{deportes}</ul>
  </section>

  <section class="pasos">
    <h2 class="reveal">{t["pasos_titulo"]}</h2>
    <ol class="rejilla-pasos">{pasos}</ol>
  </section>

  <section id="funciones" class="funciones">
    <h2 class="reveal">{t["funciones_titulo"]}</h2>
    {funciones}
  </section>

  <section id="reloj" class="reloj reveal">
    <div class="reloj-texto">
      <h2>{t["reloj_titulo"]}</h2>
      <p>{t["reloj_texto"]}</p>
      <ul class="marcas">{reloj_puntos}</ul>
    </div>
    <div class="reloj-pieza" aria-hidden="true">
      {reloj(idioma)}
    </div>
  </section>

  <section id="precio" class="precio">
    <h2 class="reveal">{t["precio_titulo"]}</h2>
    <p class="entrada reveal">{t["precio_texto"]}</p>
    <div class="pestanas" role="tablist">
      <button class="pestana activa" type="button" role="tab" aria-selected="true" data-panel="mes">{t["precio_periodos"][0]}</button>
      <button class="pestana" type="button" role="tab" aria-selected="false" data-panel="ano">{t["precio_periodos"][1]}</button>
      <button class="pestana" type="button" role="tab" aria-selected="false" data-panel="siempre">{t["precio_siempre"][0]}</button>
    </div>
    <div class="planes" data-panel="mes">{plan(t["precio_gratis"])}{plan(t["precio_pro"], True)}{plan(t["precio_familia"])}</div>
    <div class="planes oculto" data-panel="ano">{plan(t["precio_gratis"])}\
{plan(t["precio_pro"], True, t["precio_pro_anual"])}\
{plan(t["precio_familia"], False, t["precio_familia_anual"])}</div>
    <div class="planes oculto" data-panel="siempre">{plan(t["precio_siempre"], True)}</div>
  </section>

  <section id="preguntas" class="preguntas">
    <h2 class="reveal">{t["faq_titulo"]}</h2>
    <div class="lista-preguntas">{faq}</div>
  </section>

  <section class="cierre reveal">
    <h2>{t["cta_titulo"]}</h2>
    <p class="entrada">{t["cta_texto"]}</p>
    {boton(t["pronto"])}
  </section>
</main>

<footer>
  <div class="pie">
    {marca()}
    <p class="nota">{t["footer_nota"]}</p>
    <div class="pie-legal">{legal}</div>
    <label class="pie-idioma">{t["footer_idioma"]}{selector(idioma)}</label>
  </div>
  <p class="copyright">© Rackers</p>
</footer>

<script src="../static/rackers.js?v={VERSION_JS}" defer></script>
</body>
</html>
'''


# ---------------------------------------------------------------- estático

CSS = """/* El mismo azul, el mismo lima y la misma luz que la app. */
:root {
  --navy: #0B1322;
  --navy-alto: #131D33;
  --superficie: #16213A;
  --lima: #B6F24E;
  --lima-oscuro: #8CCB2A;
  --rosa: #FF7AB8;
  --crema: #F4F7FF;
  --apagado: #9AA7BF;
  --borde: rgba(244, 247, 255, .09);
  --radio: 26px;
  --ancho: 1180px;
  /* Lo que mide la cabecera pegajosa, que es igual en todos los tamaños. */
  --cabecera: 70px;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; }

body {
  background: var(--navy);
  color: var(--crema);
  font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Segoe UI", Inter, system-ui, sans-serif;
  font-size: 17px;
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
  overflow-x: hidden;
}

/* La luz de ambiente: dos manchas que respiran muy despacio, como el fondo
   de la app. Van fijas y detrás de todo. */
.ambiente { position: fixed; inset: 0; z-index: -1; overflow: hidden; }
.luz { position: absolute; border-radius: 50%; filter: blur(120px); opacity: .5; }
.luz.lima {
  width: 62vw; height: 62vw; top: -18vw; left: -12vw;
  background: radial-gradient(circle, rgba(182, 242, 78, .34), transparent 68%);
  animation: respira 18s ease-in-out infinite;
}
.luz.rosa {
  width: 52vw; height: 52vw; bottom: -16vw; right: -14vw;
  background: radial-gradient(circle, rgba(255, 122, 184, .22), transparent 68%);
  animation: respira 24s ease-in-out infinite reverse;
}
@keyframes respira {
  0%, 100% { transform: translate3d(0, 0, 0) scale(1); }
  50% { transform: translate3d(2vw, 3vw, 0) scale(1.12); }
}

img { display: block; max-width: 100%; height: auto; }
a { color: inherit; text-decoration: none; }

h1, h2, h3 { line-height: 1.04; letter-spacing: -.03em; font-weight: 800; }
h1 { font-size: clamp(42px, 6.4vw, 78px); }
h2 { font-size: clamp(30px, 4.2vw, 52px); }
h3 { font-size: clamp(22px, 2.4vw, 30px); letter-spacing: -.02em; }
p { color: var(--apagado); }
.entrada { font-size: clamp(17px, 1.6vw, 21px); max-width: 62ch; }
.nota { font-size: 15px; color: var(--apagado); opacity: .8; }

section { max-width: var(--ancho); margin: 0 auto; padding: clamp(60px, 8vw, 112px) 24px; }
/* Al saltar a una sección desde el menú tiene que quedar debajo de la
   cabecera, no tapada por ella. En pantalla ancha el propio relleno de la
   sección ya la salvaba; en el móvil baja a 60 px y el titular se comía la
   cabecera. */
section[id] { scroll-margin-top: var(--cabecera); }

/* --- Cabecera --- */
.cabecera {
  position: sticky; top: 0; z-index: 50;
  backdrop-filter: blur(18px); -webkit-backdrop-filter: blur(18px);
  background: rgba(11, 19, 34, .55);
  border-bottom: 1px solid transparent;
  transition: background .3s ease, border-color .3s ease;
}
.cabecera.pegada { background: rgba(11, 19, 34, .88); border-bottom-color: var(--borde); }
.cabecera nav {
  max-width: var(--ancho); margin: 0 auto; padding: 14px 24px;
  display: flex; align-items: center; gap: 24px;
}
.marca { display: flex; align-items: center; }
/* El logotipo ya trae su resplandor dentro del PNG: nada de drop-shadow aquí,
   que se lo pondría también a las letras. */
.marca img { height: 34px; width: auto; }
.enlaces { display: flex; gap: 22px; margin-inline-start: auto; font-size: 15px; color: var(--apagado); }
.enlaces a { transition: color .2s ease; }
.enlaces a:hover { color: var(--crema); }
.acciones { display: flex; align-items: center; gap: 12px; }

.idiomas {
  appearance: none; background: rgba(244, 247, 255, .06); color: var(--crema);
  border: 1px solid var(--borde); border-radius: 999px; padding: 8px 14px;
  font: inherit; font-size: 14px; cursor: pointer; max-width: 190px;
}
.idiomas option { background: var(--navy-alto); }

/* --- Botón --- */
.boton {
  display: inline-flex; align-items: center; gap: 10px;
  background: linear-gradient(160deg, var(--lima), var(--lima-oscuro));
  color: #0A1020; font-weight: 700; font-size: 17px;
  padding: 15px 26px; border-radius: 999px;
  box-shadow: 0 0 0 rgba(182, 242, 78, .5), 0 14px 34px -14px rgba(182, 242, 78, .75);
  transition: transform .25s cubic-bezier(.2, .8, .3, 1), box-shadow .25s ease;
  animation: latido 3.6s ease-in-out infinite;
}
.boton:hover { transform: translateY(-2px) scale(1.02); box-shadow: 0 0 34px rgba(182, 242, 78, .4), 0 18px 40px -14px rgba(182, 242, 78, .8); }
.boton.pequeno { padding: 9px 18px; font-size: 15px; animation: none; }
/* Mientras la app no esté publicada, el botón es un cartel: se ve igual pero
   no lleva a ningún sitio, así que no se comporta como si se pudiera pulsar. */
.boton.pronto { cursor: default; }
.boton.pronto:hover { transform: none; box-shadow: 0 0 0 rgba(182, 242, 78, .5), 0 14px 34px -14px rgba(182, 242, 78, .75); }
@keyframes latido {
  0%, 100% { box-shadow: 0 0 0 rgba(182, 242, 78, 0), 0 14px 34px -14px rgba(182, 242, 78, .75); }
  50% { box-shadow: 0 0 30px rgba(182, 242, 78, .35), 0 14px 34px -14px rgba(182, 242, 78, .75); }
}
.enlace-suave { color: var(--lima); font-weight: 600; display: inline-flex; align-items: center; gap: 6px; }
.enlace-suave span { transition: transform .25s ease; }
.enlace-suave:hover span { transform: translateY(3px); }

/* --- El móvil --- */
.movil { perspective: 1200px; width: min(100%, 330px); margin-inline: auto; }
.hero-movil { width: min(100%, 360px); }
/* El marco es el PNG oficial de Apple con el hueco de la pantalla
   transparente: la captura va debajo, colocada en el hueco con los
   porcentajes que salen de medir el propio PNG. La sombra y el resplandor se
   le ponen al marco, no a una caja, para que sigan su silueta. */
.marco { position: relative; container-type: inline-size; }
.marco .bisel {
  position: relative; z-index: 2; display: block; width: 100%; height: auto;
  filter: drop-shadow(0 50px 90px rgba(0, 0, 0, .75))
          drop-shadow(0 0 70px rgba(182, 242, 78, .22));
}
.marco .pantalla-app {
  position: absolute; z-index: 1; object-fit: cover;
  /* El hueco de Apple es un squircle; con esquinas cuadradas la captura
     asomaría en pico. 17cqw es algo más de lo justo, así que se mete bajo
     el titanio y no se ve el corte. */
  border-radius: 17cqw;
}
.hero-movil .marco { transform: rotate(-2deg); }
.flota { will-change: transform; }

/* --- Hero --- */
.hero {
  display: grid; grid-template-columns: 1fr 1.02fr; gap: clamp(28px, 5vw, 64px);
  align-items: center; padding-top: clamp(48px, 6vw, 88px); padding-bottom: clamp(56px, 8vw, 110px);
}
.hero h1 { margin-bottom: 20px; }
.hero .entrada { margin-bottom: 30px; }
.hero-botones { display: flex; align-items: center; gap: 22px; flex-wrap: wrap; margin-bottom: 16px; }

.hero-pieza .movil { width: min(100%, 300px); }

/* --- Deportes: seis cuadrados, uno por raqueta --- */
/* El vídeo ya trae el fondo azul y el brillo de la app, así que la tarjeta
   no pinta nada encima: solo lo recorta, lo enmarca y deja sitio al nombre. */
.rejilla-deportes {
  list-style: none; padding: 0; margin: 44px 0 0;
  display: grid; gap: 18px;
  grid-template-columns: repeat(3, 1fr);
}
.deporte {
  position: relative; overflow: hidden;
  border: 1px solid var(--borde); border-radius: var(--radio);
  transition: transform .35s cubic-bezier(.2, .8, .3, 1),
              box-shadow .35s ease, border-color .35s ease;
}
.deporte video { display: block; width: 100%; height: auto; aspect-ratio: 1; object-fit: cover; }
/* Un velo de abajo arriba para que el nombre se lea sin tapar la raqueta. */
.deporte::after {
  content: ""; position: absolute; inset: auto 0 0; height: 58%;
  background: linear-gradient(180deg, transparent, rgba(6, 10, 22, .93));
  pointer-events: none;
}
.deporte h3 {
  position: absolute; inset: auto 0 0; z-index: 1; margin: 0;
  padding: 0 20px 18px; font-size: clamp(18px, 1.6vw, 22px);
}
.deporte:hover {
  transform: translateY(-5px);
  border-color: rgba(182, 242, 78, .45);
  box-shadow: 0 0 38px rgba(182, 242, 78, .18), 0 24px 48px -20px rgba(0, 0, 0, .85);
}

/* --- Pasos --- */
.rejilla-pasos { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 44px; list-style: none; }
.paso, .funcion-suelta {
  background: linear-gradient(180deg, rgba(244, 247, 255, .06), rgba(244, 247, 255, .02));
  border: 1px solid var(--borde); border-radius: var(--radio); padding: 28px;
  position: relative; overflow: hidden;
}
.paso::before, .funcion-suelta::before {
  content: ""; position: absolute; inset: 0 0 auto; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(182, 242, 78, .6), transparent);
}
.paso { display: flex; flex-direction: column; }
/* La captura de cada paso asoma por abajo de la tarjeta, cortada: se ve la
   parte de arriba de la pantalla, que es la que cuenta, y la tarjeta no se
   hace torre. Va pegada al fondo para que las tres queden a la misma altura
   aunque los textos no midan lo mismo. */
.paso-pieza {
  margin: auto -28px -28px; padding-top: 26px; height: 400px; overflow: hidden;
  -webkit-mask-image: linear-gradient(to bottom, #000 72%, transparent);
          mask-image: linear-gradient(to bottom, #000 72%, transparent);
}
.paso-pieza .movil { width: min(74%, 250px); }
.paso-pieza .marco-reloj { width: min(66%, 220px); margin: 12px auto 0; }
/* Aquí el marco va sin su resplandor lima: la tarjeta corta la captura por
   arriba y el resplandor se quedaba cortado en recto. */
.paso-pieza .marco .bisel, .paso-pieza .marco-reloj .bisel {
  filter: drop-shadow(0 24px 40px rgba(0, 0, 0, .55));
}
.numero {
  display: grid; place-items: center; width: 38px; height: 38px; border-radius: 12px;
  background: rgba(182, 242, 78, .14); color: var(--lima); font-weight: 800; margin-bottom: 14px;
}
.paso h3 { margin-bottom: 8px; }

/* --- Funciones --- */
.funciones h2 { margin-bottom: clamp(36px, 6vw, 72px); }
.funcion {
  display: grid; grid-template-columns: 1fr 1fr; gap: clamp(28px, 5vw, 76px);
  align-items: center; margin-bottom: clamp(64px, 9vw, 130px);
}
.funcion.derecha .funcion-texto { order: 2; }
.funcion h3 { margin-bottom: 14px; }
.funcion p { margin-bottom: 20px; font-size: 18px; }
/* Las que ya enseñan su captura en los pasos: solo texto, de dos en dos. */
.funciones-sueltas {
  display: grid; grid-template-columns: 1fr 1fr; gap: 20px;
  margin-bottom: clamp(64px, 9vw, 130px);
}
.funcion-suelta h3 { margin-bottom: 12px; }
.funcion-suelta p { margin-bottom: 18px; }
.marcas { list-style: none; display: grid; gap: 10px; }
.marcas li { position: relative; padding-inline-start: 26px; color: var(--crema); font-size: 16px; }
.marcas li::before {
  content: ""; position: absolute; inset-inline-start: 0; top: .55em;
  width: 9px; height: 9px; border-radius: 50%;
  background: var(--lima); box-shadow: 0 0 12px rgba(182, 242, 78, .8);
}

/* --- El reloj --- */
.reloj {
  display: grid; grid-template-columns: 1.1fr .9fr; gap: clamp(28px, 5vw, 64px); align-items: center;
  background: linear-gradient(150deg, rgba(182, 242, 78, .10), rgba(255, 122, 184, .06) 55%, transparent);
  border: 1px solid var(--borde); border-radius: 42px;
  max-width: var(--ancho); margin: 0 auto; padding: clamp(36px, 6vw, 72px);
}
.reloj h2 { margin-bottom: 16px; }
.reloj p { margin-bottom: 22px; font-size: 18px; }
.reloj-pieza { position: relative; display: grid; place-items: center; min-height: 300px; }
/* Igual que el móvil: el marco oficial de Apple encima y la captura debajo.
   Aquí el bisel tapa las esquinas de la pantalla, así que no hace falta
   redondear la captura. */
.marco-reloj { position: relative; width: min(100%, 290px); }
.marco-reloj .bisel {
  position: relative; z-index: 2; display: block; width: 100%; height: auto;
  filter: drop-shadow(0 34px 60px rgba(0, 0, 0, .8))
          drop-shadow(0 0 54px rgba(182, 242, 78, .3));
}
.marco-reloj .pantalla-app { position: absolute; z-index: 1; object-fit: cover; }
@keyframes pulso { 0%, 100% { opacity: .55; } 50% { opacity: 1; } }

/* --- Precio --- */
/* Centrado solo para las pestañas; el texto de la sección y el de dentro de
   las tarjetas sigue alineado a su lado. */
.precio { text-align: center; }
/* Ojo: la sección y el precio de la tarjeta comparten la clase `precio`, así
   que hay que devolverle la alineación también al de dentro. */
.precio h2, .precio .entrada, .precio .plan, .plan .precio { text-align: start; }
.precio h2 { margin-bottom: 14px; }
.precio .entrada { margin-bottom: 40px; }
/* Las pestañas del precio: mensual, anual y de por vida. Cada panel trae sus
   tarjetas ya escritas; el JS solo enseña uno y esconde los otros. Sin JS se
   ven los tres seguidos, que es peor pero se lee todo. */
.pestanas {
  display: inline-flex; flex-wrap: wrap; max-width: 100%; gap: 4px; margin: 0 auto 26px; padding: 5px;
  background: rgba(244, 247, 255, .05); border: 1px solid var(--borde);
  border-radius: 999px;
}
.pestana {
  appearance: none; border: 0; background: none; cursor: pointer;
  color: var(--apagado); font: inherit; font-size: 15px; font-weight: 700;
  padding: 10px 22px; border-radius: 999px;
  transition: background .25s ease, color .25s ease;
}
.pestana:hover { color: var(--crema); }
.pestana.activa {
  background: linear-gradient(160deg, var(--lima), var(--lima-oscuro));
  color: #0A1020; box-shadow: 0 0 26px -6px rgba(182, 242, 78, .6);
}
.planes.oculto { display: none; }
/* Uno, dos o tres planes según la pestaña: que no se estiren a lo ancho. */
.planes {
  display: grid; gap: 18px; margin-bottom: 20px;
  grid-template-columns: repeat(auto-fit, minmax(0, 320px)); justify-content: center;
}
.plan {
  background: linear-gradient(180deg, rgba(244, 247, 255, .06), rgba(244, 247, 255, .02));
  border: 1px solid var(--borde); border-radius: 28px; padding: 26px 22px;
}
.plan.destacado {
  border-color: rgba(182, 242, 78, .45);
  box-shadow: 0 0 60px -22px rgba(182, 242, 78, .7);
  background: linear-gradient(180deg, rgba(182, 242, 78, .10), rgba(244, 247, 255, .02));
}
.plan h3 { margin-bottom: 6px; }
.precio-plan, .plan .precio { font-size: 30px; font-weight: 800; color: var(--lima); margin-bottom: 20px; letter-spacing: -.02em; }

/* --- Preguntas --- */
.preguntas h2 { margin-bottom: 36px; }
.lista-preguntas { display: grid; gap: 12px; }
details {
  background: rgba(244, 247, 255, .04); border: 1px solid var(--borde);
  border-radius: 20px; padding: 18px 22px; transition: border-color .25s ease;
}
details[open] { border-color: rgba(182, 242, 78, .35); }
summary { cursor: pointer; font-weight: 700; font-size: 18px; list-style: none; display: flex; justify-content: space-between; gap: 16px; }
summary::-webkit-details-marker { display: none; }
summary::after { content: "+"; color: var(--lima); font-weight: 800; transition: transform .25s ease; }
details[open] summary::after { transform: rotate(45deg); }
details p { margin-top: 12px; }

/* --- Cierre y pie --- */
.cierre { text-align: center; }
.cierre h2 { margin-bottom: 14px; }
.cierre .entrada { margin: 0 auto 28px; }
footer { border-top: 1px solid var(--borde); padding: 44px 24px 34px; }
.pie { max-width: var(--ancho); margin: 0 auto; display: flex; flex-wrap: wrap; gap: 18px 32px; align-items: center; }
.pie .nota { margin-inline-end: auto; }
.pie-legal { display: flex; gap: 14px; font-size: 15px; color: var(--apagado); }
.pie-legal a { color: var(--apagado); transition: color .2s ease; }
.pie-legal a:hover { color: var(--crema); }

/* --- Privacidad, Condiciones y Soporte --- */
.documento {
  max-width: 760px; margin: 0 auto; padding: clamp(48px, 7vw, 96px) 24px clamp(60px, 8vw, 112px);
}
.documento h1 { font-size: clamp(38px, 5.4vw, 62px); margin: 0 0 18px; }
.documento .entrada { margin: 0 0 10px; color: var(--crema); }
.documento .nota { margin: 0 0 40px; }
.apartado { margin-bottom: 34px; }
.apartado h2 {
  font-size: clamp(19px, 2vw, 23px); letter-spacing: -.02em; margin: 0 0 10px; color: var(--lima);
}
.apartado p { margin: 0 0 12px; color: var(--apagado); line-height: 1.65; max-width: 62ch; }
.apartado.correo {
  background: rgba(244, 247, 255, .04); border: 1px solid var(--borde);
  border-radius: 20px; padding: 24px 26px; margin-bottom: 40px;
}
.correo-enlace { font-size: clamp(21px, 2.6vw, 28px); font-weight: 800; color: var(--lima); }
.correo-enlace:hover { text-decoration: underline; }
.volver { font-size: 15px; color: var(--apagado); transition: color .2s ease; }
.volver:hover { color: var(--crema); }
.pie-idioma { display: flex; align-items: center; gap: 10px; font-size: 14px; color: var(--apagado); }
.copyright { max-width: var(--ancho); margin: 22px auto 0; font-size: 14px; color: var(--apagado); opacity: .7; }

/* --- Las animaciones de entrada --- */
.reveal { opacity: 0; transform: translateY(26px); }
.reveal.visto {
  opacity: 1; transform: none;
  transition: opacity .7s cubic-bezier(.2, .8, .3, 1) var(--retraso, 0ms),
              transform .7s cubic-bezier(.2, .8, .3, 1) var(--retraso, 0ms);
}

/* --- Pantallas estrechas --- */
@media (max-width: 900px) {
  .hero, .funcion, .funcion.derecha, .reloj { grid-template-columns: 1fr; }
  .funcion.derecha .funcion-texto { order: 0; }
  .hero-movil .marco { transform: none; }
  .movil { max-width: 320px; margin: 0 auto; }
  .rejilla-pasos, .funciones-sueltas { grid-template-columns: 1fr; }
  /* Seis cuadrados: tres columnas en pantalla grande, dos aquí. */
  .rejilla-deportes { grid-template-columns: repeat(2, 1fr); gap: 14px; }
  .enlaces { display: none; }
  .acciones { margin-inline-start: auto; }
  .idiomas { max-width: 130px; }
}
@media (max-width: 520px) {
  /* Las tres pestañas en una línea: con el relleno de escritorio, «Para
     siempre» partía en dos y dejaba la píldora torcida. */
  .pestana { padding: 9px 13px; font-size: 14px; }
  /* En dos columnas los nombres largos parten en dos líneas: más velo y
     menos cuerpo, para que no se echen encima de la raqueta. */
  .deporte h3 { font-size: 16px; padding: 0 14px 13px; }
  .deporte::after { height: 70%; }
  .marca img { height: 28px; }
  /* En el móvil no caben logotipo, selector y botón: el selector se va, que
     el del pie hace lo mismo. Sin esto el botón se salía de la pantalla. */
  .acciones .idiomas { display: none; }
  .boton { font-size: 16px; padding: 14px 22px; }
}

/* Quien pide menos movimiento, no ve ninguno. */
@media (prefers-reduced-motion: reduce) {
  html { scroll-behavior: auto; }
  .reveal { opacity: 1; transform: none; }
  .luz, .boton, .pantalla::after { animation: none; }
  * { transition-duration: .01ms !important; }
}
"""

JS = """// Las animaciones de la web: aparecer al llegar, el móvil que flota, la
// cabecera que se opaca y las raquetas de los deportes. Nada de librerías.
(() => {
  const suave = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Aparecer al entrar en pantalla, en cascada dentro de cada bloque.
  const porVer = document.querySelectorAll('.reveal');
  if (!suave || !('IntersectionObserver' in window)) {
    porVer.forEach((e) => e.classList.add('visto'));
  } else {
    const vigia = new IntersectionObserver((entradas) => {
      entradas.forEach((entrada) => {
        if (!entrada.isIntersecting) return;
        entrada.target.classList.add('visto');
        vigia.unobserve(entrada.target);
      });
    }, { rootMargin: '0px 0px -12% 0px', threshold: .12 });
    porVer.forEach((e) => vigia.observe(e));
  }

  // La cabecera se vuelve opaca en cuanto se baja.
  const cabecera = document.querySelector('.cabecera');
  const alBajar = () => cabecera.classList.toggle('pegada', window.scrollY > 12);
  alBajar();
  addEventListener('scroll', alBajar, { passive: true });

  // Los móviles de las funciones se mueven un poco menos que la página: da
  // profundidad sin marear. Solo en pantallas anchas y con el motor del
  // navegador, para que no cueste nada.
  const flotantes = [...document.querySelectorAll('.flota')];
  if (suave && flotantes.length && innerWidth > 900) {
    let pedido = false;
    const mover = () => {
      pedido = false;
      const centro = innerHeight / 2;
      flotantes.forEach((pieza) => {
        const caja = pieza.getBoundingClientRect();
        if (caja.bottom < -200 || caja.top > innerHeight + 200) return;
        const desvio = (caja.top + caja.height / 2 - centro) / centro;
        pieza.style.transform = `translate3d(0, ${(desvio * -22).toFixed(1)}px, 0)`;
      });
    };
    addEventListener('scroll', () => {
      if (pedido) return;
      pedido = true;
      requestAnimationFrame(mover);
    }, { passive: true });
    mover();
  }

  // Las raquetas de los deportes. Cada una gira en un momento distinto del
  // bucle, así que si van a la par el giro pasa de una a otra como una ola.
  // Arrancan las seis cuando la rejilla está a punto de verse y se paran al
  // salir. Quien pide menos movimiento se queda con el cartel, que es el
  // primer fotograma.
  const raquetas = [...document.querySelectorAll('.deporte video')];
  if (suave && raquetas.length) {
    // Cada una echa a andar según le llegan los datos, y el móvil puede
    // frenar alguna. La que va detrás de la primera acelera un poco y la que
    // va delante frena, hasta ir a la par. Saltar al segundo exacto no vale:
    // en un móvil lento el salto tarda más que el desfase que corrige, se
    // queda otra vez atrás y salta sin parar. Solo salta si se ha ido más de
    // un segundo, y nunca mientras está saltando.
    const lider = raquetas[0];
    lider.addEventListener('timeupdate', () => {
      const t = lider.currentTime, d = lider.duration;
      raquetas.forEach((v) => {
        if (v === lider) return;
        let atras = t - v.currentTime;
        // Módulo la duración: si la primera va en 5,99 s y otra ya ha dado
        // la vuelta y va en 0,01, esa va 0,02 s por delante, no 5,98 detrás.
        if (atras > d / 2) atras -= d;
        if (atras < -d / 2) atras += d;
        if (Math.abs(atras) > 1) {
          if (!v.seeking) v.currentTime = t;
        } else {
          v.playbackRate = Math.abs(atras) < .03 ? 1 : 1 + Math.max(-.25, Math.min(.25, atras));
        }
      });
    });
    const jugar = () => raquetas.forEach((v) => v.play().catch(() => {}));
    const parar = () => raquetas.forEach((v) => v.pause());
    if ('IntersectionObserver' in window) {
      // Si llegan varios avisos juntos (entrar y salir con un tirón de
      // scroll), manda el último.
      new IntersectionObserver((avisos) => (avisos[avisos.length - 1].isIntersecting ? jugar() : parar()),
                               { rootMargin: '120px 0px' })
        .observe(document.querySelector('.rejilla-deportes'));
    } else {
      jugar();
    }
  }

  // Las pestañas del precio. Los tres paneles vienen escritos en el HTML, así
  // que sin JavaScript se ven los tres seguidos: se lee todo igual, solo que
  // sin poder elegir.
  const pestanas = [...document.querySelectorAll('.pestana')];
  if (pestanas.length) {
    const paneles = [...document.querySelectorAll('.planes[data-panel]')];
    pestanas.forEach((p) => p.addEventListener('click', () => {
      pestanas.forEach((otra) => {
        const suya = otra === p;
        otra.classList.toggle('activa', suya);
        otra.setAttribute('aria-selected', suya ? 'true' : 'false');
      });
      paneles.forEach((panel) => panel.classList.toggle('oculto', panel.dataset.panel !== p.dataset.panel));
    }));
  }

})();
"""

# La raíz manda a cada uno a su idioma, y si no lo tenemos, al inglés.
def portada() -> str:
    codigos = ", ".join(f'"{c}"' for c in TEXTOS)
    enlaces = "".join(f'<li><a href="{c}/">{d["idioma"]}</a></li>' for c, d in
                      sorted(TEXTOS.items(), key=lambda p: p[1]["idioma"]))
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Rackers</title><link rel="stylesheet" href="static/rackers.css">
<script>
  const hay = [{codigos}];
  const quiere = navigator.languages || [navigator.language || "en"];
  let elegido = "en-US";
  for (const pedido of quiere) {{
    const exacto = hay.find((c) => c.toLowerCase() === pedido.toLowerCase());
    const base = hay.find((c) => c.toLowerCase().startsWith(pedido.toLowerCase().split("-")[0]));
    if (exacto || base) {{ elegido = exacto || base; break; }}
  }}
  location.replace(elegido + "/");
</script></head>
<body><section><h1>Rackers</h1><ul class="marcas">{enlaces}</ul></section></body></html>
'''


def escribir(idiomas: list[str]) -> None:
    ESTATICO.mkdir(parents=True, exist_ok=True)
    (ESTATICO / "rackers.css").write_text(CSS, encoding="utf-8")
    (ESTATICO / "rackers.js").write_text(JS, encoding="utf-8")
    preparar_imagenes(idiomas)
    preparar_deportes()
    for idioma in idiomas:
        carpeta = SALIDA / idioma
        carpeta.mkdir(parents=True, exist_ok=True)
        (carpeta / "index.html").write_text(pagina(idioma, TEXTOS[idioma]), encoding="utf-8")
        # Privacidad, Condiciones y Soporte, cada una en su carpeta para que la
        # URL quede limpia: rackers.app/es-ES/privacidad/
        for slug in PAGINAS:
            if f"{slug}_titulo" not in TEXTOS[idioma]:
                continue
            aparte = carpeta / slug
            aparte.mkdir(parents=True, exist_ok=True)
            (aparte / "index.html").write_text(documento(idioma, TEXTOS[idioma], slug), encoding="utf-8")
        print(f"  {idioma}")
    (SALIDA / "index.html").write_text(portada(), encoding="utf-8")


class ConRangos(http.server.SimpleHTTPRequestHandler):
    """El de la biblioteca estándar sirve el archivo entero y nada más.

    Al navegador eso no le vale para el vídeo: si no puede pedir trozos
    sueltos lo marca como no navegable y `currentTime` se queda clavado en
    cero, así que en local los vídeos no se movían aunque en Cloudflare sí.
    Esto responde a `Range` como responde la tienda de verdad."""

    def end_headers(self):
        self.send_header("Accept-Ranges", "bytes")
        super().end_headers()

    def send_head(self):
        rango = self.headers.get("Range", "")
        trozo = re.match(r"bytes=(\d*)-(\d*)$", rango.strip())
        ruta = self.translate_path(self.path)
        if not trozo or os.path.isdir(ruta):
            return super().send_head()
        try:
            archivo = open(ruta, "rb")
        except OSError:
            self.send_error(404)
            return None
        with archivo:
            total = os.fstat(archivo.fileno()).st_size
            desde = int(trozo.group(1)) if trozo.group(1) else 0
            hasta = min(int(trozo.group(2)) if trozo.group(2) else total - 1, total - 1)
            if desde > hasta:
                self.send_error(416)
                return None
            self.send_response(206)
            self.send_header("Content-Type", self.guess_type(ruta))
            self.send_header("Content-Range", f"bytes {desde}-{hasta}/{total}")
            self.send_header("Content-Length", str(hasta - desde + 1))
            self.end_headers()
            archivo.seek(desde)
            self.wfile.write(archivo.read(hasta - desde + 1))
        return None


def servir() -> None:
    os.chdir(SALIDA)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", 8000), ConRangos) as servidor:
        print("  http://localhost:8000")
        servidor.serve_forever()


# La huella del contenido va en la URL de `rackers.css` y `rackers.js`. Sin
# esto el navegador se queda con la copia vieja y la web se ve rota a medias:
# las capturas fuera de su marco, porque el HTML es nuevo pero el CSS y el JS
# que lo colocan son los de antes.
VERSION_CSS = hashlib.sha256(CSS.encode()).hexdigest()[:10]
VERSION_JS = hashlib.sha256(JS.encode()).hexdigest()[:10]


def main() -> None:
    pedidos = [a for a in sys.argv[1:] if not a.startswith("-")]
    idiomas = pedidos or list(TEXTOS)
    faltan = [i for i in idiomas if i not in TEXTOS]
    if faltan:
        sys.exit(f"Sin texto todavía: {', '.join(faltan)}")
    escribir(idiomas)
    print(f"{len(idiomas)} idiomas en web/publico/")
    if "--servir" in sys.argv:
        servir()


if __name__ == "__main__":
    main()
