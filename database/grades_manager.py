import sqlite3


class GradesManager:
    def __init__(self):
        self.con = sqlite3.connect(f"./database/db_grades.db")
        self.con.row_factory = sqlite3.Row

    def value_20(self, value: float, value_max: int):
        value_20 = (value/value_max) * 20
        return value_20

    def add_grade(self, subject: str, value: float, factor: float, description: str, value_max: int):
        value_20 = self.value_20(value, value_max)
        cursor = self.con.cursor()
        query = f"INSERT INTO {subject}(grade, grade_max, grade_20, factor, description) VALUES (?, ?, ?, ?, ?);"
        cursor.execute(query, (value, value_max, value_20, factor, description))
        cursor.close()
        self.con.commit()

    def update_grade(self, subject: str, value: float, factor: float, description: str, grade_id: int,
                     value_max: int):
        value_20 = self.value_20(value, value_max)
        cursor = self.con.cursor()
        query = f"UPDATE {subject} SET grade = ?, grade_max = ?, grade_20 = ?, factor = ?, description = ? " \
                f"                                                                                      WHERE id = ?;"
        cursor.execute(query, (value, value_max, value_20, factor, description, grade_id))
        cursor.close()
        self.con.commit()

    def del_grade(self, subject: str, grade_id: int):
        cursor = self.con.cursor()
        query = f"DELETE FROM {subject} WHERE id = ?;"
        cursor.execute(query, (grade_id,))
        cursor.close()
        self.con.commit()

    def view_grade(self, subject, grade_id):
        cursor = self.con.cursor()
        query = f"SELECT grade, grade_max, grade_20, factor, description from {subject} WHERE id = ?;"
        cursor.execute(query, (grade_id,))
        result = cursor.fetchall()
        cursor.close()
        return dict(result[0])
