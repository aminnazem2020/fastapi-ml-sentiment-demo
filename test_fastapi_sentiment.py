# test_fastapi_sentiment.py
import requests

# URL of your FastAPI endpoint
url = "http://127.0.0.1:8000/predict"

# Example text inputs
texts = [
    "I love this product! It works amazingly well.",
    "This is the worst experience I have ever had.",
    "I am not sure how I feel about this service."
]

for text in texts:
    # Send POST request with JSON body
    response = requests.post(url, json={"text": text})
    
    # Check if request was successful
    if response.status_code == 200:
        print(f"Input: {text}")
        print(f"Prediction: {response.json()['prediction']}\n")
    else:
        print(f"Failed to get prediction for input: {text}")
        print(f"Status Code: {response.status_code}, Response: {response.text}\n")
