from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.note import NotesRepository, Note


def test_should_return_empty_list_of_notes():
    notes_repository = NotesRepository(temp_file())
    app = create_app(repositories={"note": notes_repository})
    client = app.test_client()

    response = client.get("/api/my-notes")

    assert response.json == []


def test_should_return_list_of_notes():
    notes_repository = NotesRepository(temp_file())
    app = create_app(repositories={"note": notes_repository})
    client = app.test_client()
    note = Note(title="example1", text="text example")
    notes_repository.save(note)
    response = client.get("/api/my-notes")

    assert response.json == [
        {
            "title": "example1",
            "text": "text example"
        }

    ]
