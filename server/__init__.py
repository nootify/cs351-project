import os

from dotenv import load_dotenv
from flask import Flask


# Environment variables
load_dotenv()
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", "8080"))


def create_app(
    static_folder: str = "static", template_folder: str = "templates"
) -> Flask:
    app = Flask(__name__, static_folder=static_folder, template_folder=template_folder)
    return app


def run_app(app: Flask) -> None:
    app.run(host=HOST, port=PORT)
