import random

def quiz():
    perguntas = [
        {"pergunta": "Qual é a capital da França?", "opcoes": ["a) Paris", "b) Londres", "c) Roma", "d) Madri"], "correta": "a"},
        {"pergunta": "Qual o maior planeta do sistema solar?", "opcoes": ["a) Terra", "b) Júpiter", "c) Marte", "d) Vênus"], "correta": "b"},
        {"pergunta": "Quem pintou a Mona Lisa?", "opcoes": ["a) Van Gogh", "b) Da Vinci", "c) Picasso", "d) Michelangelo"], "correta": "b"},
        {"pergunta": "Quantos estados tem o Brasil?", "opcoes": ["a) 25", "b) 26", "c) 27", "d) 28"], "correta": "c"}
    ]

    pontos = 0
    max_acertos = 3

    while pontos < max_acertos:
        pergunta_atual = random.choice(perguntas)

        print(pergunta_atual["pergunta"])

        for opcao in pergunta_atual["opcoes"]:
            print(opcao)

        resposta = input("Escolha uma letra: ").lower()

        if resposta == pergunta_atual["correta"]:
            pontos += 1
            print("Resposta correta!\n")

            if pontos == max_acertos:
                print(f"Parabéns! Você venceu com {pontos} acertos!")
                break
        else:
            print("Resposta errada! Fim de jogo.")
            break

quiz()
