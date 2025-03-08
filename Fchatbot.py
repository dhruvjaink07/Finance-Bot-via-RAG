from Finance.Retrival import generate_response
from flask import Blueprint, request, jsonify,Flask

app = Flask(__name__)

Fchatbot = Blueprint("Finance", __name__)
#Fchatbot.register_blueprint(Fchatbot)

@Fchatbot.route("/Fchatbot", methods=["POST"])
def chatbot_route():
    data = request.json
    prompt = data.get("prompt")
    result = generate_response(prompt=prompt)
    return jsonify(result)

# Register the Blueprint with the Flask application
app.register_blueprint(Fchatbot)

if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True, host="0.0.0.0", port=5000)