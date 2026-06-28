from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from predict import get_response

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "AI Chatbot API is running!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"error": "Invalid request"}), 400

        message = data.get("message", "").strip()

        if not message:
            return jsonify({"response": "Please enter a message."})

        response = get_response(message)

        return jsonify({"response": response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))