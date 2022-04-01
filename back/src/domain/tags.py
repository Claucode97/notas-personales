import sqlite3
import json


class Tag:
    def __init__(self, note_id, tag):
        self.note_id = note_id
        self.tag = tag

    def to_dict(self):
        return {"note_id": self.note_id, "tag": self.tag}


class TagsRepository:
    def __init__(self, database_path):
        self.database_path = database_path
        self.init_tables()

    def create_conn(self):
        conn = sqlite3.connect(self.database_path)
        conn.row_factory = sqlite3.Row
        return conn

    def init_tables(self):
        sql = """
            create table if not exists tags (
                note_id varchar,
                tag varchar
            )
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()

    def get_all_tags(self):
        sql = """select * from tags"""
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        list_tag = []
        for item in data:
            tag_class = Tag(note_id=json.loads(item["note_id"]), tag=item["tag"])
            list_tag.append(tag_class)
        return list_tag

    def get_by_note_id(self, note_id):
        sql = """SELECT * FROM tags WHERE note_id = :note_id
        """
        conn = self.create_conn()
        cursor = conn.cursor()
        cursor.execute(sql, {"note_id": note_id})
        data = cursor.fetchone()
        if data is None:
            return None
        else:
            tag = Tag(**data)
        return tag

    def save(self, tags):
        sql = """INSERT INTO tags (note_id, tag) values (
            :note_id, :tag
        ) """
        conn = self.create_conn()
        cursor = conn.cursor()
        # cursor.execute(sql, {"note_id": tags.note_id, "tag": json.dumps(tags.tag)})
        # conn.commit()
        str_tags = json.dumps(tags.to_dict())
        json_tags = json.loads(str_tags)
        print(json_tags)
        if json_tags["tag"] == []:
            return ""
        else:
            for tag in json_tags["tag"]:
                cursor.execute(
                    sql, {"note_id": json.dumps(json_tags["note_id"]), "tag": tag}
                )
                conn.commit()
