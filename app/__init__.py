from flask import Flask
from app.chatbot.Fchatbot import Fchatbot as finance_bot
def create_app():
    app = Flask(__name__)

    app.register_blueprint(finance_bot,url_prefix="/api/finance")

    return app
