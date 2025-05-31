# backend/app/services/varredura.py
import requests
from bs4 import BeautifulSoup
from app.nlp.analise import analisar_sentimento
from app.services.reddit_scraper import buscar_reddit
from app.services.youtube_scraper import buscar_youtube
from app.services.twitter_scraper import buscar_twitter
from app.services.telegram_scraper import buscar_telegram

# Web scraping simples em notícias do Google
def buscar_noticias(termo):
    url = f"https://news.google.com/search?q={termo}"
    headers = {"User-Agent": "Mozilla/5.0"}
    resposta = requests.get(url, headers=headers)
    soup = BeautifulSoup(resposta.content, "html.parser")

    resultados = []
    for item in soup.select("article h3"):
        titulo = item.get_text()
        link = item.a['href'] if item.a else ''
        sentimento = analisar_sentimento(titulo)
        resultados.append({
            "fonte": "Google News",
            "titulo": titulo,
            "link": f"https://news.google.com{link}",
            "sentimento": sentimento
        })
    return resultados

# Função principal de varredura geral
def varredura_geral(termo):
    noticias = buscar_noticias(termo)
    reddit = buscar_reddit(termo)
    youtube = buscar_youtube(termo)
    twitter = buscar_twitter(termo)
    telegram = buscar_telegram(termo)

    return noticias + reddit + youtube + twitter + telegram
