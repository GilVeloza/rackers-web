"""Privacidad, Condiciones y Soporte en sl.

Lo que dice aquí tiene que casar con lo que hace el código: la copia de
seguridad sube partidos (con el pulso que midió el reloj), la salud de «Cómo
llegas hoy» no sale del iPhone y del vídeo del entrenador no se guarda nada.
Si eso cambia en la app o en el servidor, esto cambia también.
"""

TEXTO = {
    "legal_volver": "Nazaj na naslovnico",
    "legal_actualizado": "Posodobljeno 25. septembra 2026",

    # --- Privacidad ---------------------------------------------------------
    "privacidad_titulo": "Zasebnost",
    "privacidad_entrada": "Rackers je nastal za igro, ne za zbiranje podatkov. Tu je "
                          "jasno zapisano, kaj se shrani, kje in kako to izbrisati.",
    "privacidad_secciones": [
        ("Brez računa nič ne gre iz iPhona", [
            "Rackers lahko uporabljaš v celoti brez računa. Tekme, turnirji in "
            "nastavitve ostanejo na tvoji napravi in ne potujejo nikamor.",
            "Račun je za tri stvari: da imata iPhone in ura isto, da ob menjavi telefona "
            "ničesar ne izgubiš in da lahko igraš s prijatelji.",
        ]),
        ("Kaj shrani račun", [
            "Račun se ustvari s Prijavo z Applom. Apple nam da stalen identifikator, "
            "tvoje ime in e-pošto, ki bo Applov zasebni posredovalni naslov, če se "
            "odločiš svojega skriti.",
            "Shranimo ta identifikator, e-pošto, ime, ki ga kažeš, in @ime, ki ga "
            "izbereš. Pa tudi dovoljenje, ki ga da Apple, da se dostop lahko odvzame, "
            "ko izbrišeš račun.",
        ]),
        ("Varnostna kopija", [
            "Z vklopljenim računom aplikacija naloži svojo vsebino: igralce, igralne "
            "dneve, tekme, turnirje, analize in nastavitve.",
            "Tekme nosijo v sebi to, kar je ura izmerila med igro: utrip, razdaljo in "
            "energijo. Gre s tekmo, ker k tekmi sodi.",
        ]),
        ("Kar ne gre iz tvojega iPhona", [
            "Utrip v mirovanju, variabilnost in spanje — tisto iz «Kako si danes» — se "
            "bereta iz aplikacije Zdravje in ostaneta na napravi. Ne naložita se na "
            "strežnik in se z nikomer ne delita.",
            "Dovoljenje za Zdravje lahko kadar koli odvzameš v Nastavitve › Zdravje › "
            "Dostop do podatkov, aplikacija pa še naprej deluje.",
        ]),
        ("Trener z UI", [
            "Ko zaprosiš za analizo, aplikacija iz videa izlušči posamezne sličice in "
            "jih prek našega strežnika pošlje OpenAI, ki vrne poročilo.",
            "Od videa se na strežniku ne shrani nič. Poročilo se vrne v aplikacijo in "
            "ostane v tvoji kopiji.",
            "Ostane pa zapis, koliko analiz si zahteval, iz katerega športa in kako "
            "velike so bile. To služi omejitvam uporabe in temu, da vemo, koliko stane.",
        ]),
        ("Naročnina", [
            "Pro se zaračuna prek App Storea. Tvoje kartice ali podatkov o plačilu v "
            "nobenem trenutku ne vidimo in ne shranjujemo.",
            "Uporabljamo RevenueCat, da vemo, ali je tvoja naročnina veljavna — z "
            "identifikatorjem tvojega računa in ničimer drugim.",
        ]),
        ("Prijatelji in družina", [
            "Če se s kom povežeš, se shrani, da sta povezana, in tekme, ki jih delita.",
            "Tvoje @ime je tisto, po čemer te drugi najdejo. Lahko ga kadar koli "
            "spremeniš.",
        ]),
        ("Kje se shranjuje", [
            "Pri Cloudflareu, v zbirki podatkov D1. Strežnik odgovarja samo aplikaciji "
            "in shrani tisto, kar mu aplikacija pošlje.",
        ]),
        ("Ne oglasov ne sledenja", [
            "Oglasov ni. Ni sledenja med aplikacijami ali spletnimi stranmi. Nič se ne "
            "prodaja in ne izroča tretjim za njihovo lastno uporabo.",
        ]),
        ("Kako vse izbrisati", [
            "V aplikaciji: Nastavitve › Račun › Izbriši račun. Izbriše se vse tvoje s "
            "strežnika in odvzame se dostop, ki si ga dal z Applom.",
            "Kar je samo na napravi, izgine, ko izbrišeš aplikacijo.",
        ]),
        ("Mladoletni", [
            "Rackers ni namenjen otrokom, mlajšim od 13 let, in od njih zavestno ne "
            "zbiramo podatkov.",
        ]),
        ("Kdo za to odgovarja", [
            "Za obdelavo teh podatkov odgovarja {responsable}, ki dela samostojno in "
            "izdaja Rackers pod svojim imenom. Za vse v zvezi s tvojimi podatki piši na "
            "{correo}.",
            "Imaš pravico videti svoje podatke, jih popraviti, izbrisati, prenesti "
            "drugam in nasprotovati obdelavi. Najhitreje je izbrisati račun iz "
            "aplikacije, če pa raje zaprosiš pisno, piši in se bo uredilo.",
        ]),
        ("Spremembe", [
            "Če se to spremeni, bo to zapisano na tej isti strani z datumom na vrhu.",
        ]),
    ],

    # --- Condiciones --------------------------------------------------------
    "condiciones_titulo": "Pogoji uporabe",
    "condiciones_entrada": "Pravila uporabe Rackersa, na kratko in brez drobnega tiska.",
    "condiciones_secciones": [
        ("Kaj je to", [
            "Rackers je semafor in zvezek tekem za padel, tenis, pickleball, squash, "
            "namizni tenis in badminton, za iPhone in Apple Watch.",
            "Z uporabo sprejemaš te pogoje. Če jih ne sprejemaš, je ne uporabljaj.",
        ]),
        ("Tvoj račun", [
            "Račun je tvoj in odgovarjaš za to, kar se z njim počne. @ime ne sme "
            "lažno predstavljati nikogar niti biti žaljivo; če je, se lahko odvzame.",
            'Žaljivk, nadlegovanja in žaljive vsebine ne toleriramo. V aplikaciji lahko blokiraš ali prijaviš kateri koli račun; prijave v 24 urah pregleda človek, kdor krši ta pravila, pa izgubi račun.',
        ]),
        ("Pro in plačila", [
            "Rackers je brezplačen. Pro je naročnina, ki se zaračuna prek tvojega "
            "računa v App Storeu, ko potrdiš nakup.",
            "Sama se obnavlja, razen če jo prekličeš vsaj 24 ur pred koncem obdobja. "
            "Upravlja in preklicuje se v Nastavitvah tvoje naprave › tvoje ime › "
            "Naročnine.",
            "Vračila daje Apple, ne mi, po svojih pravilih.",
        ]),
        ("Družinski paket", [
            "Družinski paket da Pro tistemu, ki ga plača, in računom, ki jih povabi, do "
            "meje, ki jo navaja aplikacija. Kdor plača, lahko kogar koli kadar koli "
            "odstrani.",
        ]),
        ("Trener ni zdravnik", [
            "Trenerjevo poročilo in to, kar aplikacija izračuna iz tvojih podatkov iz "
            "Zdravja, sta informativna. Nista diagnoza, zdravljenje ne strokovni "
            "zdravstveni ali športni nasvet.",
            "Če se slabo počutiš ali imaš dvome o zdravju, vprašaj strokovnjaka.",
        ]),
        ("Storitev", [
            "Trudimo se, da vse deluje, a aplikacija in strežnik sta na voljo taka, "
            "kot sta, brez jamstva, da bosta dosegljiva brez prekinitev ali da ne bo "
            "napak.",
            "Shrani, kar ti je pomembno: varnostna kopija pomaga, a ne nadomesti tvojih "
            "lastnih kopij.",
        ]),
        ("Pravilna uporaba", [
            "Ni dovoljeno poskušati zlomiti storitve, iz nje jemati podatkov drugih "
            "računov ali jo uporabljati za kaj nezakonitega. Če se to zgodi, se račun "
            "lahko zapre.",
        ]),
        ("Spremembe", [
            "Ti pogoji se lahko spremenijo. Spremembe se objavijo tu z datumom, "
            "nadaljnja uporaba aplikacije pa pomeni, da jih sprejemaš.",
        ]),
    ],

    # --- Soporte ------------------------------------------------------------
    "soporte_titulo": "Podpora",
    "soporte_entrada": "Kaj ne deluje ali imaš boljšo idejo? Piši in odgovorili ti bomo.",
    "soporte_correo_titulo": "Piši nam",
    "soporte_correo_nota": "Odgovarja človek. Če gre za napako, povej, kaj si počel, kaj "
                           "si pričakoval in kaj se je zgodilo, in napiši, kateri iPhone "
                           "in katero različico iOS imaš: tako se prej popravi.",
    "soporte_secciones": [
        ("Izbris računa", [
            "V aplikaciji: Nastavitve › Račun › Izbriši račun. Izbriše se vse tvoje s "
            "strežnika in odvzame se Applov dostop. Ni nam treba pisati.",
        ]),
        ("Naročnina", [
            "Pro se upravlja in preklicuje v Nastavitvah tvoje naprave › tvoje ime › "
            "Naročnine. Vračila daje Apple prek reportaproblem.apple.com.",
        ]),
        ("Ura ne vidi tekem", [
            "Ura in iPhone se uskladita, ko sta blizu in je na obeh odprta aplikacija. "
            "Če ne, odpri Rackers na obeh in počakaj nekaj sekund.",
            "Ura deluje sama: celo tekmo lahko odigraš brez iPhona pri sebi, uskladila "
            "se bosta pozneje.",
        ]),
        ("Zdravje in dovoljenja", [
            "Za merjenje utripa je treba dati dovoljenje Zdravju. Če si ga zavrnil, ga "
            "znova daš v Nastavitve › Zdravje › Dostop do podatkov › Rackers.",
            "Utrip se meri kot vadba, zato ura ostane v aplikaciji, medtem ko igraš.",
        ]),
        ("Trener", [
            "Analiza videa je Pro in ima omejitev uporabe na dan in na mesec. Če "
            "analiza spodleti, se ti ne šteje.",
        ]),
    ],
}
