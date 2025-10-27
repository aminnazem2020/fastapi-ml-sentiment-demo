from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Initialize FastAPI app
app = FastAPI(title="Hugging Face Sentiment API")

# Load Hugging Face sentiment-analysis model
sentiment_model = pipeline("sentiment-analysis")

# Define input data structure
class TextRequest(BaseModel):
    text: str

# Define API endpoint
@app.post("/predict")
def predict_sentiment(request: TextRequest):
    text = request.text
    result = sentiment_model(text)
    return {"input": text, "prediction": result}
