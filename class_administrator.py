from class_benutzer import Benutzer
import sqlite3

class Administrator(Benutzer):
    def __init__(self, benutzer_id, benutzer_name, passwort, personal_nummer, abteilung):
        super().__init__(benutzer_id, benutzer_name, passwort)
        self.__personal_nummer = personal_nummer
        self.__abteilung = abteilung

    def add_product(self):
        pass

    def add_kunde(self, benutzer_name, passwort, vorname, nachname):

        conn = sqlite3.connect('test_db.db')

        conn.execute(f"INSERT INTO BENUTZER(BENUTZERNAME,PASSWORT) VALUES('{benutzer_name}','{passwort}');")

        cursor = conn.execute(f"SELECT ID,BENUTZERNAME from BENUTZER")
        for row in cursor:
            if benutzer_name == row[1]:
                benutzer_id = row[0]

        conn.execute(f"INSERT INTO KUNDE(BENUTZER_ID,VORNAME,NACHNAME) VALUES({benutzer_id},'{vorname}','{nachname}');")
        conn.close()
