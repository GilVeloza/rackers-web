"""Privacy, Terms and Support in en-US."""

TEXTO = {
    "legal_volver": "Back to the home page",
    "legal_actualizado": "Updated September 27, 2026",

    "privacidad_titulo": "Privacy",
    "privacidad_entrada": "Rackers was made for playing, not for collecting data. "
                          "Here is exactly what is stored, where, and how to delete it.",
    "privacidad_secciones": [
        ("Without an account, nothing leaves your iPhone", [
            "You can use all of Rackers without creating an account. Your matches, "
            "tournaments and settings stay on your device and go nowhere.",
            "An account does three things: keeps your iPhone and watch in step, saves "
            "everything when you change phones, and lets you play with friends.",
        ]),
        ("What the account stores", [
            "The account is created with Sign in with Apple. Apple gives us a stable "
            "identifier, your name and an email, which will be Apple's private relay "
            "address if you choose to hide yours.",
            "We store that identifier, the email, the name you show and the @name you "
            "pick. Also the permission Apple gives us so access can be revoked when "
            "you delete your account.",
        ]),
        ("The backup", [
            "With an account, the app uploads its contents: players, sessions, "
            "matches, tournaments, analyses and settings.",
            "Matches carry what the watch measured while you played: heart rate, "
            "distance and energy. It travels with the match because it belongs to it.",
        ]),
        ("What never leaves your iPhone", [
            "Resting heart rate, variability and sleep — what you see in How you "
            "arrive today — are read from the Health app and stay on your device. "
            "They are not uploaded and not shared with anyone.",
            "You can withdraw Health access whenever you like in Settings › Health "
            "› Data Access, and the app keeps working.",
        ]),
        ("The AI coach", [
            "When you ask for an analysis, the app takes frames from the video and "
            "sends them to OpenAI through our server, which returns the report.",
            "Nothing from the video is stored on the server. The report comes back to "
            "the app and stays in your own copy.",
            "What does remain is a record of how many analyses you asked for, for "
            "which sport and how large they were. That is for the usage limits and to "
            "know what it costs.",
        ]),
        ("The subscription", [
            "Pro is billed through the App Store. We never see or store your card or "
            "your payment details.",
            "We use RevenueCat to know whether your subscription is current, with your "
            "account identifier and nothing else.",
        ]),
        ("Friends and family", [
            "If you link up with someone, we store that you are linked and the matches "
            "you share.",
            "Your @name is how others find you. You can change it whenever you like.",
        ]),
        ("Tournaments", [
            "If you publish a tournament, we store its name, sport, format, date, venue and the organizer's name. The draw and the results stay on your iPhone and in your backup.",
            "Anyone can see a public tournament in Tournaments › Public and at its rackers.app link, even without an account. Only people with its code or its link can reach a private one.",
            "If you sign up from your account, the organizer sees the name you signed up with and gets a notification on their iPhone. You can leave whenever you want, and blocking someone removes any sign-ups between the two of you.",
        ]),
        ("Where it is stored", [
            "On Cloudflare, in a D1 database. The server only answers the app and only "
            "keeps what the app sends it.",
        ]),
        ("No ads, no tracking", [
            "There is no advertising. There is no tracking across apps or websites. "
            "Nothing is sold or handed to third parties for their own use.",
        ]),
        ("How to delete everything", [
            "In the app: Settings › Account › Delete account. Everything of "
            "yours is deleted from the server and the access you granted with Apple is "
            "revoked.",
            "Anything that only lives on the device goes when you delete the app.",
        ]),
        ("Children", [
            "Rackers is not intended for children under 13 and we do not knowingly "
            "collect their data.",
        ]),
        ("Who is responsible", [
            "The person responsible for handling this data is {responsable}, who is "
            "self-employed and publishes Rackers under his own name. For anything "
            "about your data, write to {correo}.",
            "You have the right to see your data, correct it, delete it, take it "
            "elsewhere and object to it being handled. The quickest way is to delete "
            "your account in the app, but if you would rather ask in writing, write "
            "and it will be done.",
        ]),
        ("Changes", [
            "If any of this changes, it will be posted on this page with the date at "
            "the top.",
        ]),
    ],

    "condiciones_titulo": "Terms of use",
    "condiciones_entrada": "The rules for using Rackers, short and without fine print.",
    "condiciones_secciones": [
        ("What this is", [
            "Rackers is a scoreboard and a match notebook for padel, tennis, "
            "pickleball, squash, table tennis and badminton, for iPhone and Apple "
            "Watch.",
            "By using it you accept these terms. If you do not accept them, do not use "
            "it.",
        ]),
        ("Your account", [
            "The account is yours and you answer for what is done with it. Your @name "
            "may not impersonate anyone or be offensive; if it is, it can be taken "
            "away.",
            'Insults, harassment and offensive content are not tolerated. You can block or report any account from the app; a person reviews reports within 24 hours, and anyone who breaks these rules loses their account.',
        ]),
        ("Pro and payments", [
            "Rackers is free. Pro is a subscription billed to your App Store account "
            "when you confirm the purchase.",
            "It renews by itself unless you cancel at least 24 hours before the period "
            "ends. Manage and cancel it in your device Settings › your name › "
            "Subscriptions.",
            "Refunds are granted by Apple, not by us, under their own rules.",
        ]),
        ("The family plan", [
            "The family plan gives Pro to whoever pays for it and to the accounts they "
            "invite, up to the limit the app states. The payer can remove anyone at "
            "any time.",
        ]),
        ("The coach is not a doctor", [
            "The coach report and anything the app works out from your Health data are "
            "there to guide you. They are not a diagnosis, a treatment, or medical or "
            "professional sports advice.",
            "If you feel unwell or have health concerns, ask a professional.",
        ]),
        ("The service", [
            "We do our best to keep everything working, but the app and the server are "
            "offered as they are, with no guarantee of uninterrupted availability or "
            "of being free of faults.",
            "Keep what matters to you: the backup helps, but it does not replace your "
            "own copies.",
        ]),
        ("Proper use", [
            "You may not try to break the service, pull data from other accounts out "
            "of it, or use it for anything unlawful. If that happens, the account can "
            "be closed.",
        ]),
        ("Changes", [
            "These terms may change. Changes are published here with their date, and "
            "carrying on using the app means accepting them.",
        ]),
    ],

    "soporte_titulo": "Support",
    "soporte_entrada": "Something not working, or an idea to make it better? Write to "
                       "us and we will answer.",
    "soporte_correo_titulo": "Write to us",
    "soporte_correo_nota": "A person answers. If it is a bug, tell us what you were "
                           "doing, what you expected and what happened, and say which "
                           "iPhone and which version of iOS you have: it gets fixed "
                           "sooner that way.",
    "soporte_secciones": [
        ("Deleting your account", [
            "In the app: Settings › Account › Delete account. Everything of "
            "yours is deleted from the server and Apple access is revoked. You do not "
            "need to write to us.",
        ]),
        ("The subscription", [
            "Pro is managed and cancelled in your device Settings › your name "
            "› Subscriptions. Refunds are granted by Apple at "
            "reportaproblem.apple.com.",
        ]),
        ("The watch cannot see the matches", [
            "The watch and the iPhone catch up when they are near each other and both "
            "have the app open. If not, open Rackers on both and wait a few seconds.",
            "The watch works on its own: you can score a whole match without the "
            "iPhone nearby and they will sort themselves out later.",
        ]),
        ("Health and permissions", [
            "Measuring heart rate needs Health access. If you said no, you can grant "
            "it again in Settings › Health › Data Access › Rackers.",
            "Heart rate is measured with a workout, so the watch stays in the app "
            "while you play.",
        ]),
        ("The coach", [
            "Video analysis is a Pro feature and has a limit per day and per month. If "
            "an analysis fails, it does not count against you.",
        ]),
    ],
}
