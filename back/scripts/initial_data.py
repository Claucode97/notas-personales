import sys
sys.path.insert(0, "")


def main():
    from src.domain.info_note import NotesRepository, Note

    database_path = "data/database.db"

    info_repository = NotesRepository(database_path)

    info_repository.save(Note(app_my_notes="f5-my-notes-app2"))


main()
