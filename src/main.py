import sys
from service.openai import gerar_conteudo
from service.kahoot import criar_draft, publicar_quiz, abrir_quiz


def gerar_quiz(tema):
    pergunta = 'Cria um quiz com o tema "' + tema + \
        '" com 10 perguntas e 4 opções de respostas, sendo que apenas uma pergunta é a correta e no final exiba o gabarito no formato JSON como neste exemplo {"question": "Quem foi que descobriu o Brasil?","choices": [{"answer": "Ronaldinho","correct": True},{"answer": "Pelé","correct": False},{"answer": "Messi","correct": False},{"answer": "Neymar","correct": False}]}.'

    return gerar_conteudo(pergunta)


def criar_questoes(questoes):
    modelo_questoes = []
    for questao in questoes["questions"]:
        modelo_questoes.append({
            "type": "quiz",
                    "question": questao["question"],
                    "choices": questao["choices"],
            "layout": "CLASSIC",
            "questionFormat": 0,
            "resources": "",
            "time": 20000,
            "video": {"fullUrl": "", "startTime": 0, "endTime": 0},
            "pointsMultiplier": 1
        })
    return modelo_questoes


def main():
    tema = sys.argv[1]
    quiz = gerar_quiz(tema)
    modelo_kahoot = criar_questoes(quiz)

    draft = criar_draft(perguntas=modelo_kahoot, titulo=tema)
    publicao = publicar_quiz(draft=draft)
    abrir_quiz(uuid=publicao["uuid"])


if __name__ == "__main__":
    main()
