"""Privacidad, Condiciones y Soporte en es-ES.

Lo que dice aquí tiene que casar con lo que hace el código: la copia de
seguridad sube partidos (con el pulso que midió el reloj), la salud de «Cómo
llegas hoy» no sale del iPhone y del vídeo del entrenador no se guarda nada.
Si eso cambia en la app o en el servidor, esto cambia también.
"""

TEXTO = {
    "legal_volver": "Volver a la portada",
    "legal_actualizado": "Actualizado el 23 de septiembre de 2026",

    # --- Privacidad ---------------------------------------------------------
    "privacidad_titulo": "Privacidad",
    "privacidad_entrada": "Rackers se hizo para jugar, no para recoger datos. "
                          "Aquí está en claro qué se guarda, dónde y cómo borrarlo.",
    "privacidad_secciones": [
        ("Sin cuenta no sale nada del iPhone", [
            "Puedes usar Rackers entera sin crear cuenta. Los partidos, los torneos y "
            "los ajustes se quedan en tu dispositivo y no viajan a ningún sitio.",
            "La cuenta sirve para tres cosas: que el iPhone y el reloj tengan lo mismo, "
            "que no pierdas nada al cambiar de móvil y poder jugar con amigos.",
        ]),
        ("Qué guarda la cuenta", [
            "La cuenta se crea con Iniciar sesión con Apple. Apple nos da un "
            "identificador estable, tu nombre y un correo, que será el de reenvío "
            "privado de Apple si eliges esconder el tuyo.",
            "Guardamos ese identificador, el correo, el nombre que enseñas y el "
            "@nombre que elijas. También el permiso que da Apple para poder retirar el "
            "acceso cuando borras la cuenta.",
        ]),
        ("La copia de seguridad", [
            "Con la cuenta puesta, la app sube su contenido: jugadores, jornadas, "
            "partidos, torneos, análisis y ajustes.",
            "Los partidos llevan dentro lo que midió el reloj mientras jugabas: pulso, "
            "distancia y energía. Va con el partido porque es del partido.",
        ]),
        ("Lo que no sale de tu iPhone", [
            "El pulso en reposo, la variabilidad y el sueño —lo de «Cómo llegas hoy»— "
            "se leen de la app Salud y se quedan en el dispositivo. No se suben al "
            "servidor ni se comparten con nadie.",
            "El permiso de Salud se puede retirar cuando quieras desde Ajustes › Salud "
            "› Acceso a datos, sin que la app deje de funcionar.",
        ]),
        ("El entrenador con IA", [
            "Cuando pides un análisis, la app saca fotogramas del vídeo y los manda a "
            "OpenAI a través de nuestro servidor, que devuelve el informe.",
            "Del vídeo no se guarda nada en el servidor. El informe vuelve a la app y "
            "se queda en tu copia.",
            "Sí queda el registro de cuántos análisis has pedido, de qué deporte y "
            "cuánto ocuparon. Sirve para los topes de uso y para saber lo que cuesta.",
        ]),
        ("La suscripción", [
            "Pro se cobra por App Store. No vemos ni guardamos tu tarjeta ni tus datos "
            "de pago en ningún momento.",
            "Usamos RevenueCat para saber si tu suscripción está al día, con el "
            "identificador de tu cuenta y nada más.",
        ]),
        ("Amigos y familia", [
            "Si te enlazas con alguien, se guarda que estáis enlazados y los partidos "
            "que compartís.",
            "Tu @nombre es cómo te encuentran los demás. Lo puedes cambiar cuando "
            "quieras.",
        ]),
        ("Dónde se guarda", [
            "En Cloudflare, en una base de datos D1. El servidor solo responde a la "
            "app y guarda lo que la app le manda.",
        ]),
        ("Ni anuncios ni rastreo", [
            "No hay publicidad. No hay seguimiento entre apps ni webs. No se vende ni "
            "se cede nada a terceros para que lo usen por su cuenta.",
        ]),
        ("Cómo borrarlo todo", [
            "Desde la app: Ajustes › Cuenta › Borrar cuenta. Se borra todo lo tuyo del "
            "servidor y se retira el acceso que diste con Apple.",
            "Lo que esté solo en el dispositivo se va al borrar la app.",
        ]),
        ("Menores", [
            "Rackers no está pensada para menores de 13 años y no les pedimos datos a "
            "sabiendas.",
        ]),
        ("Quién responde de esto", [
            "Del tratamiento de estos datos responde {responsable}, que trabaja por "
            "cuenta propia y publica Rackers a su nombre. Para cualquier cosa "
            "relacionada con tus datos, escribe a {correo}.",
            "Tienes derecho a ver lo tuyo, corregirlo, borrarlo, llevártelo a otro "
            "sitio y oponerte a que se trate. Lo más rápido es borrar la cuenta desde "
            "la app, pero si prefieres pedirlo por escrito, escribe y se hace.",
        ]),
        ("Cambios", [
            "Si esto cambia, se avisa en esta misma página con su fecha arriba.",
        ]),
    ],

    # --- Condiciones --------------------------------------------------------
    "condiciones_titulo": "Condiciones de uso",
    "condiciones_entrada": "Las reglas de usar Rackers, en corto y sin letra pequeña.",
    "condiciones_secciones": [
        ("Qué es esto", [
            "Rackers es un marcador y un cuaderno de partidos para pádel, tenis, "
            "pickleball, squash, tenis de mesa y bádminton, para iPhone y Apple Watch.",
            "Al usarla aceptas estas condiciones. Si no las aceptas, no la uses.",
        ]),
        ("Tu cuenta", [
            "La cuenta es tuya y respondes de lo que se haga con ella. El @nombre no "
            "puede suplantar a nadie ni ser ofensivo; si lo es, se puede retirar.",
        ]),
        ("Pro y los pagos", [
            "Rackers es gratis. Pro es una suscripción que se cobra por tu cuenta de "
            "App Store al confirmar la compra.",
            "Se renueva sola salvo que la canceles al menos 24 horas antes de que "
            "acabe el periodo. Se gestiona y se cancela en Ajustes de tu dispositivo › "
            "tu nombre › Suscripciones.",
            "Los reembolsos los da Apple, no nosotros, según sus propias normas.",
        ]),
        ("El plan familiar", [
            "El plan familiar da Pro a quien lo paga y a las cuentas que invite, hasta "
            "el límite que diga la app. Quien paga puede quitar a cualquiera cuando "
            "quiera.",
        ]),
        ("El entrenador no es un médico", [
            "El informe del entrenador y lo que la app calcule con tus datos de Salud "
            "son orientativos. No son diagnóstico, ni tratamiento, ni consejo médico o "
            "deportivo profesional.",
            "Si te encuentras mal o tienes dudas de salud, pregunta a un profesional.",
        ]),
        ("El servicio", [
            "Hacemos lo posible por que todo funcione, pero la app y el servidor se "
            "ofrecen tal cual, sin garantía de que estén disponibles sin interrupción "
            "ni de que no haya fallos.",
            "Guarda lo que te importe: la copia de seguridad ayuda, pero no sustituye "
            "a tus propias copias.",
        ]),
        ("Uso correcto", [
            "No se puede intentar romper el servicio, sacarle datos de otras cuentas "
            "ni usarlo para nada ilegal. Si pasa, se puede cerrar la cuenta.",
        ]),
        ("Cambios", [
            "Estas condiciones pueden cambiar. Los cambios se publican aquí con su "
            "fecha, y seguir usando la app es aceptarlos.",
        ]),
    ],

    # --- Soporte ------------------------------------------------------------
    "soporte_titulo": "Soporte",
    "soporte_entrada": "¿Algo no va, o se te ocurre algo mejor? Escribe y te "
                       "contestamos.",
    "soporte_correo_titulo": "Escríbenos",
    "soporte_correo_nota": "Contesta una persona. Si es un fallo, cuenta qué hacías, "
                           "qué esperabas y qué pasó, y di qué iPhone y qué versión de "
                           "iOS tienes: así se arregla antes.",
    "soporte_secciones": [
        ("Borrar tu cuenta", [
            "En la app: Ajustes › Cuenta › Borrar cuenta. Se borra todo lo tuyo del "
            "servidor y se retira el acceso de Apple. No hace falta escribirnos.",
        ]),
        ("La suscripción", [
            "Pro se gestiona y se cancela desde Ajustes de tu dispositivo › tu nombre "
            "› Suscripciones. Los reembolsos los da Apple desde reportaproblem.apple.com.",
        ]),
        ("El reloj no ve los partidos", [
            "El reloj y el iPhone se ponen al día cuando están cerca y los dos tienen "
            "la app abierta. Si no, abre Rackers en los dos y espera unos segundos.",
            "El reloj funciona solo: puedes puntuar un partido entero sin el iPhone "
            "encima y ya se pondrán de acuerdo luego.",
        ]),
        ("Salud y permisos", [
            "Para medir el pulso hace falta dar permiso a Salud. Si lo negaste, se "
            "vuelve a dar en Ajustes › Salud › Acceso a datos › Rackers.",
            "El pulso se mide con un entreno, así que el reloj se queda en la app "
            "mientras juegas.",
        ]),
        ("El entrenador", [
            "El análisis de vídeo es Pro y tiene un tope de usos al día y al mes. Si "
            "un análisis falla, no te cuenta.",
        ]),
    ],
}
