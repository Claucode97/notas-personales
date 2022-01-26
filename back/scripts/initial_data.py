import sys
sys.path.insert(0, "")


def main():
    from src.domain.note import NotesRepository, Note
    from src.domain.info import InfoRepository, Info

    database_path = "data/database.db"

    notes_repository = NotesRepository(database_path)

    info_repository = InfoRepository(database_path)

    info_repository.save(Info(app_my_notes="f5-my-notes-app2"))


main()
