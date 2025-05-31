backend/app/services/reddit_scraper.py
import praw
from app.nlp.analise import analisar_sentimento

reddit = praw.Reddit(
    client_id="SEU_CLIENT_ID",
    client_secret="SEU_SECRET",
    user_agent="VarreduraBot"
)

def buscar_reddit(termo):
    resultados = []
    for post in reddit.subreddit("all").search(termo, limit=10):
        sentimento = analisar_sentimento(post.title)
        resultados.append({
            "fonte": "Reddit",
            "titulo": post.title,
            "link": post.url,
            "sentimento": sentimento
        })
    return resultados
