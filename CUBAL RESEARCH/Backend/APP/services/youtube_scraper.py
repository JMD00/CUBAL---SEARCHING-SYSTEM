# backend/app/services/youtube_scraper.py
from googleapiclient.discovery import build
from app.nlp.analise import analisar_sentimento

API_KEY = "SUA_YOUTUBE_API_KEY"
youtube = build("youtube", "v3", developerKey=API_KEY)

def buscar_youtube(termo):
    resultados = []
    req = youtube.search().list(q=termo, part="snippet", type="video", maxResults=10)
    res = req.execute()

    for item in res["items"]:
        titulo = item["snippet"]["title"]
        video_id = item["id"]["videoId"]
        sentimento = analisar_sentimento(titulo)
        resultados.append({
            "fonte": "YouTube",
            "titulo": titulo,
            "link": f"https://youtube.com/watch?v={video_id}",
            "sentimento": sentimento
        })
    return resultados