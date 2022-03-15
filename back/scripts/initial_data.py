import sys
sys.path.insert(0, "")


def main():
    from src.domain.user import UserRepository, User
    from src.domain.note import NotesRepository, Note
    from src.domain.info import InfoRepository, Info

    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)

    info_repository.save(Info(app_name="f5-my-notes-app2"))

    notes_repository = NotesRepository(database_path)

    # Guardar categorias en NOTE repository
    notes_repository.save_a_new_category("cat-1", "Sports")
    notes_repository.save_a_new_category("cat-2", "Music")
    notes_repository.save_a_new_category("cat-3", "Shopping List")

    nota1 = Note(id="note-1", title="Lista de la compra:",
                 text="Pan y Chorizo", user_id="user-1", id_cat="cat-1")
    nota2 = Note(id="note-2", title='Bebidas',
                 text='Vino y agua', user_id="user-1", id_cat="cat-2")

    notes_repository.insert_data_note(nota1)
    notes_repository.insert_data_note(nota2)

    print("last category id: ", notes_repository.get_last_category_id())

    # Repositorio de Usuarios

    user_repository = UserRepository(database_path)

    user_repository.save(User("user-1", "Roberto"))
    user_repository.save(User("user-2", "Laura"))

    print("Datos iniciales cargados (se ha ejecutado initial_data.py)")


main()
