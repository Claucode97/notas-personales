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

    @app.route("/api/notes", methods=["GET"])
    def notes_get_all():

        notes = repositories["note"].get_all()
        return object_to_json(notes)

    @app.route("/api/notes/<id>", methods=["GET"])
    def notes_get_by_id(id):

        one_note_by_id = repositories["note"].get_by_id(id)
        return object_to_json(one_note_by_id)

    return app


"""    @app.route("/api/save-notes", methods=["POST"])
    def notes_post():
        repositories["note"].save("Título1", "Descripción de la nota 1")
        return True"""
