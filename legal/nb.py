"""Privacidad, Condiciones y Soporte en nb.

Lo que dice aquí tiene que casar con lo que hace el código: la copia de
seguridad sube partidos (con el pulso que midió el reloj), la salud de «Cómo
llegas hoy» no sale del iPhone y del vídeo del entrenador solo se guardan
unos segundos sin sonido de cada mejora, que se borran con su análisis.
Si eso cambia en la app o en el servidor, esto cambia también.
"""

TEXTO = {
    "legal_volver": "Tilbake til forsiden",
    "legal_actualizado": "Oppdatert 8. oktober 2026",

    # --- Privacidad ---------------------------------------------------------
    "privacidad_titulo": "Personvern",
    "privacidad_entrada": "Rackers ble laget for å spille, ikke for å samle data. Her "
                          "står det klart hva som lagres, hvor, og hvordan du sletter "
                          "det.",
    "privacidad_secciones": [
        ("Uten konto forlater ingenting iPhonen din", [
            "Du kan bruke hele Rackers uten å opprette konto. Kampene, turneringene og "
            "innstillingene blir på enheten din og reiser ingen steder.",
            "Kontoen er til tre ting: at iPhone og klokke har det samme, at du ikke "
            "mister noe når du bytter mobil, og at du kan spille med venner.",
        ]),
        ("Hva kontoen lagrer", [
            "Kontoen opprettes med Logg på med Apple. Apple gir oss en fast ID, navnet "
            "ditt og en e-post — Apples private videresendingsadresse hvis du velger å "
            "skjule din egen.",
            "Vi lagrer den ID-en, e-posten, navnet du viser og @navnet du velger. Og "
            "tillatelsen Apple gir, så tilgangen kan trekkes tilbake når du sletter "
            "kontoen.",
        ]),
        ("Sikkerhetskopien", [
            "Med konto på laster appen opp innholdet sitt: spillere, spilledager, "
            "kamper, turneringer, analyser og innstillinger.",
            "Kampene har med det klokka målte mens du spilte: puls, distanse og energi. "
            "Det følger kampen fordi det hører til kampen.",
        ]),
        ("Det som ikke forlater iPhonen din", [
            "Hvilepuls, variabilitet og søvn — det til «Hvordan du ligger an i dag» — "
            "leses fra Helse-appen og blir på enheten. De lastes ikke opp til serveren "
            "og deles ikke med noen.",
            "Tillatelsen til Helse kan trekkes tilbake når som helst under "
            "Innstillinger › Helse › Datatilgang, uten at appen slutter å virke.",
        ]),
        ("KI-treneren", [
            "Når du ber om en analyse, henter appen enkeltbilder fra videoen og sender "
            "dem til OpenAI via serveren vår, som sender rapporten tilbake.",
            "Ingenting av hele videoen lagres på serveren. Rapporten kommer tilbake til appen og blir i kopien din, sammen med noen sekunder uten lyd fra hver forbedring, så du kan se dem på en annen iPhone også. De slettes når du sletter analysen eller kontoen.",
            "Derimot lagres det hvor mange analyser du har bedt om, i hvilken idrett og "
            "hvor store de var. Det brukes til bruksgrensene og til å vite hva det "
            "koster.",
        ]),
        ("Abonnementet", [
            "Pro betales via App Store. Vi ser eller lagrer aldri kortet ditt eller "
            "betalingsopplysningene dine.",
            "Vi bruker RevenueCat for å vite om abonnementet ditt er aktivt, med ID-en "
            "til kontoen din og ingenting annet.",
        ]),
        ("Venner og familie", [
            "Hvis du kobler deg til noen, lagres det at dere er koblet og kampene dere "
            "deler.",
            "@navnet ditt er slik andre finner deg. Du kan endre det når du vil.",
        ]),
        ("Turneringer", [
            "Hvis du publiserer en turnering, lagrer vi navnet, idretten, formatet, datoen, banen og navnet til arrangøren. Oppsettet og resultatene blir værende på iPhonen din og i sikkerhetskopien din.",
            "En offentlig turnering kan alle se under Turneringer › Offentlige og via lenken på rackers.app, også uten konto. En privat når bare de som har koden eller lenken.",
            "Hvis du melder deg på med kontoen din, ser arrangøren navnet du meldte deg på med, og får et varsel på iPhonen sin. Du kan melde deg av når du vil, og hvis du blokkerer noen, fjernes påmeldingene mellom dere.",
        ]),
        ("Hvor det lagres", [
            "Hos Cloudflare, i en D1-database. Serveren svarer bare appen og lagrer det "
            "appen sender den.",
            "Trenerens videosekunder ligger i Cloudflare R2. Både databasen og videoene er i EU.",
        ]),
        ("Verken reklame eller sporing", [
            "Det er ingen reklame. Ingen sporing på tvers av apper eller nettsteder. "
            "Ingenting selges eller gis videre til tredjeparter for deres eget bruk.",
        ]),
        ("Slik sletter du alt", [
            "Fra appen: Innstillinger › Konto › Slett konto. Alt ditt slettes fra "
            "serveren, og tilgangen du ga med Apple trekkes tilbake.",
            "Det som bare ligger på enheten forsvinner når du sletter appen.",
        ]),
        ("Mindreårige", [
            "Rackers er ikke laget for barn under 13 år, og vi ber dem ikke bevisst om "
            "opplysninger.",
        ]),
        ("Hvem som har ansvaret", [
            "Behandlingen av disse dataene er {responsable} ansvarlig for, som jobber "
            "for seg selv og gir ut Rackers i eget navn. Skriv til {correo} om alt som "
            "har med dataene dine å gjøre.",
            "Du har rett til å se dine data, rette dem, slette dem, ta dem med et annet "
            "sted og motsette deg behandlingen. Raskest er å slette kontoen fra appen, "
            "men foretrekker du å be skriftlig, så skriv, og det blir gjort.",
        ]),
        ("Endringer", [
            "Endrer dette seg, står det på denne siden med datoen øverst.",
        ]),
    ],

    # --- Condiciones --------------------------------------------------------
    "condiciones_titulo": "Vilkår for bruk",
    "condiciones_entrada": "Reglene for å bruke Rackers, kort og uten liten skrift.",
    "condiciones_secciones": [
        ("Hva dette er", [
            "Rackers er en resultattavle og en kampbok for padel, tennis, pickleball, "
            "squash, bordtennis og badminton, til iPhone og Apple Watch.",
            "Ved å bruke den godtar du disse vilkårene. Godtar du dem ikke, så la være "
            "å bruke den.",
        ]),
        ("Kontoen din", [
            "Kontoen er din, og du svarer for hva som gjøres med den. @navnet kan ikke "
            "utgi seg for noen eller være støtende; er det det, kan det trekkes "
            "tilbake.",
            'Fornærmelser, trakassering og krenkende innhold tolereres ikke. I appen kan du blokkere eller rapportere hvilken som helst konto; et menneske går gjennom rapporter innen 24 timer, og den som bryter reglene, mister kontoen sin.',
        ]),
        ("Pro og betalingene", [
            "Rackers er gratis. Pro er et abonnement som trekkes fra App Store-kontoen "
            "din når du bekrefter kjøpet.",
            "Det fornyes av seg selv med mindre du sier det opp minst 24 timer før "
            "perioden er ute. Det styres og sies opp under Innstillinger på enheten din "
            "› navnet ditt › Abonnementer.",
            "Refusjoner gis av Apple, ikke av oss, etter Apples egne regler.",
        ]),
        ("Familieabonnementet", [
            "Familieabonnementet gir Pro til den som betaler og til kontoene "
            "vedkommende inviterer, opp til grensen appen oppgir. Den som betaler kan "
            "fjerne hvem som helst når som helst.",
        ]),
        ("Treneren er ikke lege", [
            "Trenerens rapport og det appen regner ut fra helsedataene dine er "
            "veiledende. Det er verken diagnose, behandling eller profesjonelle "
            "medisinske eller idrettslige råd.",
            "Føler du deg dårlig eller er i tvil om helsa, spør en fagperson.",
        ]),
        ("Tjenesten", [
            "Vi gjør vårt beste for at alt skal virke, men appen og serveren leveres "
            "som de er, uten garanti for at de er tilgjengelige uten avbrudd eller at "
            "det ikke er feil.",
            "Ta vare på det som betyr noe for deg: sikkerhetskopien hjelper, men "
            "erstatter ikke dine egne kopier.",
        ]),
        ("Riktig bruk", [
            "Man kan ikke prøve å bryte tjenesten, hente ut data fra andre kontoer "
            "eller bruke den til noe ulovlig. Skjer det, kan kontoen stenges.",
        ]),
        ("Endringer", [
            "Disse vilkårene kan endre seg. Endringene publiseres her med dato, og å "
            "fortsette å bruke appen er å godta dem.",
        ]),
    ],

    # --- Soporte ------------------------------------------------------------
    "soporte_titulo": "Brukerstøtte",
    "soporte_entrada": "Er det noe som ikke virker, eller har du en bedre idé? Skriv, så "
                       "svarer vi.",
    "soporte_correo_titulo": "Skriv til oss",
    "soporte_correo_nota": "Det er et menneske som svarer. Er det en feil, fortell hva "
                           "du gjorde, hva du ventet og hva som skjedde, og si hvilken "
                           "iPhone og hvilken iOS-versjon du har: da blir det rettet "
                           "raskere.",
    "soporte_secciones": [
        ("Slette kontoen din", [
            "I appen: Innstillinger › Konto › Slett konto. Alt ditt slettes fra "
            "serveren, og Apple-tilgangen trekkes tilbake. Du trenger ikke skrive til "
            "oss.",
        ]),
        ("Abonnementet", [
            "Pro styres og sies opp under Innstillinger på enheten din › navnet ditt › "
            "Abonnementer. Refusjoner gir Apple via reportaproblem.apple.com.",
        ]),
        ("Klokka ser ikke kampene", [
            "Klokka og iPhonen oppdaterer hverandre når de er nær og begge har appen "
            "åpen. Hvis ikke, åpne Rackers på begge og vent noen sekunder.",
            "Klokka klarer seg selv: du kan telle poeng i en hel kamp uten iPhonen på "
            "deg, så blir de enige etterpå.",
        ]),
        ("Helse og tillatelser", [
            "For å måle pulsen må du gi Helse tillatelse. Sa du nei, gir du den på nytt "
            "under Innstillinger › Helse › Datatilgang › Rackers.",
            "Pulsen måles som en økt, så klokka blir i appen mens du spiller.",
        ]),
        ("Treneren", [
            "Videoanalysen er Pro og har en grense for bruk per dag og per måned. "
            "Mislykkes en analyse, teller den ikke.",
        ]),
    ],
}
