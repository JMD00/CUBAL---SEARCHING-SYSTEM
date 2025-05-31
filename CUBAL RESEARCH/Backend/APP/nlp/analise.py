# backend/app/nlp/analise.py
from sklearn.feature_extraction.text import TfidfVectorizer
from transformers import pipeline
import numpy as np

# Pipeline de análise de sentimento com HuggingFace
sentiment_model = pipeline("sentiment-analysis")

def analisar_sentimento(texto):
    resultado = sentiment_model(texto[:512])[0]  # Limite de tokens
    return {
        "label": resultado["label"],
        "score": round(resultado["score"], 2)
    }

# Extração de tópicos usando TF-IDF
def extrair_topicos(docs, n_topicos=5):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
    X = vectorizer.fit_transform(docs)
    palavras = vectorizer.get_feature_names_out()
    pontuacoes = np.asarray(X.sum(axis=0)).flatten()

    top_indices = pontuacoes.argsort()[-n_topicos:][::-1]
    topicos = [(palavras[i], round(pontuacoes[i], 3)) for i in top_indices]
    return topicos
