from datetime import datetime
import sqlite3
from webshop.class_bestellposten import Bestellposten


class Bestellung():

    def __init__(self, bestell_id, bestelldatum, bestellstatus='offen'):
        self.__bestell_id = int(bestell_id)
        self.__bestelldatum = datetime(bestelldatum)
        self.__bestellstatus = str(bestellstatus)
        self.__bestellposten = []
        self.db_path = "../test_db.db"

        self.get_bestellposten_from_db()

    def __get_bestellposten_from_db(self):
        conn = sqlite3.connect(self.__db_path)

        cursor = conn.execute(f"SELECT * from BESTELLPOSTEN WHERE BESTELL_ID == {self.__id}")

        # ToDO: finish method
        pass
