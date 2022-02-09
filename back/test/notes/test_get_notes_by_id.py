from src.lib.utils import temp_file
from src.webserver import create_app
from src.domain.note import NotesRepository, Note


def test_shuld_return_existing_note_by_id():
    notes_repository = NotesRepository(temp_file())
    app = create_app(repositories={"note": notes_repository})
    client = app.test_client()
    note = Note(id="pepa", title="example1", text="text example")
    notes_repository.insert_data_note(note)

    response = client.get("/api/notes/pepa")

    assert response.json == {
        "id": "pepa",
        "title": "example1",
        "text": "text example"
    }
