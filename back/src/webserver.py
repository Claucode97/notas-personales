from flask import Flask
from flask_cors import CORS

from src.lib.utils import object_to_json


def create_app(repositories):
    app = Flask(__name__)
    CORS(app)

    @app.route("/", methods=["GET"])
    def hello_world():
        return "...magic!"

    @app.route("/api/info", methods=["GET"])
    def info():
        info = repositories["info"].get_info()
        return object_to_json(info)

    @app.route("/api/my-notes", methods=["GET"])
    def notes_get():

        notes = repositories["note"].get_all()
        return object_to_json(notes)

    return app


"""    @app.route("/api/save-notes", methods=["POST"])
    def notes_post():
        repositories["note"].save("Título1", "Descripción de la nota 1")
        return True"""
