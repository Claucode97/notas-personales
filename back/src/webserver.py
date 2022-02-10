from flask import Flask, request
from flask_cors import CORS

from src.lib.utils import object_to_json
from src.domain.note import Note


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

    @app.route("/api/notes", methods=["POST"])
    def notes_post():
        data = request.json
        print("*****", request.data)
        note = Note(**data)
        repositories["note"].insert_data_note(note)
        return ''

    @app.route("/api/notes/<id>", methods=["GET"])
    def notes_get_by_id(id):

        one_note_by_id = repositories["note"].get_by_id(id)
        return object_to_json(one_note_by_id)

    @app.route("/api/notes/<id>", methods=["POST"])
    def notes_modify(id, titulo, detalles):

        modified_note = repositories["note"].modify_data_note_by_id(
            id, titulo, detalles)
        return object_to_json(modified_note)

    @app.route("/api/notes/<id>", methods=["DELETE"])
    def deleted_note_by_id(id):
        note_deleted_by_id = repositories["note"].note_deleted_by_id(id)
        return ""

    return app


"""    @app.route("/api/save-notes", methods=["POST"])
    def notes_post():
         --> save cambia a insert_data_note
        repositories["note"].save("Título1", "Descripción de la nota 1")
        return True"""
