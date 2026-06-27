from flask import Flask, request, jsonify
from flask_cors import CORS

from predict import get_response

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "AI Chatbot API is running!"


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    message = data.get("message", "")

    response = get_response(message)

    return jsonify({
        "response": response
    })


if __name__ == "__main__":
    app.run(debug=True)