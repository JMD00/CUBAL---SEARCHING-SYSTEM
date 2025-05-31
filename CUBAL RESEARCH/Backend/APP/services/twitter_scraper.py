# backend/app/services/twitter_scraper.py
import requests
from app.nlp.analise import analisar_sentimento

BEARER_TOKEN = "SEU_TWITTER_BEARER_TOKEN"

def buscar_twitter(termo):
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    url = f"https://api.twitter.com/2/tweets/search/recent?query={termo}&max_results=10&tweet.fields=text"

    resposta = requests.get(url, headers=headers)
    dados = resposta.json()
    resultados = []

    for tweet in dados.get("data", []):
        texto = tweet["text"]
        sentimento = analisar_sentimento(texto)
        resultados.append({
            "fonte": "Twitter",
            "titulo": texto,
            "link": f"https://twitter.com/i/web/status/{tweet['id']}",
            "sentimento": sentimento
        })
    return resultados