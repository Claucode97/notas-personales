import sys
sys.path.insert(0, "")


def main():
    from src.domain.users import UserRepository, User
    from src.domain.note import NotesRepository, Note
    from src.domain.info import InfoRepository, Info

    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)

    info_repository.save(Info(app_name="f5-my-notes-app2"))

    notes_repository = NotesRepository(database_path)

    nota1 = Note(id="note-1", title="Lista de la compra:",
                 text="Pan y Chorizo", user_id="user-1")
    nota2 = Note(id="note-2", title='Bebidas',
                 text='Vino y agua', user_id="user-1")

    notes_repository.insert_data_note(nota1)
    notes_repository.insert_data_note(nota2)

    user_repository = UserRepository(database_path)

    user_repository.save(User("user-1", "Roberto"))
    user_repository.save(User("user-2", "Laura"))
    print("datos iniciales cargados")


main()
