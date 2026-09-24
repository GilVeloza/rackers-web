"""Prywatność, Warunki i Pomoc po polsku."""

TEXTO = {
    "legal_volver": "Wróć na stronę główną",
    "legal_actualizado": "Zaktualizowano 23 września 2026",

    "privacidad_titulo": "Prywatność",
    "privacidad_entrada": "Rackers powstał do grania, nie do zbierania danych. Tu jasno "
                          "napisane, co się zapisuje, gdzie i jak to usunąć.",
    "privacidad_secciones": [
        ("Bez konta nic nie opuszcza iPhone'a", [
            "Możesz korzystać z całego Rackersa bez zakładania konta. Mecze, turnieje i "
            "ustawienia zostają na urządzeniu i nigdzie nie wędrują.",
            "Konto daje trzy rzeczy: to samo na iPhonie i zegarku, nic nie ginie przy "
            "zmianie telefonu, i można grać ze znajomymi.",
        ]),
        ("Co zapisuje konto", [
            "Konto zakłada się przez Zaloguj się z Apple. Apple daje nam stały "
            "identyfikator, twoje imię i adres e-mail — będzie to adres przekierowania "
            "Apple, jeśli ukryjesz swój.",
            "Przechowujemy ten identyfikator, adres e-mail, wyświetlaną nazwę i wybraną "
            "@nazwę. Oraz zgodę od Apple, żeby móc cofnąć dostęp, gdy usuniesz konto.",
        ]),
        ("Kopia zapasowa", [
            "Z kontem aplikacja wysyła swoją zawartość: graczy, dni gry, mecze, turnieje, "
            "analizy i ustawienia.",
            "Mecze niosą to, co zmierzył zegarek w trakcie gry: tętno, dystans i energię. "
            "Jedzie z meczem, bo należy do meczu.",
        ]),
        ("Co nigdy nie opuszcza twojego iPhone'a", [
            "Tętno spoczynkowe, zmienność i sen — to z « Jak dziś wchodzisz » — są "
            "odczytywane z aplikacji Zdrowie i zostają na urządzeniu. Nie są wysyłane ani "
            "z nikim dzielone.",
            "Dostęp do Zdrowia możesz cofnąć, kiedy chcesz, w Ustawienia › Zdrowie › "
            "Dostęp do danych, a aplikacja dalej działa.",
        ]),
        ("Trener z AI", [
            "Kiedy prosisz o analizę, aplikacja wycina klatki z nagrania i wysyła je do "
            "OpenAI przez nasz serwer, który zwraca raport.",
            "Z nagrania nic nie zostaje na serwerze. Raport wraca do aplikacji i zostaje w "
            "twojej kopii.",
            "Zostaje natomiast zapis, ile analiz zamówiłeś, dla jakiego sportu i jak duże "
            "były. Służy limitom użycia i wiedzy o koszcie.",
        ]),
        ("Subskrypcja", [
            "Pro rozlicza App Store. Nigdy nie widzimy ani nie zapisujemy twojej karty "
            "ani danych płatności.",
            "Używamy RevenueCat, żeby wiedzieć, czy subskrypcja jest aktywna — z "
            "identyfikatorem twojego konta i niczym więcej.",
        ]),
        ("Znajomi i rodzina", [
            "Jeśli połączysz się z kimś, zapisuje się, że jesteście połączeni, i mecze, "
            "które dzielicie.",
            "Twoja @nazwa to sposób, w jaki znajdują cię inni. Możesz ją zmienić, kiedy "
            "chcesz.",
        ]),
        ("Gdzie to leży", [
            "W Cloudflare, w bazie D1. Serwer odpowiada tylko aplikacji i trzyma tylko "
            "to, co aplikacja mu wyśle.",
        ]),
        ("Bez reklam i bez śledzenia", [
            "Nie ma reklam. Nie ma śledzenia między aplikacjami ani stronami. Nic nie jest "
            "sprzedawane ani przekazywane osobom trzecim do ich własnych celów.",
        ]),
        ("Jak wszystko usunąć", [
            "W aplikacji: Ustawienia › Konto › Usuń konto. Wszystko twoje znika z serwera, "
            "a dostęp udzielony przez Apple zostaje cofnięty.",
            "To, co jest tylko na urządzeniu, znika po usunięciu aplikacji.",
        ]),
        ("Nieletni", [
            "Rackers nie jest przeznaczony dla dzieci poniżej 13 lat i świadomie nie "
            "zbieramy ich danych.",
        ]),
        ("Kto za to odpowiada", [
            "Za przetwarzanie tych danych odpowiada {responsable}, prowadzący działalność "
            "na własny rachunek, wydający Rackersa pod własnym nazwiskiem. We wszystkim, "
            "co dotyczy twoich danych, pisz na {correo}.",
            "Masz prawo zobaczyć swoje dane, poprawić je, usunąć, przenieść gdzie indziej "
            "i sprzeciwić się przetwarzaniu. Najszybciej jest usunąć konto w aplikacji, "
            "ale jeśli wolisz poprosić na piśmie — napisz, a się to zrobi.",
        ]),
        ("Zmiany", [
            "Jeśli coś z tego się zmieni, będzie to na tej stronie z datą u góry.",
        ]),
    ],

    "condiciones_titulo": "Warunki korzystania",
    "condiciones_entrada": "Zasady korzystania z Rackersa, krótko i bez drobnego druku.",
    "condiciones_secciones": [
        ("O co chodzi", [
            "Rackers to tablica wyników i zeszyt meczów do padla, tenisa, pickleballa, "
            "squasha, tenisa stołowego i badmintona, na iPhone'a i Apple Watch.",
            "Korzystając z niego, akceptujesz te warunki. Jeśli ich nie akceptujesz, nie "
            "korzystaj.",
        ]),
        ("Twoje konto", [
            "Konto jest twoje i odpowiadasz za to, co się z nim robi. @nazwa nie może "
            "podszywać się pod nikogo ani być obraźliwa; jeśli jest, można ją odebrać.",
        ]),
        ("Pro i płatności", [
            "Rackers jest darmowy. Pro to subskrypcja rozliczana na twoim koncie App "
            "Store przy potwierdzeniu zakupu.",
            "Odnawia się sama, chyba że anulujesz ją co najmniej 24 godziny przed końcem "
            "okresu. Zarządza się nią i anuluje w Ustawieniach urządzenia › twoje imię › "
            "Subskrypcje.",
            "Zwroty daje Apple, nie my, według własnych zasad.",
        ]),
        ("Plan rodzinny", [
            "Plan rodzinny daje Pro płacącemu i zaproszonym kontom, do limitu podanego w "
            "aplikacji. Płacący może usunąć każdego w dowolnym momencie.",
        ]),
        ("Trener to nie lekarz", [
            "Raport trenera i wszystko, co aplikacja wyliczy z twoich danych Zdrowia, ma "
            "charakter orientacyjny. To nie diagnoza, nie leczenie i nie porada lekarska "
            "ani profesjonalna sportowa.",
            "Jeśli źle się czujesz albo masz wątpliwości co do zdrowia, zapytaj "
            "specjalistę.",
        ]),
        ("Usługa", [
            "Robimy, co się da, żeby wszystko działało, ale aplikacja i serwer są "
            "udostępniane takie, jakie są, bez gwarancji nieprzerwanej dostępności ani "
            "braku błędów.",
            "Zachowaj to, na czym ci zależy: kopia zapasowa pomaga, ale nie zastępuje "
            "twoich własnych kopii.",
        ]),
        ("Właściwe korzystanie", [
            "Nie wolno próbować rozbić usługi, wyciągać z niej danych innych kont ani "
            "używać jej do czegoś niezgodnego z prawem. Jeśli to nastąpi, konto może "
            "zostać zamknięte.",
        ]),
        ("Zmiany", [
            "Te warunki mogą się zmienić. Zmiany publikujemy tutaj z datą, a dalsze "
            "korzystanie z aplikacji oznacza ich akceptację.",
        ]),
    ],

    "soporte_titulo": "Pomoc",
    "soporte_entrada": "Coś nie działa albo masz lepszy pomysł? Napisz, a odpowiemy.",
    "soporte_correo_titulo": "Napisz do nas",
    "soporte_correo_nota": "Odpowiada człowiek. Jeśli to błąd, napisz, co robiłeś, czego się "
                           "spodziewałeś i co się stało, oraz podaj, jakiego masz iPhone'a i "
                           "którą wersję iOS — wtedy naprawa idzie szybciej.",
    "soporte_secciones": [
        ("Usunięcie konta", [
            "W aplikacji: Ustawienia › Konto › Usuń konto. Wszystko twoje znika z serwera, "
            "a dostęp Apple zostaje cofnięty. Nie musisz do nas pisać.",
        ]),
        ("Subskrypcja", [
            "Pro zarządza się i anuluje w Ustawieniach urządzenia › twoje imię › "
            "Subskrypcje. Zwroty daje Apple na reportaproblem.apple.com.",
        ]),
        ("Zegarek nie widzi meczów", [
            "Zegarek i iPhone nadrabiają, kiedy są blisko siebie i na obu jest otwarta "
            "aplikacja. Jeśli nie — otwórz Rackersa na obu i poczekaj kilka sekund.",
            "Zegarek radzi sobie sam: możesz policzyć cały mecz bez iPhone'a w pobliżu, "
            "potem się dogadają.",
        ]),
        ("Zdrowie i uprawnienia", [
            "Do pomiaru tętna potrzebny jest dostęp do Zdrowia. Jeśli odmówiłeś, dasz go "
            "znowu w Ustawienia › Zdrowie › Dostęp do danych › Rackers.",
            "Tętno mierzy się treningiem, więc zegarek zostaje w aplikacji, kiedy grasz.",
        ]),
        ("Trener", [
            "Analiza wideo należy do Pro i ma limit dzienny i miesięczny. Jeśli analiza "
            "się nie uda, nie jest liczona.",
        ]),
    ],
}
