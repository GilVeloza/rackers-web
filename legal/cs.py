"""Soukromí, Podmínky a Podpora v češtině."""

TEXTO = {
    "legal_volver": 'Zpět na úvodní stránku',
    "legal_actualizado": 'Aktualizováno 25. září 2026',

    "privacidad_titulo": 'Soukromí',
    "privacidad_entrada": 'Rackers vznikl na hraní, ne na sbírání dat. Tady je jasně, co se ukládá, kde a jak to smazat.',
    "privacidad_secciones": [
        ('Bez účtu nic neopustí tvůj iPhone', [
            'Celý Rackers můžeš používat bez zakládání účtu. Zápasy, turnaje i nastavení zůstanou v zařízení a nikam neputují.',
            'Účet dělá tři věci: drží iPhone a hodinky stejné, nic neztratíš při výměně telefonu a můžeš hrát s přáteli.',
        ]),
        ('Co ukládá účet', [
            'Účet se zakládá přes Přihlásit se s Apple. Apple nám dá stálý identifikátor, tvé jméno a e-mail, který bude soukromá přeposílací adresa od Apple, pokud svou skryješ.',
            'Ukládáme ten identifikátor, e-mail, jméno, které ukazuješ, a @jméno, které si zvolíš. A také svolení od Apple, aby šel přístup odebrat, když účet smažeš.',
        ]),
        ('Záloha', [
            'S účtem aplikace nahraje svůj obsah: hráče, herní dny, zápasy, turnaje, rozbory a nastavení.',
            'Zápasy s sebou nesou to, co hodinky naměřily při hře: tep, vzdálenost a energii. Jede to se zápasem, protože to k zápasu patří.',
        ]),
        ('Co tvůj iPhone nikdy neopustí', [
            'Klidový tep, variabilita a spánek — to z « Jak na tom dnes jsi » — se čtou z aplikace Zdraví a zůstávají v zařízení. Nenahrávají se a s nikým se nesdílejí.',
            'Přístup ke Zdraví můžeš kdykoli odebrat v Nastavení › Zdraví › Přístup k datům, a aplikace funguje dál.',
        ]),
        ('Trenér s AI', [
            'Když si vyžádáš rozbor, aplikace vezme z videa snímky a pošle je přes náš server do OpenAI, který vrátí zprávu.',
            'Z videa se na serveru neukládá nic. Zpráva se vrátí do aplikace a zůstane v tvé záloze.',
            'Zůstane záznam o tom, kolik rozborů jsi si vyžádal, pro jaký sport a jak byly velké. Slouží to limitům použití a přehledu o nákladech.',
        ]),
        ('Předplatné', [
            'Pro se účtuje přes App Store. Tvou kartu ani platební údaje nikdy nevidíme a neukládáme.',
            'Používáme RevenueCat, abychom věděli, jestli předplatné běží — s identifikátorem tvého účtu a ničím jiným.',
        ]),
        ('Přátelé a rodina', [
            'Když se s někým propojíš, uloží se, že jste propojení, a zápasy, které sdílíte.',
            'Tvé @jméno je to, podle čeho tě ostatní najdou. Můžeš ho kdykoli změnit.',
        ]),
        ('Kde to leží', [
            'U Cloudflare, v databázi D1. Server odpovídá jen aplikaci a drží jen to, co mu aplikace pošle.',
        ]),
        ('Žádné reklamy, žádné sledování', [
            'Žádná reklama. Žádné sledování napříč aplikacemi ani weby. Nic se neprodává ani nepředává třetím stranám pro jejich vlastní použití.',
        ]),
        ('Jak všechno smazat', [
            'V aplikaci: Nastavení › Účet › Smazat účet. Všechno tvoje se smaže ze serveru a přístup daný přes Apple se odvolá.',
            'Co je jen v zařízení, zmizí, když aplikaci smažeš.',
        ]),
        ('Nezletilí', [
            'Rackers není určen dětem do 13 let a jejich údaje vědomě nesbíráme.',
        ]),
        ('Kdo za to odpovídá', [
            'Za zpracování těchto údajů odpovídá {responsable}, osoba samostatně výdělečně činná, která Rackers vydává pod svým jménem. Ve všem, co se týká tvých údajů, piš na {correo}.',
            'Máš právo své údaje vidět, opravit, smazat, vzít jinam a bránit se jejich zpracování. Nejrychleji to jde smazáním účtu v aplikaci, ale pokud to raději požádáš písemně, napiš a udělá se to.',
        ]),
        ('Změny', [
            'Pokud se něco z toho změní, bude to na této stránce s datem nahoře.',
        ]),
    ],

    "condiciones_titulo": 'Podmínky užívání',
    "condiciones_entrada": 'Pravidla pro používání Rackersu, krátce a bez drobného písma.',
    "condiciones_secciones": [
        ('O co jde', [
            'Rackers je ukazatel skóre a zápisník zápasů pro padel, tenis, pickleball, squash, stolní tenis a badminton, pro iPhone a Apple Watch.',
            'Používáním přijímáš tyto podmínky. Pokud je nepřijímáš, nepoužívej ho.',
        ]),
        ('Tvůj účet', [
            'Účet je tvůj a odpovídáš za to, co se s ním dělá. @jméno se nesmí za nikoho vydávat ani být urážlivé; pokud je, lze ho odebrat.',
            'Urážky, obtěžování ani urážlivý obsah se netolerují. V aplikaci můžeš zablokovat nebo nahlásit jakýkoli účet; nahlášení do 24 hodin zkontroluje člověk a kdo tato pravidla poruší, přijde o účet.',
        ]),
        ('Pro a platby', [
            'Rackers je zdarma. Pro je předplatné účtované na tvém účtu App Store při potvrzení nákupu.',
            'Obnovuje se samo, pokud ho nezrušíš nejméně 24 hodin před koncem období. Spravuje a ruší se v Nastavení zařízení › tvé jméno › Předplatná.',
            'Vrácení peněz poskytuje Apple, ne my, podle vlastních pravidel.',
        ]),
        ('Rodinný tarif', [
            'Rodinný tarif dává Pro tomu, kdo platí, a účtům, které pozve, až do limitu uvedeného v aplikaci. Kdo platí, může kohokoli kdykoli odebrat.',
        ]),
        ('Trenér není lékař', [
            'Zpráva trenéra a vše, co aplikace spočítá z tvých dat ze Zdraví, je orientační. Není to diagnóza, léčba ani lékařská či profesionální sportovní rada.',
            'Pokud se necítíš dobře nebo máš pochybnosti o zdraví, zeptej se odborníka.',
        ]),
        ('Služba', [
            'Děláme, co jde, aby všechno fungovalo, ale aplikace a server se nabízejí tak, jak jsou, bez záruky nepřetržité dostupnosti či bezchybnosti.',
            'Uchovej si, na čem ti záleží: záloha pomůže, ale nenahradí tvé vlastní kopie.',
        ]),
        ('Správné užívání', [
            'Není dovoleno pokoušet se službu rozbít, tahat z ní data jiných účtů nebo ji používat k něčemu nezákonnému. Pokud se to stane, účet lze uzavřít.',
        ]),
        ('Změny', [
            'Tyto podmínky se mohou změnit. Změny se zveřejňují zde s datem a další používání aplikace znamená jejich přijetí.',
        ]),
    ],

    "soporte_titulo": 'Podpora',
    "soporte_entrada": 'Něco nefunguje, nebo tě napadlo něco lepšího? Napiš a odpovíme.',
    "soporte_correo_titulo": 'Napiš nám',
    "soporte_correo_nota": 'Odpovídá člověk. Jde-li o chybu, napiš, co jsi dělal, co jsi čekal a co se stalo, a uveď, jaký máš iPhone a jakou verzi iOS — tak se to spraví dřív.',
    "soporte_secciones": [
        ('Smazání účtu', [
            'V aplikaci: Nastavení › Účet › Smazat účet. Všechno tvoje se smaže ze serveru a přístup Apple se odvolá. Nemusíš nám psát.',
        ]),
        ('Předplatné', [
            'Pro se spravuje a ruší v Nastavení zařízení › tvé jméno › Předplatná. Vrácení peněz dává Apple na reportaproblem.apple.com.',
        ]),
        ('Hodinky nevidí zápasy', [
            'Hodinky a iPhone se doženou, když jsou blízko sebe a na obou je aplikace otevřená. Jinak otevři Rackers na obou a pár vteřin počkej.',
            'Hodinky si poradí samy: celý zápas můžeš odpískat bez iPhonu poblíž, domluví se později.',
        ]),
        ('Zdraví a oprávnění', [
            'K měření tepu je potřeba přístup ke Zdraví. Když jsi odmítl, dáš ho znovu v Nastavení › Zdraví › Přístup k datům › Rackers.',
            'Tep se měří tréninkem, takže hodinky zůstanou při hře v aplikaci.',
        ]),
        ('Trenér', [
            'Rozbor videa patří k Pro a má denní a měsíční limit. Když rozbor selže, nepočítá se.',
        ]),
    ],
}
