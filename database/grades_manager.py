import sqlite3


class GradesManager:
    def __init__(self):
        self.con = sqlite3.connect(f"./db_marks.db")
        self.con.row_factory = sqlite3.Row

    def checking_value_max(self, value: float, value_max: int):
        if value_max is None:
            value_max = 20
            value_20 = value
        else:
            value_20 = (value/value_max) * 20
        return value_max, value_20

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

    def add_grade(self, subject: str, value: float, factor: float, description: str, value_max: int = None):
        v_max_20 = self.checking_value_max(value, value_max)
        cursor = self.con.cursor()
        query = f"INSERT INTO {subject}(grade, grade_max, grade_20, factor, description) VALUES (?, ?, ?, ?, ?);"
        cursor.execute(query, (value, v_max_20[0], v_max_20[1], factor, description))
        cursor.close()
        self.con.commit()

    def update_grade(self, subject: str, value: float, factor: float, description: str, grade_id: int, value_max: int = None):
        v_max_20 = self.checking_value_max(value, value_max)
        cursor = self.con.cursor()
        query = f"UPDATE {subject} SET grade = ?, grade_max = ?, grade_20 = ?, factor = ?, description = ? WHERE id = ?"
        cursor.execute(query, (value, v_max_20[0], v_max_20[1], factor, description, grade_id))
        cursor.close()
        self.con.commit()

    def del_grade(self, subject: str, grade_id: int):
        cursor = self.con.cursor()
        query = f"DELETE FROM {subject} WHERE id = ?"
        cursor.execute(query, (grade_id,))
        cursor.close()
        self.con.commit()
