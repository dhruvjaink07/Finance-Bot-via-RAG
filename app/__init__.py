from flask import Flask
from app.chatbot.Fchatbot import Fchatbot as finance_bot
from app.phishing_url.Umodel import phishing_detector as url_checker
def create_app():
    app = Flask(__name__)

    app.register_blueprint(finance_bot,url_prefix="/api/finance")
    app.register_blueprint(url_checker,url_prefix="/api/phishing")
    return app
