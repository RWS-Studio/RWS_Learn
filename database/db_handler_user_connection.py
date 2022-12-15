import os
import sqlite3


class user_connection():
    def __init__(self, db_name: str):
        # récupère le chemin du fichier
        self.con = sqlite3.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{db_name}")
        # défini les lignes
        self.con.row_factory = sqlite3.Row

    def first_connection(self, username: str, password: str, phone_number: int = None, double_auth: bool = False):
        cursor = self.con.cursor()  # création d'un fichier avant commit dans la db
        query = "INSERT INTO Account(username, password, phone_number, double_auth) VALUES (?, ?);"
        # exécution de la query + déf les valeurs pour éviter les injections SQL
        cursor.execute(query, (username, password, phone_number, double_auth))
        cursor.close()  # fermeture du fichier
        self.con.commit()  # commit dans la db

    def user_connection(self, username):
        cursor = self.con.cursor()
        query = "SELECT password FROM Account WHERE username = ?;"
        cursor.execute(query, (username,))  # il faut laisser la virgule pour éviter les erreurs
        result = cursor.fetchall()  # récupère dans une liste les infos
        cursor.close()
        return dict(result[0])["Password"]  # renvoie le password
