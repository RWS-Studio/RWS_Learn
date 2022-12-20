import sqlite3


class SubjectsManager:
    def __init__(self):
        self.con = sqlite3.connect(f"./db_marks.db")
        self.con.row_factory = sqlite3.Row

    def add_subject(self, subject: str):
        cursor = self.con.cursor()
        query = f"CREATE TABLE '{subject}' ('grade' FLOAT not null, " \
                f"                          'grade_max' INT not null, " \
                f"                          'grade_20' INT not null," \
                f"                          'factor' FLOAT not null," \
                f"                          'description' TEXT not null," \
                f"                          'id' INTEGER not null primary key autoincrement);"
        cursor.execute(query)
        cursor.close()
        self.con.commit()

    def del_subject(self, subject):
        cursor = self.con.cursor()
        query = f"DROP TABLE {subject}"
        cursor.execute(query)
        cursor.close()
        self.con.commit()

    def update_subject(self, old_name, new_name):
        cursor = self.con.cursor()
        query = f"ALTER TABLE {old_name} RENAME TO {new_name}"
        cursor.execute(query)
        cursor.close()
        self.con.commit()

    def view_subject(self):
        cursor = self.con.cursor()
        query = f'SELECT name from sqlite_master WHERE type="table"'
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
        # see result by *for loop* with 'print(list(result[i]))'
        # declare result before with 'SubjectsManager().view_subject()'
        # import SubjectsManager() before with 'from subjects_manager import SubjectsManager()'
