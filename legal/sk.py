"""Privacidad, Condiciones y Soporte en sk.

Lo que dice aquí tiene que casar con lo que hace el código: la copia de
seguridad sube partidos (con el pulso que midió el reloj), la salud de «Cómo
llegas hoy» no sale del iPhone y del vídeo del entrenador solo se guardan
unos segundos sin sonido de cada mejora, que se borran con su análisis.
Si eso cambia en la app o en el servidor, esto cambia también.
"""

TEXTO = {
    "legal_volver": "Späť na úvod",
    "legal_actualizado": "Aktualizované 8. októbra 2026",

    # --- Privacidad ---------------------------------------------------------
    "privacidad_titulo": "Súkromie",
    "privacidad_entrada": "Rackers vznikol na hranie, nie na zbieranie údajov. Tu je "
                          "jasne napísané, čo sa ukladá, kde a ako to zmazať.",
    "privacidad_secciones": [
        ("Bez účtu nič neodchádza z iPhonu", [
            "Rackers môžeš používať celý bez zakladania účtu. Zápasy, turnaje aj "
            "nastavenia ostávajú v tvojom zariadení a nikam necestujú.",
            "Účet slúži na tri veci: aby iPhone a hodinky mali to isté, aby si nič "
            "nestratil pri výmene mobilu a aby si mohol hrať s kamarátmi.",
        ]),
        ("Čo ukladá účet", [
            "Účet sa zakladá cez Prihlásenie s Apple. Apple nám dá stály identifikátor, "
            "tvoje meno a e-mail, ktorý bude súkromná preposielacia adresa od Apple, ak "
            "si zvolíš skryť ten svoj.",
            "Ukladáme ten identifikátor, e-mail, meno, ktoré ukazuješ, a @meno, ktoré "
            "si vyberieš. Aj povolenie od Apple, aby sa dal prístup odobrať, keď účet "
            "zmažeš.",
        ]),
        ("Záloha", [
            "So zapnutým účtom appka nahráva svoj obsah: hráčov, hracie dni, zápasy, "
            "turnaje, analýzy a nastavenia.",
            "Zápasy v sebe nesú to, čo hodinky namerali počas hry: pulz, vzdialenosť a "
            "energiu. Ide to so zápasom, lebo to k zápasu patrí.",
        ]),
        ("Čo neodchádza z tvojho iPhonu", [
            "Pokojový pulz, variabilita a spánok — to z «Ako si na tom dnes» — sa "
            "čítajú z appky Zdravie a ostávajú v zariadení. Nenahrávajú sa na server "
            "ani sa s nikým nezdieľajú.",
            "Povolenie pre Zdravie sa dá kedykoľvek odobrať v Nastavenia › Zdravie › "
            "Prístup k údajom, a appka funguje ďalej.",
        ]),
        ("Tréner s AI", [
            "Keď si vypýtaš analýzu, appka vyberie z videa jednotlivé snímky a pošle "
            "ich do OpenAI cez náš server, ktorý vráti správu.",
            "Z celého videa sa na serveri neukladá nič. Správa sa vráti do appky a ostane v tvojej kópii spolu s niekoľkými sekundami bez zvuku ku každému zlepšeniu, aby si ich videl aj na inom iPhone. Zmažú sa, keď zmažeš analýzu alebo účet.",
            "Ostáva však záznam, koľko analýz si si vypýtal, z akého športu a aké boli "
            "veľké. Slúži to na limity používania a na to, aby sme vedeli, koľko to "
            "stojí.",
        ]),
        ("Predplatné", [
            "Pro sa účtuje cez App Store. Tvoju kartu ani platobné údaje v žiadnom "
            "momente nevidíme a neukladáme.",
            "Používame RevenueCat, aby sme vedeli, či je tvoje predplatné platné — s "
            "identifikátorom tvojho účtu a ničím iným.",
        ]),
        ("Kamaráti a rodina", [
            "Ak sa s niekým prepojíš, uloží sa, že ste prepojení, a zápasy, ktoré "
            "zdieľate.",
            "Tvoje @meno je to, podľa čoho ťa ostatní nájdu. Môžeš ho kedykoľvek "
            "zmeniť.",
        ]),
        ("Turnaje", [
            "Keď zverejníš turnaj, uložíme jeho názov, šport, formát, dátum, kurt a meno organizátora. Pavúk a výsledky zostávajú v tvojom iPhone a v tvojej zálohe.",
            "Verejný turnaj uvidí ktokoľvek v Turnaje › Verejné a na jeho odkaze na rackers.app, aj bez účtu. K súkromnému sa dostane len ten, kto má kód alebo odkaz.",
            "Keď sa prihlásiš zo svojho účtu, organizátor uvidí meno, pod ktorým si sa prihlásil(a), a dostane upozornenie na iPhone. Odhlásiť sa môžeš kedykoľvek a zablokovaním niekoho sa prihlášky medzi vami zrušia.",
        ]),
        ("Kde sa to ukladá", [
            "V Cloudflare, v databáze D1. Server odpovedá len appke a ukladá to, čo mu "
            "appka pošle.",
            "Sekundy videa od trénera sú v Cloudflare R2. Databáza aj videá sú v Európskej únii.",
        ]),
        ("Ani reklamy, ani sledovanie", [
            "Žiadna reklama. Žiadne sledovanie medzi appkami ani webmi. Nič sa "
            "nepredáva ani neposkytuje tretím stranám na ich vlastné použitie.",
        ]),
        ("Ako to celé zmazať", [
            "Z appky: Nastavenia › Účet › Zmazať účet. Zmaže sa všetko tvoje zo servera "
            "a odoberie sa prístup, ktorý si dal cez Apple.",
            "To, čo je len v zariadení, zmizne, keď zmažeš appku.",
        ]),
        ("Maloletí", [
            "Rackers nie je určený deťom do 13 rokov a vedome od nich údaje nepýtame.",
        ]),
        ("Kto za to zodpovedá", [
            "Za spracovanie týchto údajov zodpovedá {responsable}, ktorý pracuje na "
            "seba a vydáva Rackers pod vlastným menom. V čomkoľvek, čo sa týka tvojich "
            "údajov, píš na {correo}.",
            "Máš právo vidieť svoje údaje, opraviť ich, zmazať, preniesť inam a "
            "namietať proti spracovaniu. Najrýchlejšie je zmazať účet z appky, ale ak "
            "to radšej chceš písomne, napíš a spraví sa.",
        ]),
        ("Zmeny", [
            "Ak sa toto zmení, oznámi sa to na tejto istej stránke s dátumom hore.",
        ]),
    ],

    # --- Condiciones --------------------------------------------------------
    "condiciones_titulo": "Podmienky používania",
    "condiciones_entrada": "Pravidlá používania Rackersu, nakrátko a bez drobného "
                           "písma.",
    "condiciones_secciones": [
        ("Čo to je", [
            "Rackers je tabuľa a zápisník zápasov pre padel, tenis, pickleball, squash, "
            "stolný tenis a bedminton, pre iPhone a Apple Watch.",
            "Používaním prijímaš tieto podmienky. Ak ich neprijímaš, nepoužívaj ju.",
        ]),
        ("Tvoj účet", [
            "Účet je tvoj a zodpovedáš za to, čo sa s ním robí. @meno nesmie nikoho "
            "predstierať ani byť urážlivé; ak je, môže sa odobrať.",
            'Urážky, obťažovanie ani urážlivý obsah sa netolerujú. V aplikácii môžeš zablokovať alebo nahlásiť akýkoľvek účet; nahlásenia do 24 hodín skontroluje človek a kto tieto pravidlá poruší, príde o účet.',
        ]),
        ("Pro a platby", [
            "Rackers je zadarmo. Pro je predplatné, ktoré sa účtuje z tvojho účtu v App "
            "Store po potvrdení nákupu.",
            "Obnovuje sa samo, ak ho nezrušíš aspoň 24 hodín pred koncom obdobia. "
            "Spravuje sa a ruší v Nastaveniach tvojho zariadenia › tvoje meno › "
            "Predplatné.",
            "Vrátenie peňazí dáva Apple, nie my, podľa vlastných pravidiel.",
        ]),
        ("Rodinný plán", [
            "Rodinný plán dáva Pro tomu, kto ho platí, a účtom, ktoré pozve, až do "
            "limitu, ktorý uvádza appka. Kto platí, môže kohokoľvek kedykoľvek odobrať.",
        ]),
        ("Tréner nie je lekár", [
            "Správa trénera a to, čo appka vypočíta z tvojich údajov zo Zdravia, sú "
            "orientačné. Nie sú to diagnóza, liečba ani odborná lekárska či športová "
            "rada.",
            "Ak sa necítiš dobre alebo máš pochybnosti o zdraví, opýtaj sa odborníka.",
        ]),
        ("Služba", [
            "Robíme, čo sa dá, aby všetko fungovalo, ale appka a server sa poskytujú "
            "tak, ako sú, bez záruky, že budú dostupné bez prerušenia alebo že v nich "
            "nebudú chyby.",
            "Ulož si, na čom ti záleží: záloha pomáha, ale nenahrádza tvoje vlastné "
            "kópie.",
        ]),
        ("Správne používanie", [
            "Nesmie sa skúšať rozbiť službu, ťahať z nej údaje iných účtov ani "
            "používať ju na nič nezákonné. Ak sa to stane, účet sa môže zrušiť.",
        ]),
        ("Zmeny", [
            "Tieto podmienky sa môžu zmeniť. Zmeny sa zverejňujú tu s dátumom a ďalšie "
            "používanie appky znamená ich prijatie.",
        ]),
    ],

    # --- Soporte ------------------------------------------------------------
    "soporte_titulo": "Podpora",
    "soporte_entrada": "Niečo nefunguje alebo ťa napadlo niečo lepšie? Napíš a "
                       "odpovieme.",
    "soporte_correo_titulo": "Napíš nám",
    "soporte_correo_nota": "Odpovedá človek. Ak ide o chybu, napíš, čo si robil, čo si "
                           "čakal a čo sa stalo, a uveď, aký iPhone a akú verziu iOS "
                           "máš: tak sa to opraví skôr.",
    "soporte_secciones": [
        ("Zmazať účet", [
            "V appke: Nastavenia › Účet › Zmazať účet. Zmaže sa všetko tvoje zo servera "
            "a odoberie sa prístup od Apple. Nemusíš nám písať.",
        ]),
        ("Predplatné", [
            "Pro sa spravuje a ruší v Nastaveniach tvojho zariadenia › tvoje meno › "
            "Predplatné. Vrátenie peňazí dáva Apple cez reportaproblem.apple.com.",
        ]),
        ("Hodinky nevidia zápasy", [
            "Hodinky a iPhone sa zladia, keď sú blízko a na oboch je otvorená appka. Ak "
            "nie, otvor Rackers na oboch a počkaj pár sekúnd.",
            "Hodinky fungujú samé: celý zápas môžeš odzapisovať bez iPhonu pri sebe a "
            "dohodnú sa až potom.",
        ]),
        ("Zdravie a povolenia", [
            "Na meranie pulzu treba dať povolenie Zdraviu. Ak si ho odmietol, dá sa "
            "znova v Nastavenia › Zdravie › Prístup k údajom › Rackers.",
            "Pulz sa meria ako tréning, takže hodinky ostanú v appke, kým hráš.",
        ]),
        ("Tréner", [
            "Analýza videa je Pro a má limit použití na deň a na mesiac. Ak analýza "
            "zlyhá, nepočíta sa ti.",
        ]),
    ],
}
