import requests
import json
import os
import webbrowser
from dotenv import load_dotenv


load_dotenv()

token = os.environ.get("API_KEY_KAHOOT")

headers_contenxt_data = {
    "Authorization": "Bearer " + token,
    "User-Agente": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5.1 Safari/605.1.15',
    "content-type": "application/json",
    "accept-encoding": "gzip, deflate, br",
    "accept": "*/*",
}


def criar_draft(perguntas, titulo):
    url = "https://create.kahoot.it/rest/drafts"
    print("creating draft: ["+url+"]")
    body = {
        "kahoot": {
            "cover": "",
            "description": "Quiz gerado pela IA",
            "folderId": "031af8f4-ea14-44de-993f-fe81dda4037b",
            "introVideo": "",
            "playAsGuest": False,
            "language": "Português",
            "metadata": {
                "resolution": "",
                "moderation": {"flaggedTimestamp": 0, "timestampResolution": 0},
                "duplicationProtection": False
            },
            "title": titulo,
            "questions": perguntas,
            "quizType": "quiz",
            "resources": "",
            "type": "quiz",
            "visibility": 0,
            "creator_username": "",
            "lobby_video": {
                "youtube": {"id": "", "fullUrl": "", "startTime": 0}
            }
        },
        "kahootExists": False
    }

    resposta = requests.post(
        url, data=json.dumps(body), headers=headers_contenxt_data)

    if resposta.status_code == 200:
        return json.loads(resposta.content)
    else:
        print(resposta.content)
        print("Não foi possivel criar o rascunho, favor tente novamente!")
        return {}


def publicar_quiz(draft):
    url = "https://create.kahoot.it/rest/drafts/"+draft["id"]+"/publish"
    print("send data to: ["+url+"]")

    resposta = requests.post(url, data=json.dumps(
        draft), headers=headers_contenxt_data)

    if (resposta.status_code == 200):
        return json.loads(resposta.content)
    else:
        print(resposta.content)
        print("Não foi possivel publicar este quiz, favor tente manualmente!")
        return {}


def abrir_quiz(uuid):
    url = "https://play.kahoot.it/v2/lobby?quizId="+uuid
    print("open game: ["+url+"]")

    webbrowser.open(url)
