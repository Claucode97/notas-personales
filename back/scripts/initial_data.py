import sys
sys.path.insert(0, "")


def main():
    from src.domain.note import NotesRepository, Note
    from src.domain.info import InfoRepository, Info

    database_path = "data/database.db"

    info_repository = InfoRepository(database_path)

    info_repository.save(Info(app_name="f5-my-notes-app2"))

    notes_repository = NotesRepository(database_path)

    nota1 = Note(id="note-1", title="Lista de la compra:",
                 text="Pan y Chorizo")
    nota2 = Note(id="note-2", title='Bebidas', text='Vino y agua')

    notes_repository.insert_data_note(nota1)
    notes_repository.insert_data_note(nota2)

    print("datos iniciales cargados")


main()
