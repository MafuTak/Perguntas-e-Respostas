import random

def quiz():
    perguntas = [
        {"pergunta": "Qual é a capital da França?", "opcoes": ["a) Paris", "b) Londres", "c) Roma", "d) Madri"],
         "correta": "a"},
        {"pergunta": "Qual o maior planeta do sistema solar?",
         "opcoes": ["a) Terra", "b) Júpiter", "c) Marte", "d) Vênus"], "correta": "b"},
        {"pergunta": "Quem pintou a Mona Lisa?",
         "opcoes": ["a) Van Gogh", "b) Da Vinci", "c) Picasso", "d) Michelangelo"], "correta": "b"},
        {"pergunta": "Quantos estados tem o Brasil?", "opcoes": ["a) 25", "b) 26", "c) 27", "d) 28"], "correta": "c"},
        {"pergunta": "Em que ano o homem pisou na Lua?", "opcoes": ["a) 1965", "b) 1969", "c) 1972", "d) 1960"],
         "correta": "b"},
        {"pergunta": "Qual é o país mais populoso do mundo?",
         "opcoes": ["a) Índia", "b) Estados Unidos", "c) China", "d) Indonésia"], "correta": "c"},
        {"pergunta": "Qual é a montanha mais alta do mundo?",
         "opcoes": ["a) K2", "b) Monte Everest", "c) Monte Fuji", "d) Kilimanjaro"], "correta": "b"},
        {"pergunta": "Quantos minutos tem uma hora?", "opcoes": ["a) 50", "b) 55", "c) 60", "d) 65"], "correta": "c"},
        {"pergunta": "Qual o maior oceano do mundo?",
         "opcoes": ["a) Atlântico", "b) Índico", "c) Pacífico", "d) Ártico"], "correta": "c"},
        {"pergunta": "Qual é o menor país do mundo?",
         "opcoes": ["a) Mônaco", "b) Vaticano", "c) San Marino", "d) Malta"], "correta": "b"},
        {"pergunta": "Em que ano começou a Primeira Guerra Mundial?",
         "opcoes": ["a) 1910", "b) 1912", "c) 1914", "d) 1916"], "correta": "c"},
        {"pergunta": "Qual o metal cujo símbolo químico é 'Au'?",
         "opcoes": ["a) Prata", "b) Cobre", "c) Ouro", "d) Platina"], "correta": "c"},
        {"pergunta": "Quem escreveu 'Dom Quixote'?",
         "opcoes": ["a) Shakespeare", "b) Machado de Assis", "c) Cervantes", "d) Camões"], "correta": "c"},
        {"pergunta": "Quantas patas tem uma aranha?", "opcoes": ["a) 6", "b) 8", "c) 10", "d) 12"], "correta": "b"},
        {"pergunta": "Quem desenvolveu a teoria da relatividade?",
         "opcoes": ["a) Isaac Newton", "b) Galileo Galilei", "c) Albert Einstein", "d) Nikola Tesla"], "correta": "c"}
    ]

    pontos = 0
    max_acertos = 10

    while pontos < max_acertos and len(perguntas) > 0:
        pergunta_atual = random.choice(perguntas)
        perguntas.remove(pergunta_atual)

        print(pergunta_atual["pergunta"])

        for opcao in pergunta_atual["opcoes"]:
            print(opcao)

        resposta = input("Escolha uma letra: ").lower()

        if resposta == pergunta_atual["correta"]:
            pontos += 1
            print("Resposta correta!\n")

            if pontos == max_acertos:
                print(f"Parabéns, você venceu! Obrigado por jogar!")
                break
        else:
            print("Resposta errada! Fim de jogo.")
            print("\nObrigado por jogar!")
            break

quiz()