from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputText(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Welcome to your FastAPI app on Render!"}

@app.post("/predict")
def predict(data: InputText):
    # Just an example — replace with your logic later
    return {"input": data.text, "prediction": "Example result"}
