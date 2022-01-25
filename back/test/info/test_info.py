from src.lib.utils import temp_file

from src.webserver import create_app
from src.domain.info_note import NotesRepository, Note


def test_should_return_note_in_database():
    notes_repository = NotesRepository(temp_file())
    app = create_app(repositories={"note": notes_repository})
    client = app.test_client()

    notes_repository.save(
        Note(
            app_my_notes="test application",
        )
    )

    response = client.get("/api/my-notes")
    assert response.json == {
        "app_my_notes": "test application",
    }
