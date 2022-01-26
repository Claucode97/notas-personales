import sqlite3


class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text

    def to_dict(self):
        return {
            'title': self.title,
            'text': self.text
        }


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
                title varchar,
                text varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all(self):
        notes_list = []
        sql = """select * from notes"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)

        data = cursor.fetchall()

        for item in data:
            one_note = Note(
                title=item["title"], text=item["text"]
            )
            notes_list.append(one_note)

        return notes_list

    def save(self, note):
        sql = """insert into notes (title, text) values (
            :title, :text
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(
            sql,
            note.to_dict(),
        )
        conn.commit()
