"""Privacidad, Condiciones y Soporte en ca.

Lo que dice aquí tiene que casar con lo que hace el código: la copia de
seguridad sube partidos (con el pulso que midió el reloj), la salud de «Cómo
llegas hoy» no sale del iPhone y del vídeo del entrenador no se guarda nada.
Si eso cambia en la app o en el servidor, esto cambia también.
"""

TEXTO = {
    "legal_volver": "Tornar a la portada",
    "legal_actualizado": "Actualitzat el 27 de setembre de 2026",

    # --- Privacidad ---------------------------------------------------------
    "privacidad_titulo": "Privacitat",
    "privacidad_entrada": "Rackers es va fer per jugar, no per recollir dades. Aquí "
                          "tens clar què es desa, on i com esborrar-ho.",
    "privacidad_secciones": [
        ("Sense compte no surt res de l'iPhone", [
            "Pots fer servir Rackers sencera sense crear cap compte. Els partits, els "
            "tornejos i els ajustos es queden al teu dispositiu i no viatgen enlloc.",
            "El compte serveix per a tres coses: que l'iPhone i el rellotge tinguin el "
            "mateix, que no perdis res en canviar de mòbil i poder jugar amb amics.",
        ]),
        ("Què desa el compte", [
            "El compte es crea amb Iniciar sessió amb Apple. Apple ens dona un "
            "identificador estable, el teu nom i un correu, que serà el de reenviament "
            "privat d'Apple si tries amagar el teu.",
            "Desem aquest identificador, el correu, el nom que ensenyes i el @nom que "
            "triïs. També el permís que dona Apple per poder retirar l'accés quan "
            "esborres el compte.",
        ]),
        ("La còpia de seguretat", [
            "Amb el compte posat, l'app puja el seu contingut: jugadors, jornades, "
            "partits, tornejos, anàlisis i ajustos.",
            "Els partits porten dins el que va mesurar el rellotge mentre jugaves: "
            "pols, distància i energia. Va amb el partit perquè és del partit.",
        ]),
        ("El que no surt del teu iPhone", [
            "El pols en repòs, la variabilitat i la son —el de «Com arribes avui»— es "
            "llegeixen de l'app Salut i es queden al dispositiu. No es pugen al "
            "servidor ni es comparteixen amb ningú.",
            "El permís de Salut es pot retirar quan vulguis des d'Ajustos › Salut › "
            "Accés a dades, sense que l'app deixi de funcionar.",
        ]),
        ("L'entrenador amb IA", [
            "Quan demanes una anàlisi, l'app treu fotogrames del vídeo i els envia a "
            "OpenAI a través del nostre servidor, que retorna l'informe.",
            "Del vídeo no es desa res al servidor. L'informe torna a l'app i es queda a "
            "la teva còpia.",
            "Sí que queda el registre de quantes anàlisis has demanat, de quin esport i "
            "quant ocupaven. Serveix per als límits d'ús i per saber què costa.",
        ]),
        ("La subscripció", [
            "Pro es cobra per App Store. No veiem ni desem la teva targeta ni les teves "
            "dades de pagament en cap moment.",
            "Fem servir RevenueCat per saber si la teva subscripció està al dia, amb "
            "l'identificador del teu compte i res més.",
        ]),
        ("Amics i família", [
            "Si t'enllaces amb algú, es desa que esteu enllaçats i els partits que "
            "compartiu.",
            "El teu @nom és com et troben els altres. El pots canviar quan vulguis.",
        ]),
        ("Tornejos", [
            "Si publiques un torneig, es desa el nom, l'esport, el format, la data, la pista i el nom de qui l'organitza. El quadre i els resultats es queden al teu iPhone i a la teva còpia.",
            "Un torneig públic el pot veure qualsevol a Tornejos › Públics i al seu enllaç de rackers.app, també sense compte. A un de privat només hi arriba qui en tingui el codi o l'enllaç.",
            "Si t'hi apuntes des del teu compte, qui l'organitza veu el nom amb què t'hi apuntes i rep un avís al seu iPhone. Et pots desapuntar quan vulguis, i en bloquejar algú es desfan les inscripcions entre tots dos.",
        ]),
        ("On es desa", [
            "A Cloudflare, en una base de dades D1. El servidor només respon a l'app i "
            "desa el que l'app li envia.",
        ]),
        ("Ni anuncis ni rastreig", [
            "No hi ha publicitat. No hi ha seguiment entre apps ni webs. No es ven ni "
            "es cedeix res a tercers perquè ho facin servir pel seu compte.",
        ]),
        ("Com esborrar-ho tot", [
            "Des de l'app: Ajustos › Compte › Esborrar el compte. S'esborra tot el teu "
            "del servidor i es retira l'accés que vas donar amb Apple.",
            "El que només sigui al dispositiu se'n va en esborrar l'app.",
        ]),
        ("Menors", [
            "Rackers no està pensada per a menors de 13 anys i no els demanem dades a "
            "posta.",
        ]),
        ("Qui en respon", [
            "Del tractament d'aquestes dades en respon {responsable}, que treballa pel "
            "seu compte i publica Rackers al seu nom. Per a qualsevol cosa relacionada "
            "amb les teves dades, escriu a {correo}.",
            "Tens dret a veure el que és teu, corregir-ho, esborrar-ho, endur-te'l a "
            "un altre lloc i oposar-te que es tracti. El més ràpid és esborrar el "
            "compte des de l'app, però si ho prefereixes per escrit, escriu i es fa.",
        ]),
        ("Canvis", [
            "Si això canvia, s'avisa en aquesta mateixa pàgina amb la data a dalt.",
        ]),
    ],

    # --- Condiciones --------------------------------------------------------
    "condiciones_titulo": "Condicions d'ús",
    "condiciones_entrada": "Les regles de fer servir Rackers, en curt i sense lletra "
                           "petita.",
    "condiciones_secciones": [
        ("Què és això", [
            "Rackers és un marcador i una llibreta de partits per a pàdel, tennis, "
            "pickleball, esquaix, tennis taula i bàdminton, per a iPhone i Apple Watch.",
            "En fer-la servir acceptes aquestes condicions. Si no les acceptes, no la "
            "facis servir.",
        ]),
        ("El teu compte", [
            "El compte és teu i respons del que s'hi faci. El @nom no pot suplantar "
            "ningú ni ser ofensiu; si ho és, es pot retirar.",
            "No es toleren insults, assetjament ni contingut ofensiu. Des de l'app pots bloquejar o denunciar qualsevol compte; les denúncies les revisa una persona en menys de 24 hores, i qui no compleixi aquestes normes perd el compte.",
        ]),
        ("Pro i els pagaments", [
            "Rackers és gratis. Pro és una subscripció que es cobra pel teu compte "
            "d'App Store en confirmar la compra.",
            "Es renova sola llevat que la cancel·lis almenys 24 hores abans que acabi "
            "el període. Es gestiona i es cancel·la a Ajustos del teu dispositiu › el "
            "teu nom › Subscripcions.",
            "Els reemborsaments els dona Apple, no nosaltres, segons les seves normes.",
        ]),
        ("El pla familiar", [
            "El pla familiar dona Pro a qui el paga i als comptes que convidi, fins al "
            "límit que digui l'app. Qui paga pot treure qualsevol quan vulgui.",
        ]),
        ("L'entrenador no és un metge", [
            "L'informe de l'entrenador i el que l'app calculi amb les teves dades de "
            "Salut són orientatius. No són diagnòstic, ni tractament, ni consell mèdic "
            "o esportiu professional.",
            "Si et trobes malament o tens dubtes de salut, pregunta a un professional.",
        ]),
        ("El servei", [
            "Fem el possible perquè tot funcioni, però l'app i el servidor s'ofereixen "
            "tal com són, sense garantia que estiguin disponibles sense interrupció ni "
            "que no hi hagi errors.",
            "Desa el que t'importi: la còpia de seguretat ajuda, però no substitueix "
            "les teves pròpies còpies.",
        ]),
        ("Ús correcte", [
            "No es pot intentar trencar el servei, treure'n dades d'altres comptes ni "
            "fer-lo servir per a res il·legal. Si passa, es pot tancar el compte.",
        ]),
        ("Canvis", [
            "Aquestes condicions poden canviar. Els canvis es publiquen aquí amb la "
            "seva data, i seguir fent servir l'app és acceptar-los.",
        ]),
    ],

    # --- Soporte ------------------------------------------------------------
    "soporte_titulo": "Suport",
    "soporte_entrada": "Alguna cosa no va, o se t'acut alguna cosa millor? Escriu i et "
                       "contestem.",
    "soporte_correo_titulo": "Escriu-nos",
    "soporte_correo_nota": "Contesta una persona. Si és un error, explica què feies, "
                           "què esperaves i què va passar, i digues quin iPhone i quina "
                           "versió d'iOS tens: així s'arregla abans.",
    "soporte_secciones": [
        ("Esborrar el teu compte", [
            "A l'app: Ajustos › Compte › Esborrar el compte. S'esborra tot el teu del "
            "servidor i es retira l'accés d'Apple. No cal escriure'ns.",
        ]),
        ("La subscripció", [
            "Pro es gestiona i es cancel·la des d'Ajustos del teu dispositiu › el teu "
            "nom › Subscripcions. Els reemborsaments els dona Apple des de "
            "reportaproblem.apple.com.",
        ]),
        ("El rellotge no veu els partits", [
            "El rellotge i l'iPhone es posen al dia quan són a prop i tots dos tenen "
            "l'app oberta. Si no, obre Rackers als dos i espera uns segons.",
            "El rellotge funciona sol: pots puntuar un partit sencer sense l'iPhone a "
            "sobre i ja es posaran d'acord després.",
        ]),
        ("Salut i permisos", [
            "Per mesurar el pols cal donar permís a Salut. Si el vas negar, es torna a "
            "donar a Ajustos › Salut › Accés a dades › Rackers.",
            "El pols es mesura amb un entrenament, així que el rellotge es queda a "
            "l'app mentre jugues.",
        ]),
        ("L'entrenador", [
            "L'anàlisi de vídeo és Pro i té un límit d'usos al dia i al mes. Si una "
            "anàlisi falla, no et compta.",
        ]),
    ],
}
