import sqlite3


class marks_manager():
    def __init__(self):
        self.con = sqlite3.connect(f"./db_marks.db")
        self.con.row_factory = sqlite3.Row

    def add_subject(self, subject: str):
        cursor = self.con.cursor()
        query = f"CREATE TABLE '{subject}' ('mark' FLOAT not null, " \
                f"                          'max_mark' INT not null, " \
                f"                          'mark_20' INT not null);"
        cursor.execute(query)
        cursor.close()
        self.con.commit()

    def add_marks(self, subject: str, mark: float, max_mark: int = None):
        if max_mark is None:
            max_mark = 20
            mark_20 = mark
        else:
            mark_20 = (mark/max_mark)*20
        cursor = self.con.cursor()
        query = f"INSERT INTO {subject}(mark, max_mark, mark_20) VALUES (?, ?, ?);"
        cursor.execute(query, (mark, max_mark, mark_20))
        cursor.close()
        self.con.commit()
