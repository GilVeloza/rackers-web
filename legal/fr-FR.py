"""Confidentialité, Conditions et Assistance en fr-FR."""

TEXTO = {
    "legal_volver": "Retour à l'accueil",
    "legal_actualizado": "Mis à jour le 8 octobre 2026",

    "privacidad_titulo": "Confidentialité",
    "privacidad_entrada": "Rackers est faite pour jouer, pas pour collecter des données. "
                          "Voici clairement ce qui est enregistré, où, et comment l'effacer.",
    "privacidad_secciones": [
        ("Sans compte, rien ne quitte ton iPhone", [
            "Tu peux utiliser tout Rackers sans créer de compte. Tes matchs, tes tournois "
            "et tes réglages restent sur ton appareil et ne partent nulle part.",
            "Le compte sert à trois choses : que l'iPhone et la montre aient la même "
            "chose, ne rien perdre en changeant de téléphone, et jouer avec des amis.",
        ]),
        ("Ce que le compte enregistre", [
            "Le compte se crée avec Se connecter avec Apple. Apple nous donne un "
            "identifiant stable, ton nom et une adresse e-mail, qui sera l'adresse relais "
            "privée d'Apple si tu choisis de masquer la tienne.",
            "Nous gardons cet identifiant, l'e-mail, le nom que tu affiches et le @nom que "
            "tu choisis. Ainsi que l'autorisation donnée par Apple pour pouvoir retirer "
            "l'accès quand tu supprimes ton compte.",
        ]),
        ("La sauvegarde", [
            "Avec un compte, l'app envoie son contenu : joueurs, journées, matchs, "
            "tournois, analyses et réglages.",
            "Les matchs contiennent ce que la montre a mesuré pendant que tu jouais : "
            "fréquence cardiaque, distance et énergie. Cela voyage avec le match parce que "
            "cela lui appartient.",
        ]),
        ("Ce qui ne quitte jamais ton iPhone", [
            "La fréquence cardiaque au repos, la variabilité et le sommeil — ce que montre "
            "« Comment tu arrives aujourd'hui » — sont lus dans l'app Santé et restent sur "
            "l'appareil. Rien n'est envoyé ni partagé avec qui que ce soit.",
            "Tu peux retirer l'accès à Santé quand tu veux dans Réglages › Santé › Accès "
            "aux données, sans que l'app cesse de fonctionner.",
        ]),
        ("L'entraîneur IA", [
            "Quand tu demandes une analyse, l'app extrait des images de la vidéo et les "
            "envoie à OpenAI via notre serveur, qui renvoie le rapport.",
            "Rien de la vidéo entière n'est conservé sur le serveur. Le rapport revient à l'app et reste dans ta sauvegarde, avec quelques secondes sans son de chaque point à améliorer, pour que tu les voies aussi sur un autre iPhone. Elles sont effacées quand tu supprimes l'analyse ou le compte.",
            "Ce qui reste, c'est le décompte des analyses demandées, pour quel sport et de "
            "quelle taille. Cela sert aux limites d'usage et à connaître le coût.",
        ]),
        ("L'abonnement", [
            "Pro est facturé via l'App Store. Nous ne voyons ni n'enregistrons jamais ta "
            "carte ni tes données de paiement.",
            "Nous utilisons RevenueCat pour savoir si ton abonnement est à jour, avec "
            "l'identifiant de ton compte et rien d'autre.",
        ]),
        ("Amis et famille", [
            "Si tu te lies à quelqu'un, on enregistre que vous êtes liés et les matchs que "
            "vous partagez.",
            "Ton @nom, c'est ainsi que les autres te trouvent. Tu peux le changer quand tu "
            "veux.",
        ]),
        ("Tournois", [
            "Si vous publiez un tournoi, nous enregistrons son nom, le sport, le format, la date, le lieu et le nom de l'organisateur. Le tableau et les résultats restent sur votre iPhone et dans votre sauvegarde.",
            "Un tournoi public est visible par tous dans Tournois › Publics et via son lien rackers.app, même sans compte. Un tournoi privé n'est accessible qu'avec son code ou son lien.",
            "Si vous vous inscrivez depuis votre compte, l'organisateur voit le nom sous lequel vous vous inscrivez et reçoit une notification sur son iPhone. Vous pouvez vous désinscrire quand vous voulez, et bloquer quelqu'un annule les inscriptions entre vous deux.",
        ]),
        ("Où c'est stocké", [
            "Chez Cloudflare, dans une base de données D1. Le serveur ne répond qu'à l'app "
            "et ne garde que ce que l'app lui envoie.",
            "Les secondes de vidéo de l'entraîneur sont chez Cloudflare R2. La base de données et les vidéos sont dans l'Union européenne.",
        ]),
        ("Ni publicité ni pistage", [
            "Il n'y a pas de publicité. Pas de pistage entre apps ou sites. Rien n'est "
            "vendu ni cédé à des tiers pour leur propre usage.",
        ]),
        ("Comment tout effacer", [
            "Dans l'app : Réglages › Compte › Supprimer le compte. Tout ce qui est à toi "
            "est effacé du serveur et l'accès accordé avec Apple est révoqué.",
            "Ce qui n'existe que sur l'appareil disparaît quand tu supprimes l'app.",
        ]),
        ("Mineurs", [
            "Rackers n'est pas destinée aux enfants de moins de 13 ans et nous ne "
            "collectons pas sciemment leurs données.",
        ]),
        ("Qui en est responsable", [
            "Le responsable du traitement de ces données est {responsable}, travailleur "
            "indépendant, qui publie Rackers en son nom propre. Pour tout ce qui concerne "
            "tes données, écris à {correo}.",
            "Tu as le droit de consulter tes données, les corriger, les effacer, les "
            "emporter ailleurs et t'opposer à leur traitement. Le plus rapide est de "
            "supprimer le compte depuis l'app, mais si tu préfères le demander par écrit, "
            "écris et ce sera fait.",
        ]),
        ("Modifications", [
            "Si tout cela change, ce sera publié sur cette page avec la date en haut.",
        ]),
    ],

    "condiciones_titulo": "Conditions d'utilisation",
    "condiciones_entrada": "Les règles d'utilisation de Rackers, courtes et sans petits caractères.",
    "condiciones_secciones": [
        ("De quoi il s'agit", [
            "Rackers est un tableau de score et un carnet de matchs pour le padel, le "
            "tennis, le pickleball, le squash, le tennis de table et le badminton, sur "
            "iPhone et Apple Watch.",
            "En l'utilisant, tu acceptes ces conditions. Si tu ne les acceptes pas, ne "
            "l'utilise pas.",
        ]),
        ("Ton compte", [
            "Le compte est à toi et tu réponds de ce qui en est fait. Le @nom ne peut "
            "usurper l'identité de personne ni être offensant ; le cas échéant, il peut "
            "être retiré.",
            "Les insultes, le harcèlement et les contenus offensants ne sont pas tolérés. Depuis l'app, vous pouvez bloquer ou signaler n'importe quel compte ; une personne examine les signalements sous 24 heures, et quiconque enfreint ces règles perd son compte.",
        ]),
        ("Pro et les paiements", [
            "Rackers est gratuite. Pro est un abonnement facturé sur ton compte App Store "
            "à la confirmation de l'achat.",
            "Il se renouvelle automatiquement sauf si tu l'annules au moins 24 heures "
            "avant la fin de la période. Il se gère et s'annule dans les Réglages de ton "
            "appareil › ton nom › Abonnements.",
            "Les remboursements sont accordés par Apple, pas par nous, selon ses propres "
            "règles.",
        ]),
        ("L'offre famille", [
            "L'offre famille donne Pro à la personne qui paie et aux comptes qu'elle "
            "invite, dans la limite indiquée par l'app. Celle qui paie peut retirer "
            "quelqu'un à tout moment.",
        ]),
        ("L'entraîneur n'est pas médecin", [
            "Le rapport de l'entraîneur et tout ce que l'app calcule à partir de tes "
            "données de Santé sont indicatifs. Ce n'est ni un diagnostic, ni un "
            "traitement, ni un conseil médical ou sportif professionnel.",
            "Si tu te sens mal ou si tu as des doutes sur ta santé, demande à un "
            "professionnel.",
        ]),
        ("Le service", [
            "Nous faisons de notre mieux pour que tout fonctionne, mais l'app et le "
            "serveur sont fournis tels quels, sans garantie de disponibilité continue ni "
            "d'absence de défauts.",
            "Garde ce qui compte pour toi : la sauvegarde aide, mais ne remplace pas tes "
            "propres copies.",
        ]),
        ("Usage correct", [
            "Il est interdit d'essayer de casser le service, d'en extraire les données "
            "d'autres comptes ou de l'utiliser à des fins illégales. Le cas échéant, le "
            "compte peut être fermé.",
        ]),
        ("Modifications", [
            "Ces conditions peuvent changer. Les modifications sont publiées ici avec leur "
            "date, et continuer à utiliser l'app vaut acceptation.",
        ]),
    ],

    "soporte_titulo": "Assistance",
    "soporte_entrada": "Quelque chose ne marche pas, ou tu as une meilleure idée ? Écris-nous "
                       "et on te répond.",
    "soporte_correo_titulo": "Écris-nous",
    "soporte_correo_nota": "C'est une personne qui répond. Si c'est un bug, raconte ce que tu "
                           "faisais, ce que tu attendais et ce qui s'est passé, et précise "
                           "quel iPhone et quelle version d'iOS tu as : ça se répare plus vite.",
    "soporte_secciones": [
        ("Supprimer ton compte", [
            "Dans l'app : Réglages › Compte › Supprimer le compte. Tout ce qui est à toi "
            "est effacé du serveur et l'accès Apple est révoqué. Pas besoin de nous écrire.",
        ]),
        ("L'abonnement", [
            "Pro se gère et s'annule dans les Réglages de ton appareil › ton nom › "
            "Abonnements. Les remboursements sont accordés par Apple sur "
            "reportaproblem.apple.com.",
        ]),
        ("La montre ne voit pas les matchs", [
            "La montre et l'iPhone se mettent à jour quand ils sont proches et que l'app "
            "est ouverte sur les deux. Sinon, ouvre Rackers sur les deux et attends "
            "quelques secondes.",
            "La montre fonctionne seule : tu peux compter les points d'un match entier "
            "sans l'iPhone à côté, ils se mettront d'accord plus tard.",
        ]),
        ("Santé et autorisations", [
            "Pour mesurer la fréquence cardiaque, il faut autoriser Santé. Si tu as "
            "refusé, tu peux l'autoriser à nouveau dans Réglages › Santé › Accès aux "
            "données › Rackers.",
            "La fréquence cardiaque se mesure avec un entraînement, la montre reste donc "
            "dans l'app pendant que tu joues.",
        ]),
        ("L'entraîneur", [
            "L'analyse vidéo fait partie de Pro et a une limite par jour et par mois. Si "
            "une analyse échoue, elle n'est pas comptée.",
        ]),
    ],
}
