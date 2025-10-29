from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import spacy

app = FastAPI()

# Allow Android app or web clients to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load English model
nlp = spacy.load("en_core_web_sm")

@app.get("/")
def home():
    return {"message": "Welcome to your FastAPI NLP Keyword API!"}

@app.post("/extract_keywords")
async def extract_keywords(request: Request):
    data = await request.json()
    text = data.get("text", "")
    doc = nlp(text)

    # Collect important phrases (noun chunks + meaningful verbs)
    keywords = set()

    # Add noun phrases like "the ladder", "a car accident"
    for chunk in doc.noun_chunks:
        if len(chunk.text.split()) > 1:
            keywords.add(chunk.text.lower())

    # Add strong verbs (actions)
    for token in doc:
        if token.pos_ in ["VERB", "ADJ"] and not token.is_stop:
            keywords.add(token.lemma_.lower())

    return {
        "input": text,
        "keywords": list(keywords)
    }
