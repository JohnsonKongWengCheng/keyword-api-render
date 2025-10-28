from fastapi import FastAPI, Request
import spacy

app = FastAPI()

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI NLP Keyword API!"}

@app.post("/extract_keywords/")
async def extract_keywords(request: Request):
    data = await request.json()
    text = data.get("text", "")
    
    if not text:
        return {"error": "Please provide some text input."}
    
    doc = nlp(text)

    # Extract potential keywords
    keywords = set()

    # Add noun chunks (phrases like "fall down", "heart attack")
    for chunk in doc.noun_chunks:
        keywords.add(chunk.text.lower())

    # Add verbs and adjectives that might be meaningful
    for token in doc:
        if token.pos_ in ["VERB", "ADJ"] and not token.is_stop:
            keywords.add(token.lemma_.lower())

    # Add named entities (like person, location, etc.)
    for ent in doc.ents:
        keywords.add(ent.text.lower())

    return {"input": text, "keywords": list(keywords)}
