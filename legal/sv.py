"""Integritet, Villkor och Support på svenska."""

TEXTO = {
    "legal_volver": "Tillbaka till startsidan",
    "legal_actualizado": "Uppdaterad 25 september 2026",

    "privacidad_titulo": "Integritet",
    "privacidad_entrada": "Rackers är gjord för att spela, inte för att samla data. Här "
                          "står det klart vad som sparas, var och hur du raderar det.",
    "privacidad_secciones": [
        ("Utan konto lämnar ingenting din iPhone", [
            "Du kan använda hela Rackers utan att skapa konto. Dina matcher, turneringar "
            "och inställningar stannar på enheten och går ingenstans.",
            "Kontot gör tre saker: håller iPhone och klocka lika, gör att inget försvinner "
            "när du byter telefon, och låter dig spela med vänner.",
        ]),
        ("Vad kontot sparar", [
            "Kontot skapas med Logga in med Apple. Apple ger oss en fast identifierare, "
            "ditt namn och en e-postadress, som blir Apples privata vidarebefordran om du "
            "väljer att dölja din.",
            "Vi sparar den identifieraren, e-postadressen, namnet du visar och det @namn "
            "du väljer. Samt tillståndet Apple ger för att kunna dra tillbaka åtkomsten "
            "när du raderar kontot.",
        ]),
        ("Säkerhetskopian", [
            "Med konto laddar appen upp sitt innehåll: spelare, speldagar, matcher, "
            "turneringar, analyser och inställningar.",
            "Matcherna bär med sig vad klockan mätte medan du spelade: puls, sträcka och "
            "energi. Det följer med matchen eftersom det hör till matchen.",
        ]),
        ("Vad som aldrig lämnar din iPhone", [
            "Vilopuls, variabilitet och sömn — det i « Hur du kommer in idag » — läses "
            "från Hälsa-appen och stannar på enheten. Det laddas inte upp och delas inte "
            "med någon.",
            "Åtkomsten till Hälsa kan du dra tillbaka när du vill i Inställningar › Hälsa "
            "› Dataåtkomst, och appen fortsätter fungera.",
        ]),
        ("AI-tränaren", [
            "När du ber om en analys tar appen bildrutor ur videon och skickar dem till "
            "OpenAI via vår server, som skickar tillbaka rapporten.",
            "Inget från videon sparas på servern. Rapporten kommer tillbaka till appen och "
            "stannar i din egen kopia.",
            "Det som blir kvar är räkningen av hur många analyser du bett om, för vilken "
            "sport och hur stora de var. Det är för användningsgränserna och för att veta "
            "vad det kostar.",
        ]),
        ("Prenumerationen", [
            "Pro debiteras via App Store. Vi ser eller sparar aldrig ditt kort eller dina "
            "betaluppgifter.",
            "Vi använder RevenueCat för att veta om din prenumeration gäller, med din "
            "kontoidentifierare och inget annat.",
        ]),
        ("Vänner och familj", [
            "Om du länkar ihop dig med någon sparas att ni är länkade och matcherna ni "
            "delar.",
            "Ditt @namn är hur andra hittar dig. Du kan ändra det när du vill.",
        ]),
        ("Var det sparas", [
            "Hos Cloudflare, i en D1-databas. Servern svarar bara appen och behåller bara "
            "det appen skickar.",
        ]),
        ("Ingen reklam, ingen spårning", [
            "Det finns ingen reklam. Ingen spårning mellan appar eller webbplatser. "
            "Ingenting säljs eller lämnas till tredje part för deras eget bruk.",
        ]),
        ("Hur du raderar allt", [
            "I appen: Inställningar › Konto › Radera konto. Allt ditt raderas från servern "
            "och åtkomsten du gav med Apple dras tillbaka.",
            "Det som bara finns på enheten försvinner när du raderar appen.",
        ]),
        ("Barn", [
            "Rackers är inte avsedd för barn under 13 år och vi samlar inte medvetet in "
            "deras uppgifter.",
        ]),
        ("Vem som ansvarar", [
            "Ansvarig för behandlingen av dessa uppgifter är {responsable}, egenföretagare, "
            "som ger ut Rackers i eget namn. För allt som rör dina uppgifter, skriv till "
            "{correo}.",
            "Du har rätt att se dina uppgifter, rätta dem, radera dem, ta med dem någon "
            "annanstans och invända mot behandlingen. Snabbast är att radera kontot i "
            "appen, men vill du hellre begära det skriftligt, skriv så ordnas det.",
        ]),
        ("Ändringar", [
            "Om något av detta ändras meddelas det på den här sidan med datum överst.",
        ]),
    ],

    "condiciones_titulo": "Användarvillkor",
    "condiciones_entrada": "Reglerna för att använda Rackers, kort och utan finstilt.",
    "condiciones_secciones": [
        ("Vad det här är", [
            "Rackers är en resultattavla och en matchbok för padel, tennis, pickleball, "
            "squash, bordtennis och badminton, för iPhone och Apple Watch.",
            "Genom att använda den godtar du dessa villkor. Godtar du dem inte, använd den "
            "inte.",
        ]),
        ("Ditt konto", [
            "Kontot är ditt och du svarar för vad som görs med det. @namnet får inte "
            "utge sig för att vara någon annan eller vara stötande; är det så kan det dras "
            "in.",
            'Förolämpningar, trakasserier och kränkande innehåll tolereras inte. I appen kan du blockera eller anmäla vilket konto som helst; en människa granskar anmälningar inom 24 timmar, och den som bryter mot reglerna förlorar sitt konto.',
        ]),
        ("Pro och betalningar", [
            "Rackers är gratis. Pro är en prenumeration som debiteras ditt App "
            "Store-konto när du bekräftar köpet.",
            "Den förnyas av sig själv om du inte säger upp den minst 24 timmar innan "
            "perioden tar slut. Den hanteras och sägs upp i Inställningar på din enhet › "
            "ditt namn › Prenumerationer.",
            "Återbetalningar ges av Apple, inte av oss, enligt deras egna regler.",
        ]),
        ("Familjeplanen", [
            "Familjeplanen ger Pro till den som betalar och till de konton hen bjuder in, "
            "upp till gränsen appen anger. Den som betalar kan ta bort vem som helst när "
            "som helst.",
        ]),
        ("Tränaren är ingen läkare", [
            "Tränarens rapport och allt appen räknar ut från dina Hälsa-data är "
            "vägledande. Det är ingen diagnos, ingen behandling och inget medicinskt eller "
            "professionellt idrottsråd.",
            "Mår du dåligt eller är osäker på din hälsa, fråga en fackperson.",
        ]),
        ("Tjänsten", [
            "Vi gör vad vi kan för att allt ska fungera, men appen och servern erbjuds som "
            "de är, utan garanti för oavbruten tillgänglighet eller frihet från fel.",
            "Spara det som betyder något för dig: säkerhetskopian hjälper, men ersätter "
            "inte dina egna kopior.",
        ]),
        ("Rätt användning", [
            "Det är inte tillåtet att försöka bryta sönder tjänsten, hämta ut data från "
            "andras konton eller använda den till något olagligt. Sker det kan kontot "
            "stängas.",
        ]),
        ("Ändringar", [
            "Dessa villkor kan ändras. Ändringar publiceras här med sitt datum, och att "
            "fortsätta använda appen innebär att du godtar dem.",
        ]),
    ],

    "soporte_titulo": "Support",
    "soporte_entrada": "Något som inte fungerar, eller en bättre idé? Skriv så svarar vi.",
    "soporte_correo_titulo": "Skriv till oss",
    "soporte_correo_nota": "Det är en människa som svarar. Är det ett fel: berätta vad du "
                           "gjorde, vad du väntade dig och vad som hände, och säg vilken "
                           "iPhone och vilken iOS-version du har — då löses det snabbare.",
    "soporte_secciones": [
        ("Radera ditt konto", [
            "I appen: Inställningar › Konto › Radera konto. Allt ditt raderas från servern "
            "och Apple-åtkomsten dras tillbaka. Du behöver inte skriva till oss.",
        ]),
        ("Prenumerationen", [
            "Pro hanteras och sägs upp i Inställningar på din enhet › ditt namn › "
            "Prenumerationer. Återbetalningar ges av Apple på reportaproblem.apple.com.",
        ]),
        ("Klockan ser inte matcherna", [
            "Klockan och iPhone kommer ikapp när de är nära varandra och appen är öppen på "
            "båda. Annars: öppna Rackers på båda och vänta några sekunder.",
            "Klockan klarar sig själv: du kan räkna en hel match utan iPhone i närheten, "
            "de kommer överens sedan.",
        ]),
        ("Hälsa och tillstånd", [
            "För att mäta pulsen krävs åtkomst till Hälsa. Sa du nej går det att ge den "
            "igen i Inställningar › Hälsa › Dataåtkomst › Rackers.",
            "Pulsen mäts med ett träningspass, så klockan stannar i appen medan du spelar.",
        ]),
        ("Tränaren", [
            "Videoanalys ingår i Pro och har en gräns per dag och per månad. Misslyckas en "
            "analys räknas den inte.",
        ]),
    ],
}
