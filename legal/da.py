"""Privacidad, Condiciones y Soporte en da.

Lo que dice aquí tiene que casar con lo que hace el código: la copia de
seguridad sube partidos (con el pulso que midió el reloj), la salud de «Cómo
llegas hoy» no sale del iPhone y del vídeo del entrenador no se guarda nada.
Si eso cambia en la app o en el servidor, esto cambia también.
"""

TEXTO = {
    "legal_volver": "Tilbage til forsiden",
    "legal_actualizado": "Opdateret 25. september 2026",

    # --- Privacidad ---------------------------------------------------------
    "privacidad_titulo": "Privatliv",
    "privacidad_entrada": "Rackers blev lavet til at spille, ikke til at samle data. Her "
                          "står klart, hvad der gemmes, hvor, og hvordan du sletter det.",
    "privacidad_secciones": [
        ("Uden konto forlader intet din iPhone", [
            "Du kan bruge hele Rackers uden at oprette en konto. Kampe, turneringer og "
            "indstillinger bliver på din enhed og rejser ingen steder hen.",
            "Kontoen er til tre ting: at iPhone og ur har det samme, at du ikke mister "
            "noget, når du skifter telefon, og at du kan spille med venner.",
        ]),
        ("Hvad kontoen gemmer", [
            "Kontoen oprettes med Log ind med Apple. Apple giver os et fast id, dit "
            "navn og en e-mail — Apples private videresendelsesadresse, hvis du vælger "
            "at skjule din egen.",
            "Vi gemmer det id, e-mailen, det navn du viser, og det @navn du vælger. Og "
            "den tilladelse, Apple giver, så adgangen kan trækkes tilbage, når du "
            "sletter kontoen.",
        ]),
        ("Sikkerhedskopien", [
            "Med kontoen slået til uploader appen sit indhold: spillere, spilledage, "
            "kampe, turneringer, analyser og indstillinger.",
            "Kampene har det med, uret målte, mens du spillede: puls, distance og "
            "energi. Det følger kampen, fordi det hører til kampen.",
        ]),
        ("Det der ikke forlader din iPhone", [
            "Hvilepuls, variabilitet og søvn — det til «Sådan har du det i dag» — "
            "læses fra Sundhed-appen og bliver på enheden. De uploades ikke til "
            "serveren og deles ikke med nogen.",
            "Tilladelsen til Sundhed kan trækkes tilbage når som helst under "
            "Indstillinger › Sundhed › Dataadgang, uden at appen holder op med at virke.",
        ]),
        ("AI-træneren", [
            "Når du beder om en analyse, trækker appen enkeltbilleder ud af videoen og "
            "sender dem til OpenAI gennem vores server, som sender rapporten tilbage.",
            "Der gemmes intet af videoen på serveren. Rapporten kommer tilbage til "
            "appen og bliver i din kopi.",
            "Der gemmes til gengæld, hvor mange analyser du har bedt om, i hvilken "
            "sportsgren og hvor store de var. Det bruges til brugsgrænserne og til at "
            "vide, hvad det koster.",
        ]),
        ("Abonnementet", [
            "Pro betales via App Store. Vi ser eller gemmer på intet tidspunkt dit "
            "kort eller dine betalingsoplysninger.",
            "Vi bruger RevenueCat til at vide, om dit abonnement er aktivt, med id'et "
            "på din konto og intet andet.",
        ]),
        ("Venner og familie", [
            "Hvis du forbinder dig med nogen, gemmes det, at I er forbundet, og de "
            "kampe I deler.",
            "Dit @navn er sådan, andre finder dig. Du kan ændre det når som helst.",
        ]),
        ("Hvor det gemmes", [
            "Hos Cloudflare, i en D1-database. Serveren svarer kun appen og gemmer det, "
            "appen sender den.",
        ]),
        ("Hverken reklamer eller sporing", [
            "Der er ingen reklamer. Ingen sporing på tværs af apps eller websteder. "
            "Intet sælges eller videregives til tredjeparter til deres eget brug.",
        ]),
        ("Sådan sletter du det hele", [
            "Fra appen: Indstillinger › Konto › Slet konto. Alt dit slettes fra "
            "serveren, og den adgang, du gav med Apple, trækkes tilbage.",
            "Det, der kun ligger på enheden, forsvinder, når du sletter appen.",
        ]),
        ("Mindreårige", [
            "Rackers er ikke tænkt til børn under 13 år, og vi beder dem ikke bevidst "
            "om oplysninger.",
        ]),
        ("Hvem der står for det", [
            "Behandlingen af disse data står {responsable} for, som arbejder "
            "selvstændigt og udgiver Rackers i eget navn. Skriv til {correo} om alt, "
            "der har med dine data at gøre.",
            "Du har ret til at se dine data, rette dem, slette dem, tage dem med et "
            "andet sted hen og gøre indsigelse mod behandlingen. Hurtigst er at slette "
            "kontoen fra appen, men foretrækker du at bede skriftligt, så skriv, og det "
            "bliver gjort.",
        ]),
        ("Ændringer", [
            "Ændrer det sig, står det på netop denne side med datoen øverst.",
        ]),
    ],

    # --- Condiciones --------------------------------------------------------
    "condiciones_titulo": "Betingelser",
    "condiciones_entrada": "Reglerne for at bruge Rackers, kort og uden småt med.",
    "condiciones_secciones": [
        ("Hvad det her er", [
            "Rackers er en scoretavle og en kampbog til padel, tennis, pickleball, "
            "squash, bordtennis og badminton, til iPhone og Apple Watch.",
            "Ved at bruge den accepterer du disse betingelser. Accepterer du dem ikke, "
            "så lad være med at bruge den.",
        ]),
        ("Din konto", [
            "Kontoen er din, og du svarer for, hvad der sker med den. @navnet må ikke "
            "udgive sig for nogen eller være stødende; er det det, kan det trækkes "
            "tilbage.",
            'Fornærmelser, chikane og krænkende indhold tolereres ikke. I appen kan du blokere eller anmelde enhver konto; et menneske gennemgår anmeldelser inden for 24 timer, og den, der bryder reglerne, mister sin konto.',
        ]),
        ("Pro og betalingerne", [
            "Rackers er gratis. Pro er et abonnement, der trækkes på din App "
            "Store-konto, når du bekræfter købet.",
            "Det fornyes af sig selv, medmindre du opsiger det mindst 24 timer før "
            "perioden slutter. Det styres og opsiges under Indstillinger på din enhed › "
            "dit navn › Abonnementer.",
            "Refusioner gives af Apple, ikke af os, efter Apples egne regler.",
        ]),
        ("Familieabonnementet", [
            "Familieabonnementet giver Pro til den, der betaler, og til de konti, "
            "vedkommende inviterer, op til den grænse appen angiver. Den, der betaler, "
            "kan fjerne hvem som helst når som helst.",
        ]),
        ("Træneren er ikke en læge", [
            "Trænerens rapport og det, appen regner ud af dine sundhedsdata, er "
            "vejledende. Det er hverken diagnose, behandling eller professionel "
            "lægelig eller sportslig rådgivning.",
            "Har du det dårligt eller er i tvivl om dit helbred, så spørg en "
            "fagperson.",
        ]),
        ("Tjenesten", [
            "Vi gør, hvad vi kan, for at alt virker, men appen og serveren leveres, som "
            "de er, uden garanti for, at de er tilgængelige uden afbrydelser, eller at "
            "der ikke er fejl.",
            "Gem det, der betyder noget for dig: sikkerhedskopien hjælper, men "
            "erstatter ikke dine egne kopier.",
        ]),
        ("Ordentlig brug", [
            "Man må ikke forsøge at bryde tjenesten, hente data fra andres konti eller "
            "bruge den til noget ulovligt. Sker det, kan kontoen lukkes.",
        ]),
        ("Ændringer", [
            "Disse betingelser kan ændre sig. Ændringerne offentliggøres her med deres "
            "dato, og bliver du ved med at bruge appen, accepterer du dem.",
        ]),
    ],

    # --- Soporte ------------------------------------------------------------
    "soporte_titulo": "Support",
    "soporte_entrada": "Er der noget, der ikke virker, eller har du en bedre idé? Skriv, "
                       "så svarer vi.",
    "soporte_correo_titulo": "Skriv til os",
    "soporte_correo_nota": "Der svarer et menneske. Er det en fejl, så fortæl, hvad du "
                           "gjorde, hvad du forventede, og hvad der skete, og skriv "
                           "hvilken iPhone og hvilken iOS-version du har: så bliver det "
                           "rettet hurtigere.",
    "soporte_secciones": [
        ("Slet din konto", [
            "I appen: Indstillinger › Konto › Slet konto. Alt dit slettes fra serveren, "
            "og Apple-adgangen trækkes tilbage. Du behøver ikke skrive til os.",
        ]),
        ("Abonnementet", [
            "Pro styres og opsiges under Indstillinger på din enhed › dit navn › "
            "Abonnementer. Refusioner giver Apple via reportaproblem.apple.com.",
        ]),
        ("Uret kan ikke se kampene", [
            "Uret og iPhone opdaterer hinanden, når de er tæt på og begge har appen "
            "åben. Ellers åbn Rackers på begge og vent et par sekunder.",
            "Uret klarer sig selv: du kan tælle point i en hel kamp uden iPhone på dig, "
            "så finder de ud af det bagefter.",
        ]),
        ("Sundhed og tilladelser", [
            "For at måle puls skal du give Sundhed tilladelse. Sagde du nej, giver du "
            "den igen under Indstillinger › Sundhed › Dataadgang › Rackers.",
            "Pulsen måles som en træning, så uret bliver i appen, mens du spiller.",
        ]),
        ("Træneren", [
            "Videoanalysen er Pro og har en grænse for brug om dagen og om måneden. "
            "Mislykkes en analyse, tæller den ikke med.",
        ]),
    ],
}
