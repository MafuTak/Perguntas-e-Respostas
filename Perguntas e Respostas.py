import random

def quiz():
    temas = {
        "Geografia": [
            {"pergunta": "Qual é a capital da França?", "opcoes": ["a) Paris", "b) Londres", "c) Roma", "d) Madri"], "correta": "a"},
            {"pergunta": "Qual o maior planeta do sistema solar?", "opcoes": ["a) Terra", "b) Júpiter", "c) Marte", "d) Vênus"], "correta": "b"},
            {"pergunta": "Qual o maior oceano do mundo?", "opcoes": ["a) Atlântico", "b) Índico", "c) Pacífico", "d) Ártico"], "correta": "c"}
        ],
        "História": [
            {"pergunta": "Em que ano o homem pisou na Lua?", "opcoes": ["a) 1965", "b) 1969", "c) 1972", "d) 1960"], "correta": "b"},
            {"pergunta": "Em que ano começou a Primeira Guerra Mundial?", "opcoes": ["a) 1910", "b) 1912", "c) 1914", "d) 1916"], "correta": "c"},
            {"pergunta": "Quem desenvolveu a teoria da relatividade?", "opcoes": ["a) Isaac Newton", "b) Galileo Galilei", "c) Albert Einstein", "d) Nikola Tesla"], "correta": "c"}
        ],
        "Literatura": [
            {"pergunta": "Quem pintou a Mona Lisa?", "opcoes": ["a) Van Gogh", "b) Da Vinci", "c) Picasso", "d) Michelangelo"], "correta": "b"},
            {"pergunta": "Quem escreveu 'Dom Quixote'?", "opcoes": ["a) Shakespeare", "b) Machado de Assis", "c) Cervantes", "d) Camões"], "correta": "c"},
            {"pergunta": "Quem escreveu 'O Pequeno Príncipe'?", "opcoes": ["a) Antoine de Saint-Exupéry", "b) J.K. Rowling", "c) Mark Twain", "d) Jane Austen"], "correta": "a"}
        ],
        "Futebol": [
            {"pergunta": "Quantas Copas do Mundo a França já venceu?", "opcoes": ["a) 1", "b) 2", "c) 3", "d) 4"], "correta": "b"},
            {"pergunta": "Quem é o maior artilheiro da Seleção Brasileira?", "opcoes": ["a) Pelé", "b) Ronaldo", "c) Romário", "d) Neymar"], "correta": "a"},
            {"pergunta": "Qual é o time com mais títulos da Copa Libertadores?", "opcoes": ["a) Palmeiras", "b) Independiente", "c) River Plate", "d) Flamengo"], "correta": "b"}
        ],
        "Xadrez": [
            {"pergunta": "Quem é o campeão mundial de xadrez de 2021?", "opcoes": ["a) Magnus Carlsen", "b) Garry Kasparov", "c) Bobby Fischer", "d) Viswanathan Anand"], "correta": "a"},
            {"pergunta": "Quantas casas um cavalo pode se mover no xadrez?", "opcoes": ["a) 2", "b) 3", "c) 5", "d) 1"], "correta": "a"},
            {"pergunta": "O que é um xeque-mate?", "opcoes": ["a) Empate", "b) Captura da dama", "c) Rei em posição de ser capturado", "d) Movimento ilegal"], "correta": "c"}
        ]
    }

    perguntas = []
    for tema in temas.values():
        perguntas.extend(tema)

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