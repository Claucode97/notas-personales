from flask import Flask
from flask_cors import CORS

from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/my-notes", methods=["GET"])
    def notes_get():
        notes = repositories["note"].get_notes()
        return object_to_json(notes)

    return app
