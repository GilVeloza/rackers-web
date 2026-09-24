"""Privacidad, Condiciones y Soporte en hr.

Lo que dice aquí tiene que casar con lo que hace el código: la copia de
seguridad sube partidos (con el pulso que midió el reloj), la salud de «Cómo
llegas hoy» no sale del iPhone y del vídeo del entrenador no se guarda nada.
Si eso cambia en la app o en el servidor, esto cambia también.
"""

TEXTO = {
    "legal_volver": "Natrag na naslovnicu",
    "legal_actualizado": "Ažurirano 24. rujna 2026.",

    # --- Privacidad ---------------------------------------------------------
    "privacidad_titulo": "Privatnost",
    "privacidad_entrada": "Rackers je napravljen za igru, ne za skupljanje podataka. "
                          "Ovdje jasno piše što se sprema, gdje i kako to obrisati.",
    "privacidad_secciones": [
        ("Bez računa ništa ne izlazi iz iPhonea", [
            "Rackers možeš koristiti u cijelosti bez otvaranja računa. Mečevi, turniri i "
            "postavke ostaju na tvom uređaju i ne putuju nikamo.",
            "Račun služi za tri stvari: da iPhone i sat imaju isto, da ništa ne izgubiš "
            "kad promijeniš mobitel i da možeš igrati s prijateljima.",
        ]),
        ("Što račun sprema", [
            "Račun se otvara s Prijavom putem Applea. Apple nam daje stalni "
            "identifikator, tvoje ime i e-poštu, koja će biti Appleova privatna adresa "
            "za preusmjeravanje ako odlučiš sakriti svoju.",
            "Spremamo taj identifikator, e-poštu, ime koje prikazuješ i @ime koje "
            "odabereš. I dopuštenje koje Apple daje kako bi se pristup mogao povući kad "
            "obrišeš račun.",
        ]),
        ("Sigurnosna kopija", [
            "S uključenim računom aplikacija šalje svoj sadržaj: igrače, dane igranja, "
            "mečeve, turnire, analize i postavke.",
            "Mečevi nose u sebi ono što je sat izmjerio dok si igrao: puls, udaljenost "
            "i energiju. Ide uz meč jer pripada meču.",
        ]),
        ("Ono što ne izlazi iz tvog iPhonea", [
            "Puls u mirovanju, varijabilnost i san — ono iz «Kako si danas» — čitaju se "
            "iz aplikacije Zdravlje i ostaju na uređaju. Ne šalju se na poslužitelj "
            "niti se dijele s ikim.",
            "Dopuštenje za Zdravlje možeš povući kad god hoćeš u Postavke › Zdravlje › "
            "Pristup podacima, a aplikacija i dalje radi.",
        ]),
        ("AI trener", [
            "Kad zatražiš analizu, aplikacija izvuče pojedinačne sličice iz videa i "
            "pošalje ih OpenAI-ju preko našeg poslužitelja, koji vraća izvještaj.",
            "Od videa se ništa ne sprema na poslužitelju. Izvještaj se vraća u "
            "aplikaciju i ostaje u tvojoj kopiji.",
            "Ostaje zapis koliko si analiza zatražio, iz kojeg sporta i koliko su "
            "zauzimale. To služi za ograničenja korištenja i da znamo koliko košta.",
        ]),
        ("Pretplata", [
            "Pro se naplaćuje preko App Storea. Ni u jednom trenutku ne vidimo niti "
            "spremamo tvoju karticu ni podatke o plaćanju.",
            "Koristimo RevenueCat da znamo je li tvoja pretplata aktivna, s "
            "identifikatorom tvog računa i ničim više.",
        ]),
        ("Prijatelji i obitelj", [
            "Ako se povežeš s nekim, sprema se da ste povezani i mečevi koje dijelite.",
            "Tvoje @ime je način na koji te drugi pronalaze. Možeš ga promijeniti kad "
            "god hoćeš.",
        ]),
        ("Gdje se sprema", [
            "Na Cloudflareu, u bazi podataka D1. Poslužitelj odgovara samo aplikaciji i "
            "sprema ono što mu aplikacija pošalje.",
        ]),
        ("Ni oglasa ni praćenja", [
            "Nema oglasa. Nema praćenja između aplikacija ni web-stranica. Ništa se ne "
            "prodaje ni ne ustupa trećima za njihovu upotrebu.",
        ]),
        ("Kako sve obrisati", [
            "Iz aplikacije: Postavke › Račun › Obriši račun. Briše se sve tvoje s "
            "poslužitelja i povlači se pristup koji si dao putem Applea.",
            "Ono što je samo na uređaju nestaje kad obrišeš aplikaciju.",
        ]),
        ("Maloljetnici", [
            "Rackers nije namijenjen djeci mlađoj od 13 godina i ne tražimo od njih "
            "podatke svjesno.",
        ]),
        ("Tko za ovo odgovara", [
            "Za obradu ovih podataka odgovara {responsable}, koji radi samostalno i "
            "objavljuje Rackers na svoje ime. Za sve vezano uz tvoje podatke piši na "
            "{correo}.",
            "Imaš pravo vidjeti svoje podatke, ispraviti ih, obrisati ih, prenijeti ih "
            "drugamo i usprotiviti se obradi. Najbrže je obrisati račun iz aplikacije, "
            "ali ako radije tražiš pisanim putem, javi se i napravit će se.",
        ]),
        ("Promjene", [
            "Ako se ovo promijeni, javlja se na ovoj istoj stranici s datumom na vrhu.",
        ]),
    ],

    # --- Condiciones --------------------------------------------------------
    "condiciones_titulo": "Uvjeti korištenja",
    "condiciones_entrada": "Pravila korištenja Rackersa, ukratko i bez sitnih slova.",
    "condiciones_secciones": [
        ("Što je ovo", [
            "Rackers je semafor i bilježnica mečeva za padel, tenis, pickleball, "
            "squash, stolni tenis i badminton, za iPhone i Apple Watch.",
            "Korištenjem prihvaćaš ove uvjete. Ako ih ne prihvaćaš, nemoj je koristiti.",
        ]),
        ("Tvoj račun", [
            "Račun je tvoj i odgovaraš za ono što se s njim radi. @ime ne smije lažno "
            "predstavljati nikoga niti biti uvredljivo; ako jest, može se povući.",
        ]),
        ("Pro i plaćanja", [
            "Rackers je besplatan. Pro je pretplata koja se naplaćuje preko tvog računa "
            "na App Storeu kad potvrdiš kupnju.",
            "Sama se obnavlja osim ako je otkažeš najmanje 24 sata prije isteka "
            "razdoblja. Upravlja se i otkazuje u Postavkama tvog uređaja › tvoje ime › "
            "Pretplate.",
            "Povrate daje Apple, a ne mi, prema vlastitim pravilima.",
        ]),
        ("Obiteljski plan", [
            "Obiteljski plan daje Pro onome tko ga plaća i računima koje pozove, do "
            "granice koju navodi aplikacija. Onaj tko plaća može svakoga maknuti kad "
            "god hoće.",
        ]),
        ("Trener nije liječnik", [
            "Trenerov izvještaj i ono što aplikacija izračuna iz tvojih podataka iz "
            "Zdravlja informativni su. Nisu dijagnoza, ni liječenje, ni stručni "
            "medicinski ili sportski savjet.",
            "Ako se ne osjećaš dobro ili imaš dvojbi o zdravlju, pitaj stručnjaka.",
        ]),
        ("Usluga", [
            "Trudimo se da sve radi, ali aplikacija i poslužitelj nude se takvi kakvi "
            "jesu, bez jamstva da će biti dostupni bez prekida ni da neće biti "
            "pogrešaka.",
            "Sačuvaj ono do čega ti je stalo: sigurnosna kopija pomaže, ali ne "
            "zamjenjuje tvoje vlastite kopije.",
        ]),
        ("Ispravna upotreba", [
            "Ne smije se pokušavati razbiti usluga, vaditi iz nje podatke drugih računa "
            "ni koristiti je za išta nezakonito. Ako se to dogodi, račun se može "
            "zatvoriti.",
        ]),
        ("Promjene", [
            "Ovi se uvjeti mogu promijeniti. Promjene se objavljuju ovdje s datumom, a "
            "daljnje korištenje aplikacije znači da ih prihvaćaš.",
        ]),
    ],

    # --- Soporte ------------------------------------------------------------
    "soporte_titulo": "Podrška",
    "soporte_entrada": "Nešto ne radi ili imaš bolju ideju? Piši i odgovorit ćemo ti.",
    "soporte_correo_titulo": "Piši nam",
    "soporte_correo_nota": "Odgovara čovjek. Ako je greška, opiši što si radio, što si "
                           "očekivao i što se dogodilo, i reci koji iPhone i koju "
                           "verziju iOS-a imaš: tako se brže popravi.",
    "soporte_secciones": [
        ("Brisanje računa", [
            "U aplikaciji: Postavke › Račun › Obriši račun. Briše se sve tvoje s "
            "poslužitelja i povlači se Appleov pristup. Ne trebaš nam pisati.",
        ]),
        ("Pretplata", [
            "Pro se upravlja i otkazuje u Postavkama tvog uređaja › tvoje ime › "
            "Pretplate. Povrate daje Apple preko reportaproblem.apple.com.",
        ]),
        ("Sat ne vidi mečeve", [
            "Sat i iPhone se usklade kad su blizu i kad su na oba otvorena aplikacija. "
            "Ako ne, otvori Rackers na oba i pričekaj nekoliko sekundi.",
            "Sat radi sam: možeš odigrati cijeli meč bez iPhonea uza se, a poslije će "
            "se već uskladiti.",
        ]),
        ("Zdravlje i dopuštenja", [
            "Za mjerenje pulsa treba dati dopuštenje Zdravlju. Ako si ga odbio, daje se "
            "ponovno u Postavke › Zdravlje › Pristup podacima › Rackers.",
            "Puls se mjeri kao trening, pa sat ostaje u aplikaciji dok igraš.",
        ]),
        ("Trener", [
            "Analiza videa je Pro i ima ograničenje broja korištenja na dan i na "
            "mjesec. Ako analiza ne uspije, ne računa se.",
        ]),
    ],
}
