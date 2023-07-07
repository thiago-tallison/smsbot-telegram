import random
import datetime

messages = [
    """Se puder votar nesta proposta que solicita o aumento de cargos da PRF, vai me ajudar demais! Seu voto levará no máximo 1 minuto, mas poderá mudar a vida de muitas pessoas que aguardam a convocação no concurso da PRF. Ahh... lembrando que, caso aprovada, a proposta favorece um novo concurso em breve! 👊🏻🇧🇷

🚨 Quem quiser ajudar ainda mais, pode divulgar no Instagram e marcar @aprovadosprf.2021
Assim conseguimos alcançar mais pessoas.

✅Pronto, tudo certo! Agradeço imensamente ❤️

https://brasilparticipativo.presidencia.gov.br/processes/programas/f/2/proposals/3533

Obs: Não é vírus, pode notar que a URL é do domínio .gov.br. Agradeço desde já! 🙏""",
    """Olá! Se você puder dar seu apoio a esta proposta que busca o aumento de cargos da PRF, será de grande ajuda para mim! Seu voto só levará 1 minuto no máximo, mas pode mudar a vida de muitas pessoas que estão esperando ser convocadas no concurso da PRF. Ah, e se a proposta for aprovada, abrirá caminho para um novo concurso em breve! 👊🏻🇧🇷
🚨 Se quiser ajudar ainda mais, pode compartilhar no Instagram e marcar @aprovadosprf.2021. Assim, poderemos alcançar mais pessoas.

✅ Pronto, tudo certo! Agradeço imensamente ❤️

https://brasilparticipativo.presidencia.gov.br/processes/programas/f/2/proposals/3533

Obs: Não se preocupe, não é um vírus. A URL é do domínio .gov.br. Agradeço antecipadamente! 🙏""",
    """Sua colaboração é muito importante! Se puder votar nesta proposta que busca o aumento de cargos da PRF, estará me ajudando imensamente! Apenas um minuto do seu tempo pode fazer a diferença na vida de muitas pessoas que aguardam ansiosamente pela convocação no concurso da PRF. Vale ressaltar que, se aprovada, a proposta abrirá caminho para um novo concurso em breve! 👊🏻🇧🇷
🚨 Se quiser contribuir ainda mais, compartilhe no Instagram e marque @aprovadosprf.2021. Assim, poderemos alcançar um número maior de pessoas.

✅ Pronto, está tudo certo! Agradeço de coração ❤️

https://brasilparticipativo.presidencia.gov.br/processes/programas/f/2/proposals/3533

Obs: Não é um vírus, você pode perceber que a URL pertence ao domínio .gov.br. Agradeço antecipadamente! 🙏""",
    """Se você puder votar nesta proposta que busca o aumento de cargos da PRF, estará me fazendo um grande favor! Seu voto levará apenas 1 minuto, mas pode mudar a vida de muitas pessoas que aguardam ansiosamente a convocação no concurso da PRF. Ah, e se a proposta for aprovada, haverá a possibilidade de um novo concurso em breve! 👊🏻🇧🇷
🚨 Se quiser contribuir ainda mais, divulgue no Instagram e marque @aprovadosprf.2021. Assim, conseguiremos alcançar um número maior de pessoas.

✅ Tudo pronto! Agradeço imensamente ❤️

https://brasilparticipativo.presidencia.gov.br/processes/programas/f/2/proposals/3533

Obs: Não é um vírus, repare que a URL pertence ao domínio .gov.br. Desde já, agradeço! 🙏""",
    """Se você puder votar nesta proposta que solicita o aumento de cargos da PRF, estará me ajudando muito! Seu voto levará apenas 1 minuto, mas poderá fazer a diferença na vida de muitas pessoas que estão esperando ser convocadas no concurso da PRF. Ahh... lembrando que, se aprovada, a proposta abrirá portas para um novo concurso em breve! 👊🏻🇧🇷
🚨 Quem quiser contribuir ainda mais, pode divulgar no Instagram e marcar @aprovadosprf.2021. Assim, poderemos alcançar um público maior.

✅ Tudo certo! Agradeço de coração ❤️

https://brasilparticipativo.presidencia.gov.br/processes/programas/f/2/proposals/3533

Obs: Não é um vírus, pode perceber que a URL pertence ao domínio .gov.br. Agradeço desde já! 🙏""",
    """Se você puder votar nesta proposta que busca o aumento de cargos da PRF, estará me dando uma grande ajuda! Seu voto só levará 1 minuto, mas pode mudar a vida de muitas pessoas que estão aguardando a convocação no concurso da PRF. Ahh... lembrando que, se aprovada, a proposta favorecerá um novo concurso em breve! 👊🏻🇧🇷
🚨 Quem quiser colaborar ainda mais, pode compartilhar no Instagram e marcar @aprovadosprf.2021. Assim, conseguiremos alcançar mais pessoas.

✅ Tudo pronto! Agradeço imensamente ❤️

https://brasilparticipativo.presidencia.gov.br/processes/programas/f/2/proposals/3533

Obs: Não se preocupe, não é um vírus. A URL pertence ao domínio .gov.br. Agradeço antecipadamente! 🙏""",
    """Caso possa apoiar esta proposta que requer a ampliação dos cargos na PRF, será de extrema valia para mim! Seu voto exigirá apenas um minuto do seu tempo, mas poderá impactar positivamente a vida de diversas pessoas que anseiam pela convocação no concurso da PRF. Além disso, vale destacar que, se aprovada, a proposta possibilitará a realização de um novo concurso em breve! 👊🏻🇧🇷
🚨 Se desejar ajudar ainda mais, compartilhe no Instagram e mencione @aprovadosprf.2021. Assim, poderemos alcançar um maior número de pessoas.

✅ Tudo pronto! Agradeço imensamente ❤️

https://brasilparticipativo.presidencia.gov.br/processes/programas/f/2/proposals/3533

Obs: Não há motivo para preocupação, não se trata de um vírus. Observe que a URL pertence ao domínio .gov.br. Desde já, agradeço! 🙏""",
    """Caso possa manifestar seu apoio a esta proposta que reivindica o aumento de cargos na PRF, estará me prestando uma ajuda imensurável! Seu voto exigirá apenas um minuto do seu tempo, porém poderá alterar positivamente a vida de muitas pessoas que estão na expectativa de serem convocadas no concurso da PRF. Ah, e não se esqueça: se a proposta for aprovada, abrirá caminho para um novo concurso em breve! 👊🏻🇧🇷
🚨 Se desejar colaborar ainda mais, divulgue no Instagram e marque @aprovadosprf.2021. Dessa forma, poderemos alcançar um público maior.

✅ Está tudo certo! Agradeço de coração ❤️

https://brasilparticipativo.presidencia.gov.br/processes/programas/f/2/proposals/3533

Obs: Fique tranquilo, não se trata de um vírus. Repare que a URL pertence ao domínio .gov.br. Desde já, agradeço! 🙏""",
]


def should_init_with_greet():
    return random.choice([0, 1])


def get_greet_by_time():
    current_time = datetime.datetime.now().time()
    if current_time < datetime.time(12):
        return "Bom dia!"
    elif current_time < datetime.time(18):
        return "Boa tarde!"

    return "Boa noite!"


def get_random_message():
    random_message = random.choice(messages)

    greeting = get_greet_by_time() + " " if bool(should_init_with_greet()) else ""

    return greeting + random_message
