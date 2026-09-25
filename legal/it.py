"""Privacy, Condizioni e Assistenza in italiano."""

TEXTO = {
    "legal_volver": "Torna alla home",
    "legal_actualizado": "Aggiornato il 25 settembre 2026",

    "privacidad_titulo": "Privacy",
    "privacidad_entrada": "Rackers è fatta per giocare, non per raccogliere dati. Qui c'è "
                          "scritto chiaro cosa si salva, dove e come cancellarlo.",
    "privacidad_secciones": [
        ("Senza account non esce nulla dall'iPhone", [
            "Puoi usare tutta Rackers senza creare un account. Le partite, i tornei e le "
            "impostazioni restano sul dispositivo e non vanno da nessuna parte.",
            "L'account serve per tre cose: avere le stesse cose su iPhone e orologio, non "
            "perdere niente cambiando telefono e giocare con gli amici.",
        ]),
        ("Cosa salva l'account", [
            "L'account si crea con Accedi con Apple. Apple ci dà un identificativo stabile, "
            "il tuo nome e un'email, che sarà l'indirizzo di inoltro privato di Apple se "
            "scegli di nascondere il tuo.",
            "Conserviamo quell'identificativo, l'email, il nome che mostri e il @nome che "
            "scegli. Più il permesso che dà Apple per poter revocare l'accesso quando "
            "cancelli l'account.",
        ]),
        ("La copia di sicurezza", [
            "Con l'account, l'app carica il suo contenuto: giocatori, giornate, partite, "
            "tornei, analisi e impostazioni.",
            "Le partite portano con sé quello che ha misurato l'orologio mentre giocavi: "
            "battito, distanza ed energia. Viaggia con la partita perché è della partita.",
        ]),
        ("Cosa non esce mai dal tuo iPhone", [
            "Battito a riposo, variabilità e sonno — quello di « Come arrivi oggi » — si "
            "leggono dall'app Salute e restano sul dispositivo. Non vengono caricati né "
            "condivisi con nessuno.",
            "Il permesso di Salute si può togliere quando vuoi da Impostazioni › Salute › "
            "Accesso ai dati, e l'app continua a funzionare.",
        ]),
        ("L'allenatore con IA", [
            "Quando chiedi un'analisi, l'app estrae fotogrammi dal video e li manda a "
            "OpenAI attraverso il nostro server, che restituisce il referto.",
            "Del video non si salva nulla sul server. Il referto torna all'app e resta "
            "nella tua copia.",
            "Resta invece il conto di quante analisi hai chiesto, per quale sport e quanto "
            "erano grandi. Serve per i limiti d'uso e per sapere quanto costa.",
        ]),
        ("L'abbonamento", [
            "Pro si paga tramite App Store. Non vediamo né salviamo mai la tua carta o i "
            "tuoi dati di pagamento.",
            "Usiamo RevenueCat per sapere se il tuo abbonamento è attivo, con "
            "l'identificativo del tuo account e nient'altro.",
        ]),
        ("Amici e famiglia", [
            "Se ti colleghi con qualcuno, si salva che siete collegati e le partite che "
            "condividete.",
            "Il tuo @nome è come ti trovano gli altri. Puoi cambiarlo quando vuoi.",
        ]),
        ("Dove si salva", [
            "Su Cloudflare, in un database D1. Il server risponde solo all'app e tiene "
            "solo quello che l'app gli manda.",
        ]),
        ("Niente pubblicità né tracciamento", [
            "Non c'è pubblicità. Non c'è tracciamento tra app o siti. Non si vende né si "
            "cede nulla a terzi per un loro uso.",
        ]),
        ("Come cancellare tutto", [
            "Nell'app: Impostazioni › Account › Elimina account. Si cancella tutto il tuo "
            "dal server e si revoca l'accesso dato con Apple.",
            "Quello che sta solo sul dispositivo se ne va cancellando l'app.",
        ]),
        ("Minori", [
            "Rackers non è pensata per minori di 13 anni e non raccogliamo "
            "consapevolmente i loro dati.",
        ]),
        ("Chi ne risponde", [
            "Del trattamento di questi dati risponde {responsable}, lavoratore autonomo, "
            "che pubblica Rackers a proprio nome. Per qualsiasi cosa riguardi i tuoi dati, "
            "scrivi a {correo}.",
            "Hai diritto a vedere i tuoi dati, correggerli, cancellarli, portarli altrove "
            "e opporti al trattamento. La via più rapida è eliminare l'account dall'app, "
            "ma se preferisci chiederlo per iscritto, scrivi e si fa.",
        ]),
        ("Modifiche", [
            "Se qualcosa cambia, lo trovi su questa stessa pagina con la data in alto.",
        ]),
    ],

    "condiciones_titulo": "Condizioni d'uso",
    "condiciones_entrada": "Le regole per usare Rackers, in breve e senza righe in piccolo.",
    "condiciones_secciones": [
        ("Di cosa si tratta", [
            "Rackers è un segnapunti e un quaderno di partite per padel, tennis, "
            "pickleball, squash, tennistavolo e badminton, per iPhone e Apple Watch.",
            "Usandola accetti queste condizioni. Se non le accetti, non usarla.",
        ]),
        ("Il tuo account", [
            "L'account è tuo e rispondi di quello che ci si fa. Il @nome non può fingersi "
            "qualcun altro né essere offensivo; se lo è, può essere tolto.",
            "Insulti, molestie e contenuti offensivi non sono tollerati. Dall'app puoi bloccare o segnalare qualsiasi account; le segnalazioni le controlla una persona entro 24 ore, e chi non rispetta queste regole perde l'account.",
        ]),
        ("Pro e i pagamenti", [
            "Rackers è gratis. Pro è un abbonamento addebitato sul tuo account App Store "
            "alla conferma dell'acquisto.",
            "Si rinnova da solo salvo disdetta almeno 24 ore prima della fine del periodo. "
            "Si gestisce e si disdice in Impostazioni del dispositivo › il tuo nome › "
            "Abbonamenti.",
            "I rimborsi li dà Apple, non noi, secondo le sue regole.",
        ]),
        ("Il piano famiglia", [
            "Il piano famiglia dà Pro a chi paga e agli account che invita, fino al limite "
            "indicato dall'app. Chi paga può togliere chiunque quando vuole.",
        ]),
        ("L'allenatore non è un medico", [
            "Il referto dell'allenatore e quello che l'app calcola con i tuoi dati di "
            "Salute sono indicativi. Non sono una diagnosi, né una cura, né un consiglio "
            "medico o sportivo professionale.",
            "Se non ti senti bene o hai dubbi sulla salute, chiedi a un professionista.",
        ]),
        ("Il servizio", [
            "Facciamo il possibile perché tutto funzioni, ma l'app e il server si offrono "
            "così come sono, senza garanzia di disponibilità continua né di assenza di "
            "errori.",
            "Conserva quello che ti sta a cuore: la copia di sicurezza aiuta, ma non "
            "sostituisce le tue copie.",
        ]),
        ("Uso corretto", [
            "Non si può provare a rompere il servizio, tirarne fuori dati di altri account "
            "o usarlo per qualcosa di illecito. Se succede, l'account può essere chiuso.",
        ]),
        ("Modifiche", [
            "Queste condizioni possono cambiare. Le modifiche si pubblicano qui con la "
            "loro data, e continuare a usare l'app significa accettarle.",
        ]),
    ],

    "soporte_titulo": "Assistenza",
    "soporte_entrada": "Qualcosa non va, o ti viene in mente qualcosa di meglio? Scrivi e ti "
                       "rispondiamo.",
    "soporte_correo_titulo": "Scrivici",
    "soporte_correo_nota": "Risponde una persona. Se è un errore, racconta cosa stavi "
                           "facendo, cosa ti aspettavi e cosa è successo, e dicci che iPhone "
                           "e che versione di iOS hai: così si sistema prima.",
    "soporte_secciones": [
        ("Eliminare l'account", [
            "Nell'app: Impostazioni › Account › Elimina account. Si cancella tutto il tuo "
            "dal server e si revoca l'accesso Apple. Non serve scriverci.",
        ]),
        ("L'abbonamento", [
            "Pro si gestisce e si disdice da Impostazioni del dispositivo › il tuo nome › "
            "Abbonamenti. I rimborsi li dà Apple da reportaproblem.apple.com.",
        ]),
        ("L'orologio non vede le partite", [
            "Orologio e iPhone si aggiornano quando sono vicini e su entrambi l'app è "
            "aperta. Altrimenti apri Rackers su tutti e due e aspetta qualche secondo.",
            "L'orologio funziona da solo: puoi segnare una partita intera senza l'iPhone "
            "vicino, poi si mettono d'accordo.",
        ]),
        ("Salute e permessi", [
            "Per misurare il battito serve il permesso di Salute. Se hai detto di no, si "
            "ridà da Impostazioni › Salute › Accesso ai dati › Rackers.",
            "Il battito si misura con un allenamento, quindi l'orologio resta nell'app "
            "mentre giochi.",
        ]),
        ("L'allenatore", [
            "L'analisi video è Pro e ha un limite al giorno e al mese. Se un'analisi "
            "fallisce, non ti viene contata.",
        ]),
    ],
}
