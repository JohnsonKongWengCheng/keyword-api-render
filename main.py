from flask import Flask, request, jsonify
import spacy

app = Flask(__name__)

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

@app.route("/")
def home():
    return "✅ Keyword Extraction API is running!"

@app.route("/extract", methods=["POST"])
def extract_keywords():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    doc = nlp(text)
    keywords = [token.text for token in doc if token.is_alpha and not token.is_stop]

    return jsonify({"keywords": keywords})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
