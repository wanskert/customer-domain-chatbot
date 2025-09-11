# Customer Domain Chatbot


Production‑style demo of a customer support chatbot. Uses a **zero‑shot intent router** (transformers) to classify messages into business intents (order_status, refund_request, product_info, troubleshooting, smalltalk) and then calls simple **skill handlers**. Exposes a **FastAPI** endpoint.

customer support chatbot with RESTful microservices and Java backend, which accurately handles scalable multi-domain chatbots.

![build](https://img.shields.io/badge/build-passing-brightgreen)
![python](https://img.shields.io/badge/python-3.10+-blue)
![license](https://img.shields.io/badge/license-MIT-informational)


##  Features
- Zero‑shot intent classification (no training needed) using `typeform/distilbert-base-uncased-mnli`
- Confidence threshold & fallback to smalltalk
- Modular skill handlers (order status, refunds, product info, troubleshooting, smalltalk)
- FastAPI endpoints: `POST /classify`, `POST /chat`
- Unit tests with `pytest`
- Optional Dockerfile


##  Data (optional)
Place a CSV at `data/intents.csv` with columns: `text, intent` to fine-tune later.


##  Quickstart
```bash
python -m venv .venv && source .venv/bin/activate # Windows: .venv\Scripts\activate
pip install -r requirements.txt


# run API
uvicorn api.main:app --reload --port 8001
# classify
curl -X POST http://127.0.0.1:8001/classify -H 'Content-Type: application/json' \
-d '{"text":"Where is my order #12345?"}'


# chat (routes to a handler)
curl -X POST http://127.0.0.1:8001/chat -H 'Content-Type: application/json' \
-d '{"text":"I want a refund for my last purchase"}'
