"""Privacidad, Condiciones y Soporte en fi.

Lo que dice aquí tiene que casar con lo que hace el código: la copia de
seguridad sube partidos (con el pulso que midió el reloj), la salud de «Cómo
llegas hoy» no sale del iPhone y del vídeo del entrenador solo se guardan
unos segundos sin sonido de cada mejora, que se borran con su análisis.
Si eso cambia en la app o en el servidor, esto cambia también.
"""

TEXTO = {
    "legal_volver": "Takaisin etusivulle",
    "legal_actualizado": "Päivitetty 8. lokakuuta 2026",

    # --- Privacidad ---------------------------------------------------------
    "privacidad_titulo": "Tietosuoja",
    "privacidad_entrada": "Rackers tehtiin pelaamista varten, ei tiedon keräämistä. "
                          "Tässä sanotaan suoraan, mitä tallennetaan, minne ja miten "
                          "sen poistaa.",
    "privacidad_secciones": [
        ("Ilman tiliä mikään ei lähde iPhonesta", [
            "Voit käyttää koko Rackersia luomatta tiliä. Ottelut, turnaukset ja "
            "asetukset jäävät laitteeseesi eivätkä matkusta minnekään.",
            "Tiliä tarvitaan kolmeen asiaan: että iPhonella ja kellolla on sama tieto, "
            "ettet menetä mitään puhelinta vaihtaessasi ja että voit pelata kavereiden "
            "kanssa.",
        ]),
        ("Mitä tili tallentaa", [
            "Tili luodaan Kirjaudu Applella -toiminnolla. Apple antaa meille pysyvän "
            "tunnisteen, nimesi ja sähköpostiosoitteen, joka on Applen yksityinen "
            "välitysosoite, jos päätät piilottaa omasi.",
            "Tallennamme tuon tunnisteen, sähköpostin, näyttämäsi nimen ja valitsemasi "
            "@nimen. Lisäksi Applen antaman luvan, jolla pääsy voidaan perua, kun "
            "poistat tilin.",
        ]),
        ("Varmuuskopio", [
            "Kun tili on käytössä, sovellus lataa sisältönsä palvelimelle: pelaajat, "
            "pelipäivät, ottelut, turnaukset, analyysit ja asetukset.",
            "Otteluissa on mukana se, mitä kello mittasi pelin aikana: syke, matka ja "
            "energia. Se kulkee ottelun mukana, koska se kuuluu otteluun.",
        ]),
        ("Se mikä ei lähde iPhonestasi", [
            "Leposyke, vaihtelu ja uni — se, mistä «Kuntosi tänään» kertoo — luetaan "
            "Terveys-apista ja jäävät laitteeseen. Niitä ei ladata palvelimelle eikä "
            "jaeta kenellekään.",
            "Terveys-luvan voi perua milloin tahansa kohdasta Asetukset › Terveys › "
            "Datan käyttöoikeus, eikä sovellus lakkaa toimimasta.",
        ]),
        ("Tekoälyvalmentaja", [
            "Kun pyydät analyysin, sovellus poimii videosta yksittäisiä kuvia ja "
            "lähettää ne OpenAI:lle palvelimemme kautta, joka palauttaa raportin.",
            "Koko videosta ei tallenneta mitään palvelimelle. Raportti palaa sovellukseen ja jää sinun kopioosi, samoin muutama äänetön sekunti jokaisesta parannettavasta asiasta, jotta näet ne myös toisella iPhonella. Ne poistetaan, kun poistat analyysin tai tilin.",
            "Sen sijaan jää merkintä siitä, montako analyysia olet pyytänyt, mistä "
            "lajista ja kuinka suuria ne olivat. Sitä tarvitaan käyttörajoihin ja "
            "kulujen seurantaan.",
        ]),
        ("Tilaus", [
            "Pro veloitetaan App Storen kautta. Emme näe emmekä tallenna korttiasi tai "
            "maksutietojasi missään vaiheessa.",
            "Käytämme RevenueCatia tietääksemme, onko tilauksesi voimassa — tilisi "
            "tunnisteella ja ei muulla.",
        ]),
        ("Kaverit ja perhe", [
            "Jos linkität itsesi johonkuhun, tallennetaan se, että olette linkitetty, "
            "ja jaetut ottelut.",
            "@nimesi on se, jolla muut löytävät sinut. Voit vaihtaa sen milloin "
            "tahansa.",
        ]),
        ("Turnaukset", [
            "Jos julkaiset turnauksen, tallennamme sen nimen, lajin, muodon, päivämäärän, kentän ja järjestäjän nimen. Kaavio ja tulokset pysyvät iPhonessasi ja varmuuskopiossasi.",
            "Julkisen turnauksen näkee kuka tahansa kohdassa Turnaukset › Julkiset ja sen rackers.app-linkistä, myös ilman tiliä. Yksityiseen pääsee vain se, jolla on koodi tai linkki.",
            "Jos ilmoittaudut tililläsi, järjestäjä näkee nimen, jolla ilmoittauduit, ja saa ilmoituksen iPhoneensa. Voit perua ilmoittautumisen milloin haluat, ja jonkun estäminen poistaa ilmoittautumiset välillänne.",
        ]),
        ("Missä se säilytetään", [
            "Cloudflaressa, D1-tietokannassa. Palvelin vastaa vain sovellukselle ja "
            "tallentaa sen, mitä sovellus sille lähettää.",
            "Valmentajan videosekunnit ovat Cloudflare R2:ssa. Sekä tietokanta että videot ovat Euroopan unionissa.",
        ]),
        ("Ei mainoksia eikä seurantaa", [
            "Mainoksia ei ole. Ei seurantaa sovellusten tai sivustojen välillä. Mitään "
            "ei myydä eikä luovuteta kolmansille heidän omaan käyttöönsä.",
        ]),
        ("Miten poistat kaiken", [
            "Sovelluksesta: Asetukset › Tili › Poista tili. Kaikki sinun tietosi "
            "poistuvat palvelimelta ja Applella antamasi pääsy perutaan.",
            "Se mikä on vain laitteessa katoaa, kun poistat sovelluksen.",
        ]),
        ("Alaikäiset", [
            "Rackersia ei ole tarkoitettu alle 13-vuotiaille emmekä tietoisesti pyydä "
            "heiltä tietoja.",
        ]),
        ("Kuka tästä vastaa", [
            "Näiden tietojen käsittelystä vastaa {responsable}, joka toimii "
            "itsenäisenä ammatinharjoittajana ja julkaisee Rackersin omissa nimissään. "
            "Kaikissa tietojasi koskevissa asioissa kirjoita osoitteeseen {correo}.",
            "Sinulla on oikeus nähdä omat tietosi, korjata ne, poistaa ne, siirtää ne "
            "muualle ja vastustaa käsittelyä. Nopeinta on poistaa tili sovelluksesta, "
            "mutta jos haluat pyytää kirjallisesti, kirjoita ja se hoidetaan.",
        ]),
        ("Muutokset", [
            "Jos tämä muuttuu, siitä kerrotaan tällä samalla sivulla, päiväys ylhäällä.",
        ]),
    ],

    # --- Condiciones --------------------------------------------------------
    "condiciones_titulo": "Käyttöehdot",
    "condiciones_entrada": "Rackersin käytön säännöt, lyhyesti ja ilman pientä "
                           "präntättyä.",
    "condiciones_secciones": [
        ("Mikä tämä on", [
            "Rackers on tulostaulu ja ottelupäiväkirja padeliin, tennikseen, "
            "pickleballiin, squashiin, pöytätennikseen ja sulkapalloon, iPhonelle ja "
            "Apple Watchille.",
            "Käyttämällä sitä hyväksyt nämä ehdot. Jos et hyväksy, älä käytä sitä.",
        ]),
        ("Tilisi", [
            "Tili on sinun ja vastaat siitä, mitä sillä tehdään. @nimi ei saa esiintyä "
            "toisena eikä olla loukkaava; jos on, se voidaan ottaa pois.",
            'Loukkauksia, häirintää tai loukkaavaa sisältöä ei suvaita. Sovelluksessa voit estää tai ilmiantaa minkä tahansa tilin; ihminen käy ilmoitukset läpi 24 tunnin kuluessa, ja sääntöjä rikkova menettää tilinsä.',
        ]),
        ("Pro ja maksut", [
            "Rackers on ilmainen. Pro on tilaus, joka veloitetaan App Store -tililtäsi, "
            "kun vahvistat oston.",
            "Se uusiutuu itsestään, ellet peruuta sitä vähintään 24 tuntia ennen "
            "kauden päättymistä. Sitä hallitaan ja se peruutetaan laitteesi Asetukset › "
            "nimesi › Tilaukset.",
            "Palautukset antaa Apple, emme me, omien sääntöjensä mukaan.",
        ]),
        ("Perhetilaus", [
            "Perhetilaus antaa Pron maksajalle ja niille tileille, jotka hän kutsuu, "
            "sovelluksen ilmoittamaan rajaan asti. Maksaja voi poistaa kenet tahansa "
            "milloin tahansa.",
        ]),
        ("Valmentaja ei ole lääkäri", [
            "Valmentajan raportti ja se, mitä sovellus laskee Terveys-tiedoistasi, ovat "
            "suuntaa antavia. Ne eivät ole diagnoosi, hoito eivätkä ammattimainen "
            "lääketieteellinen tai urheilullinen neuvo.",
            "Jos olet huonovointinen tai terveytesi mietityttää, kysy ammattilaiselta.",
        ]),
        ("Palvelu", [
            "Teemme voitavamme, jotta kaikki toimii, mutta sovellus ja palvelin "
            "tarjotaan sellaisinaan, takaamatta keskeytymätöntä saatavuutta tai "
            "virheettömyyttä.",
            "Säilytä se mikä on sinulle tärkeää: varmuuskopio auttaa, mutta ei korvaa "
            "omia kopioitasi.",
        ]),
        ("Asiallinen käyttö", [
            "Palvelua ei saa yrittää murtaa, siitä ei saa kaivaa muiden tilien tietoja "
            "eikä sitä saa käyttää mihinkään laittomaan. Jos niin käy, tili voidaan "
            "sulkea.",
        ]),
        ("Muutokset", [
            "Nämä ehdot voivat muuttua. Muutokset julkaistaan täällä päiväyksineen, ja "
            "sovelluksen käytön jatkaminen on niiden hyväksymistä.",
        ]),
    ],

    # --- Soporte ------------------------------------------------------------
    "soporte_titulo": "Tuki",
    "soporte_entrada": "Eikö jokin toimi, vai tuliko parempi idea? Kirjoita, niin "
                       "vastaamme.",
    "soporte_correo_titulo": "Kirjoita meille",
    "soporte_correo_nota": "Vastaajana on ihminen. Jos kyse on virheestä, kerro mitä "
                           "teit, mitä odotit ja mitä tapahtui, ja mainitse mikä iPhone "
                           "ja mikä iOS-versio sinulla on: niin se korjaantuu nopeammin.",
    "soporte_secciones": [
        ("Tilin poistaminen", [
            "Sovelluksessa: Asetukset › Tili › Poista tili. Kaikki sinun tietosi "
            "poistuvat palvelimelta ja Apple-pääsy perutaan. Meille ei tarvitse "
            "kirjoittaa.",
        ]),
        ("Tilaus", [
            "Prota hallitaan ja se peruutetaan laitteesi Asetukset › nimesi › "
            "Tilaukset. Palautukset antaa Apple osoitteessa reportaproblem.apple.com.",
        ]),
        ("Kello ei näe otteluita", [
            "Kello ja iPhone päivittyvät toisistaan, kun ne ovat lähekkäin ja "
            "molemmissa on sovellus auki. Muuten avaa Rackers molemmissa ja odota "
            "hetki.",
            "Kello pärjää yksin: voit pitää pisteitä koko ottelun ilman iPhonea "
            "mukana, ne sopivat asiat jälkeenpäin.",
        ]),
        ("Terveys ja luvat", [
            "Sykkeen mittaamiseen tarvitaan lupa Terveydelle. Jos kielsit sen, sen "
            "antaa uudelleen kohdasta Asetukset › Terveys › Datan käyttöoikeus › "
            "Rackers.",
            "Syke mitataan harjoituksena, joten kello pysyy sovelluksessa pelin ajan.",
        ]),
        ("Valmentaja", [
            "Videoanalyysi on Prota ja sillä on käyttöraja päivässä ja kuukaudessa. Jos "
            "analyysi epäonnistuu, se ei kuluta rajaa.",
        ]),
    ],
}
