#  FastAPI + Hugging Face Sentiment Analysis App

This is a simple **Machine Learning deployment project** built using **FastAPI** and a **Hugging Face Transformer model**.  
It performs **sentiment analysis** (Positive / Negative) on user input text — a great example of modern AI integration with web APIs.

---

## What It Does
You send a text string to the API, and it responds with the model’s prediction:
- **Positive sentiment**
- **Negative sentiment**

Example:
```json
Input:  "I love this project!"
Output: {"label": "POSITIVE", "score": 0.9997}
