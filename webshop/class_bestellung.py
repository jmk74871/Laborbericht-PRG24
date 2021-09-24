from class_kunde import Kunde
import sqlite3

class Bestellung():

    def __init__(self, id, benutzer_id, bestelldatum, bestellstatus='offen'):
        self.__id = id
        self.__benutzer_id = benutzer_id
        self.__bestelldatum = bestelldatum
        self.__bestellstatus = bestellstatus
        self.__bestellposten = []
        self.db_path = "../test_db.db"

        self.get_bestellposten_from_db()

    def __get_bestellposten_from_db(self):
        conn = sqlite3.connect('test_db.db')

        cursor = conn.execute(f"SELECT * from BESTELLPOSTEN WHERE BESTELL_ID == {self.__id}")

        # ToDO: finish method
        pass
