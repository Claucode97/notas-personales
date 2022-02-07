from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.note import NotesRepository, Note


def test_should_save_note():
    notes_repository = NotesRepository(temp_file())
    app = create_app(repositories={"note": notes_repository})
    client = app.test_client()

    note = {
        "id": "note1",
        "title": "example1",
        "text": "Hola nena",
    }

    response = client.post("/api/notes", json=note)

    assert response.status_code == 200

    response_get = client.get("/api/notes/note1")
    assert response_get.json == {
        "id": "note1",
        "title": "example1",
        "text": "Hola nena",
    }
