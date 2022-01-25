import sqlite3


class Note:
    def __init__(self, app_my_notes):
        self.app_my_notes = app_my_notes

    def to_dict(self):
        return {"app_my_notes": self.app_my_notes}


class NotesRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists notes (
                app_my_notes varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_notes(self):
        sql = """select * from notes"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchone()

        return Note(app_my_notes=data["app_my_notes"])

    def save(self, notes):
        sql = """insert into notes (app_my_notes) values (
            :app_my_notes
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, notes.to_dict())
        conn.commit()
