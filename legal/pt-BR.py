"""Privacidade, Termos e Suporte em pt-BR."""

TEXTO = {
    "legal_volver": "Voltar para a página inicial",
    "legal_actualizado": "Atualizado em 27 de setembro de 2026",

    "privacidad_titulo": "Privacidade",
    "privacidad_entrada": "O Rackers foi feito para jogar, não para coletar dados. Aqui "
                          "está claro o que é guardado, onde e como apagar.",
    "privacidad_secciones": [
        ("Sem conta, nada sai do seu iPhone", [
            "Você pode usar o Rackers inteiro sem criar conta. Suas partidas, torneios e "
            "ajustes ficam no aparelho e não vão a lugar nenhum.",
            "A conta serve para três coisas: manter iPhone e relógio iguais, não perder "
            "nada ao trocar de celular e jogar com amigos.",
        ]),
        ("O que a conta guarda", [
            "A conta é criada com Login com a Apple. A Apple nos dá um identificador "
            "estável, seu nome e um e-mail, que será o de encaminhamento privado da Apple "
            "se você esconder o seu.",
            "Guardamos esse identificador, o e-mail, o nome que você mostra e o @nome que "
            "escolher. E a permissão que a Apple dá para poder revogar o acesso quando "
            "você apaga a conta.",
        ]),
        ("O backup", [
            "Com a conta, o app envia o conteúdo dele: jogadores, rodadas, partidas, "
            "torneios, análises e ajustes.",
            "As partidas levam o que o relógio mediu enquanto você jogava: batimentos, "
            "distância e energia. Vai junto com a partida porque é da partida.",
        ]),
        ("O que nunca sai do seu iPhone", [
            "Batimentos em repouso, variabilidade e sono — o de « Como você chega hoje » "
            "— são lidos do app Saúde e ficam no aparelho. Não são enviados nem "
            "compartilhados com ninguém.",
            "A permissão da Saúde pode ser retirada quando quiser em Ajustes › Saúde › "
            "Acesso a dados, e o app continua funcionando.",
        ]),
        ("O treinador com IA", [
            "Quando você pede uma análise, o app tira quadros do vídeo e manda para a "
            "OpenAI pelo nosso servidor, que devolve o relatório.",
            "Do vídeo não se guarda nada no servidor. O relatório volta para o app e fica "
            "no seu backup.",
            "O que fica é o registro de quantas análises você pediu, de qual esporte e de "
            "que tamanho. Serve para os limites de uso e para saber o custo.",
        ]),
        ("A assinatura", [
            "O Pro é cobrado pela App Store. Nunca vemos nem guardamos seu cartão ou seus "
            "dados de pagamento.",
            "Usamos o RevenueCat para saber se sua assinatura está em dia, com o "
            "identificador da sua conta e mais nada.",
        ]),
        ("Amigos e família", [
            "Se você se conectar com alguém, guardamos que vocês estão conectados e as "
            "partidas que compartilham.",
            "Seu @nome é como os outros te encontram. Dá para mudar quando quiser.",
        ]),
        ("Torneios", [
            "Se você publica um torneio, guardamos o nome, o esporte, o formato, a data, a quadra e o nome de quem organiza. A chave e os resultados ficam no seu iPhone e no seu backup.",
            "Um torneio público pode ser visto por qualquer pessoa em Torneios › Públicos e no link dele em rackers.app, mesmo sem conta. A um privado só chega quem tem o código ou o link.",
            "Se você se inscreve pela sua conta, quem organiza vê o nome com que você se inscreveu e recebe uma notificação no iPhone. Você pode sair quando quiser, e bloquear alguém desfaz as inscrições entre vocês dois.",
        ]),
        ("Onde fica guardado", [
            "Na Cloudflare, num banco de dados D1. O servidor só responde ao app e só "
            "guarda o que o app manda.",
        ]),
        ("Sem anúncios e sem rastreamento", [
            "Não há publicidade. Não há rastreamento entre apps ou sites. Nada é vendido "
            "nem cedido a terceiros para uso próprio deles.",
        ]),
        ("Como apagar tudo", [
            "No app: Ajustes › Conta › Apagar conta. Tudo o que é seu é apagado do "
            "servidor e o acesso dado com a Apple é revogado.",
            "O que estiver só no aparelho some ao apagar o app.",
        ]),
        ("Menores", [
            "O Rackers não é feito para menores de 13 anos e não coletamos dados deles "
            "conscientemente.",
        ]),
        ("Quem responde por isso", [
            "Pelo tratamento desses dados responde {responsable}, que trabalha por conta "
            "própria e publica o Rackers em seu próprio nome. Para qualquer coisa sobre "
            "seus dados, escreva para {correo}.",
            "Você tem direito a ver o que é seu, corrigir, apagar, levar para outro lugar "
            "e se opor ao tratamento. O mais rápido é apagar a conta pelo app, mas se "
            "preferir pedir por escrito, escreva e será feito.",
        ]),
        ("Mudanças", [
            "Se isso mudar, será avisado nesta mesma página com a data em cima.",
        ]),
    ],

    "condiciones_titulo": "Termos de uso",
    "condiciones_entrada": "As regras para usar o Rackers, curtas e sem letra miúda.",
    "condiciones_secciones": [
        ("O que é isto", [
            "O Rackers é um placar e um caderno de partidas para padel, tênis, "
            "pickleball, squash, tênis de mesa e badminton, para iPhone e Apple Watch.",
            "Ao usá-lo você aceita estes termos. Se não aceita, não use.",
        ]),
        ("Sua conta", [
            "A conta é sua e você responde pelo que for feito com ela. O @nome não pode "
            "se passar por ninguém nem ser ofensivo; se for, pode ser retirado.",
            'Não toleramos insultos, assédio nem conteúdo ofensivo. Pelo app você pode bloquear ou denunciar qualquer conta; uma pessoa analisa as denúncias em menos de 24 horas, e quem descumprir estas regras perde a conta.',
        ]),
        ("Pro e os pagamentos", [
            "O Rackers é grátis. O Pro é uma assinatura cobrada na sua conta da App Store "
            "ao confirmar a compra.",
            "Renova sozinha a menos que você cancele pelo menos 24 horas antes do fim do "
            "período. Gerencia e cancela em Ajustes do aparelho › seu nome › Assinaturas.",
            "Os reembolsos são dados pela Apple, não por nós, segundo as regras dela.",
        ]),
        ("O plano família", [
            "O plano família dá Pro a quem paga e às contas que convidar, até o limite que "
            "o app indicar. Quem paga pode tirar qualquer um quando quiser.",
        ]),
        ("O treinador não é médico", [
            "O relatório do treinador e o que o app calcula com seus dados de Saúde são "
            "orientativos. Não são diagnóstico, nem tratamento, nem conselho médico ou "
            "esportivo profissional.",
            "Se estiver se sentindo mal ou tiver dúvidas de saúde, procure um "
            "profissional.",
        ]),
        ("O serviço", [
            "Fazemos o possível para que tudo funcione, mas o app e o servidor são "
            "oferecidos como estão, sem garantia de disponibilidade sem interrupção nem de "
            "ausência de falhas.",
            "Guarde o que importa para você: o backup ajuda, mas não substitui suas "
            "próprias cópias.",
        ]),
        ("Uso correto", [
            "Não se pode tentar quebrar o serviço, tirar dele dados de outras contas ou "
            "usá-lo para algo ilegal. Se acontecer, a conta pode ser encerrada.",
        ]),
        ("Mudanças", [
            "Estes termos podem mudar. As mudanças são publicadas aqui com a data, e "
            "continuar usando o app é aceitá-las.",
        ]),
    ],

    "soporte_titulo": "Suporte",
    "soporte_entrada": "Algo não funciona, ou você teve uma ideia melhor? Escreva que a "
                       "gente responde.",
    "soporte_correo_titulo": "Escreva para nós",
    "soporte_correo_nota": "Responde uma pessoa. Se for um erro, conte o que estava "
                           "fazendo, o que esperava e o que aconteceu, e diga qual iPhone e "
                           "qual versão do iOS você tem: assim conserta antes.",
    "soporte_secciones": [
        ("Apagar sua conta", [
            "No app: Ajustes › Conta › Apagar conta. Tudo o que é seu é apagado do "
            "servidor e o acesso da Apple é revogado. Não precisa escrever para a gente.",
        ]),
        ("A assinatura", [
            "O Pro se gerencia e se cancela em Ajustes do aparelho › seu nome › "
            "Assinaturas. Os reembolsos são dados pela Apple em reportaproblem.apple.com.",
        ]),
        ("O relógio não vê as partidas", [
            "O relógio e o iPhone se atualizam quando estão perto e os dois estão com o "
            "app aberto. Se não, abra o Rackers nos dois e espere alguns segundos.",
            "O relógio funciona sozinho: dá para marcar uma partida inteira sem o iPhone "
            "por perto, e depois eles se acertam.",
        ]),
        ("Saúde e permissões", [
            "Para medir os batimentos é preciso dar permissão à Saúde. Se você negou, dá "
            "de novo em Ajustes › Saúde › Acesso a dados › Rackers.",
            "Os batimentos são medidos com um treino, então o relógio fica no app "
            "enquanto você joga.",
        ]),
        ("O treinador", [
            "A análise de vídeo é Pro e tem um limite por dia e por mês. Se uma análise "
            "falhar, não conta.",
        ]),
    ],
}
