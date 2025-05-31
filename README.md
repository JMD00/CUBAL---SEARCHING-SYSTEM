# CUBAL--SYSTEMA DE VARREDURA INTELIGENTE


# 🕵️‍♂️ Varredura Sondagem App

Sistema de varredura inteligente para coleta, análise e visualização de assuntos populares e tendências em diversas fontes da internet e redes sociais, com análise de sentimento embutida.

## 📦 Estrutura do Projeto

```
projeto-sondagem/
├── backend/              # API + serviços de varredura
│   ├── app/
│   │   ├── main.py       # FastAPI app
│   │   ├── routes/       # Rotas da API
│   │   ├── services/     # Scrapers e APIs externas (Reddit, Twitter, etc)
│   │   ├── nlp/          # Módulo de análise de sentimentos
│   │   └── database/     # (Futuro) integração com MongoDB
│   └── requirements.txt  # Dependências do backend
│
├── frontend/             # Interface de visualização
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── App.jsx       # Página principal
│   └── package.json
│
├── database/             # Scripts de setup do banco (em breve)
│   └── init-mongo.js
│
├── docker-compose.yml    # (Futuro) Orquestração com Docker
└── README.md
```

---

## 🚀 Tecnologias

### Backend

- [FastAPI](https://fastapi.tiangolo.com/)
- [PRAW (Reddit API)](https://praw.readthedocs.io/)
- [Requests + BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Transformers - HuggingFace](https://huggingface.co/transformers/)
- [Twitter API v2](https://developer.twitter.com/en/docs/twitter-api)
- MongoDB (em breve)

### Frontend

- React + Tailwind CSS
- Axios para comunicação com API

---

## ⚙️ Instalação

### 1. Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

#### Variáveis de ambiente (coloque no `.env`)

```
TWITTER_BEARER_TOKEN=SEU_TOKEN_AQUI
```

### 2. Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 🔍 Funcionalidades Atuais

- ✅ Busca por termo em:
  - Reddit
  - Notícias (Google News)
  - Twitter (X)
- ✅ Análise de sentimentos com Transformers (HuggingFace)
- ✅ Visualização dos resultados em uma interface simples

---

## 📌 Futuras Integrações

- [ ] YouTube (Data API)
- [ ] Telegram (via bot/grupo público)
- [ ] Facebook & Instagram (Meta API)
- [ ] Armazenamento em MongoDB
- [ ] Orquestração com Docker

---

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

---

## 🧠 Licença

Este projeto é open-source sob a licença MIT.
