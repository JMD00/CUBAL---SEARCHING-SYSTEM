# backend/app/services/telegram_scraper.py
import requests
from bs4 import BeautifulSoup
from app.nlp.analise import analisar_sentimento

# Exemplo usando scraping em canal público no telegra.ph

def buscar_telegram(termo):
    resultados = []
    url = f"https://t.me/s/{termo}"
    headers = {"User-Agent": "Mozilla/5.0"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser")

    for msg in soup.select(".tgme_widget_message_text")[:10]:
        texto = msg.get_text()
        sentimento = analisar_sentimento(texto)
        resultados.append({
            "fonte": "Telegram",
            "titulo": texto[:100],
            "link": url,
            "sentimento": sentimento
        })
    return resultados