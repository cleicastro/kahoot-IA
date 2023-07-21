import openai
import os
import json
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.environ.get("API_KEY_CHATGPT")


def gerar_conteudo(pergunta):
    modelo_de_pergunta = [{"role": "user", "content": pergunta}]
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=modelo_de_pergunta, temperature=0.5, max_tokens=1024)
    message = resposta.choices[0].message

    if "content" in message:
        return json.loads(message.content)

    return []
