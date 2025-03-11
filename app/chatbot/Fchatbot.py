from app.chatbot.Retrival import generate_response
from flask import Blueprint, request, jsonify

Fchatbot = Blueprint("Finance", __name__)

@Fchatbot.route("/chat-bot", methods=["POST"])
def chatbot_route():
    data = request.json
    prompt = data.get("prompt")
    result = generate_response(prompt=prompt)
    return jsonify(result)