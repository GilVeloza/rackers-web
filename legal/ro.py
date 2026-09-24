"""Confidențialitate, Condiții și Asistență în română."""

TEXTO = {
    "legal_volver": 'Înapoi la pagina principală',
    "legal_actualizado": 'Actualizat pe 23 septembrie 2026',

    "privacidad_titulo": 'Confidențialitate',
    "privacidad_entrada": 'Rackers e făcut ca să joci, nu ca să strângă date. Aici scrie limpede ce se salvează, unde și cum ștergi.',
    "privacidad_secciones": [
        ('Fără cont nimic nu îți părăsește iPhone-ul', [
            'Poți folosi tot Rackers fără să-ți faci cont. Meciurile, turneele și setările rămân pe dispozitiv și nu pleacă nicăieri.',
            'Contul face trei lucruri: ține iPhone-ul și ceasul la fel, nu pierzi nimic când schimbi telefonul și poți juca cu prietenii.',
        ]),
        ('Ce salvează contul', [
            'Contul se creează cu Autentificare cu Apple. Apple ne dă un identificator stabil, numele tău și un e-mail, care va fi adresa privată de redirecționare de la Apple dacă alegi să o ascunzi pe a ta.',
            'Păstrăm acel identificator, e-mailul, numele afișat și @numele ales. Și permisiunea dată de Apple ca accesul să poată fi retras când îți ștergi contul.',
        ]),
        ('Copia de siguranță', [
            'Cu cont, aplicația își încarcă conținutul: jucători, etape, meciuri, turnee, analize și setări.',
            'Meciurile duc cu ele ce a măsurat ceasul cât ai jucat: puls, distanță și energie. Merge cu meciul pentru că ține de meci.',
        ]),
        ('Ce nu îți părăsește niciodată iPhone-ul', [
            'Pulsul în repaus, variabilitatea și somnul — cele din « Cum intri azi » — se citesc din aplicația Sănătate și rămân pe dispozitiv. Nu se încarcă și nu se împart cu nimeni.',
            'Accesul la Sănătate poate fi retras oricând din Setări › Sănătate › Acces la date, iar aplicația funcționează mai departe.',
        ]),
        ('Antrenorul cu IA', [
            'Când ceri o analiză, aplicația scoate cadre din filmare și le trimite la OpenAI prin serverul nostru, care întoarce raportul.',
            'Din filmare nu se salvează nimic pe server. Raportul se întoarce în aplicație și rămâne în copia ta.',
            'Rămâne evidența câte analize ai cerut, pentru ce sport și cât de mari au fost. Servește limitelor de folosire și costului.',
        ]),
        ('Abonamentul', [
            'Pro se încasează prin App Store. Nu vedem și nu salvăm niciodată cardul sau datele tale de plată.',
            'Folosim RevenueCat ca să știm dacă abonamentul e la zi, cu identificatorul contului tău și nimic altceva.',
        ]),
        ('Prieteni și familie', [
            'Dacă te legi cu cineva, se salvează că sunteți legați și meciurile pe care le împărțiți.',
            '@numele tău e felul în care te găsesc ceilalți. Îl poți schimba oricând.',
        ]),
        ('Unde se păstrează', [
            'La Cloudflare, într-o bază de date D1. Serverul răspunde doar aplicației și ține doar ce îi trimite aplicația.',
        ]),
        ('Fără reclame și fără urmărire', [
            'Nu există publicitate. Nu există urmărire între aplicații sau site-uri. Nimic nu se vinde și nu se dă unor terți pentru folosul lor.',
        ]),
        ('Cum ștergi tot', [
            'În aplicație: Setări › Cont › Șterge contul. Tot ce e al tău se șterge de pe server și accesul dat prin Apple se retrage.',
            'Ce e doar pe dispozitiv dispare când ștergi aplicația.',
        ]),
        ('Minori', [
            'Rackers nu e gândit pentru copii sub 13 ani și nu le colectăm cu bună știință datele.',
        ]),
        ('Cine răspunde de asta', [
            'De prelucrarea acestor date răspunde {responsable}, care lucrează pe cont propriu și publică Rackers pe numele său. Pentru orice ține de datele tale, scrie la {correo}.',
            'Ai dreptul să-ți vezi datele, să le corectezi, să le ștergi, să le duci în altă parte și să te opui prelucrării. Cel mai repede e să ștergi contul din aplicație, dar dacă preferi să ceri în scris, scrie și se face.',
        ]),
        ('Modificări', [
            'Dacă se schimbă ceva, va fi pe această pagină cu data sus.',
        ]),
    ],

    "condiciones_titulo": 'Condiții de utilizare',
    "condiciones_entrada": 'Regulile de folosire a Rackers, pe scurt și fără litere mici.',
    "condiciones_secciones": [
        ('Despre ce e vorba', [
            'Rackers e un tabelă de scor și un caiet de meciuri pentru padel, tenis, pickleball, squash, tenis de masă și badminton, pentru iPhone și Apple Watch.',
            'Folosindu-l accepți aceste condiții. Dacă nu le accepți, nu-l folosi.',
        ]),
        ('Contul tău', [
            'Contul e al tău și răspunzi de ce se face cu el. @numele nu poate să se dea drept altcineva și nu poate fi jignitor; dacă e, poate fi retras.',
        ]),
        ('Pro și plățile', [
            'Rackers e gratuit. Pro e un abonament încasat din contul tău App Store la confirmarea cumpărării.',
            'Se reînnoiește singur dacă nu îl anulezi cu cel puțin 24 de ore înainte să se termine perioada. Se administrează și se anulează din Setări pe dispozitiv › numele tău › Abonamente.',
            'Rambursările le dă Apple, nu noi, după regulile lor.',
        ]),
        ('Planul de familie', [
            'Planul de familie dă Pro celui care plătește și conturilor invitate, până la limita spusă în aplicație. Cine plătește poate scoate pe oricine oricând.',
        ]),
        ('Antrenorul nu e medic', [
            'Raportul antrenorului și tot ce calculează aplicația din datele tale de Sănătate sunt orientative. Nu sunt diagnostic, tratament sau sfat medical ori sportiv profesionist.',
            'Dacă nu te simți bine sau ai îndoieli legate de sănătate, întreabă un specialist.',
        ]),
        ('Serviciul', [
            'Facem ce putem ca totul să meargă, dar aplicația și serverul se oferă așa cum sunt, fără garanția disponibilității neîntrerupte sau a lipsei de erori.',
            'Păstrează ce contează pentru tine: copia de siguranță ajută, dar nu înlocuiește copiile tale.',
        ]),
        ('Folosire corectă', [
            'Nu ai voie să încerci să strici serviciul, să scoți din el date ale altor conturi sau să-l folosești pentru ceva ilegal. Dacă se întâmplă, contul poate fi închis.',
        ]),
        ('Modificări', [
            'Aceste condiții se pot schimba. Modificările se publică aici cu data lor, iar folosirea în continuare a aplicației înseamnă că le accepți.',
        ]),
    ],

    "soporte_titulo": 'Asistență',
    "soporte_entrada": 'Nu merge ceva, sau ți-a venit o idee mai bună? Scrie-ne și îți răspundem.',
    "soporte_correo_titulo": 'Scrie-ne',
    "soporte_correo_nota": 'Răspunde un om. Dacă e o eroare, spune ce făceai, ce te așteptai și ce s-a întâmplat, și zi ce iPhone și ce versiune de iOS ai: așa se repară mai repede.',
    "soporte_secciones": [
        ('Ștergerea contului', [
            'În aplicație: Setări › Cont › Șterge contul. Tot ce e al tău se șterge de pe server și accesul Apple se retrage. Nu trebuie să ne scrii.',
        ]),
        ('Abonamentul', [
            'Pro se administrează și se anulează din Setări pe dispozitiv › numele tău › Abonamente. Rambursările le dă Apple pe reportaproblem.apple.com.',
        ]),
        ('Ceasul nu vede meciurile', [
            'Ceasul și iPhone-ul se pun la punct când sunt aproape și aplicația e deschisă pe amândouă. Dacă nu, deschide Rackers pe amândouă și așteaptă câteva secunde.',
            'Ceasul se descurcă singur: poți puncta un meci întreg fără iPhone lângă tine, se înțeleg ele mai târziu.',
        ]),
        ('Sănătate și permisiuni', [
            'Ca să măsoare pulsul e nevoie de acces la Sănătate. Dacă ai refuzat, îl dai din nou din Setări › Sănătate › Acces la date › Rackers.',
            'Pulsul se măsoară cu un antrenament, așa că ceasul rămâne în aplicație cât joci.',
        ]),
        ('Antrenorul', [
            'Analiza video ține de Pro și are o limită pe zi și pe lună. Dacă o analiză eșuează, nu se pune la socoteală.',
        ]),
    ],
}
