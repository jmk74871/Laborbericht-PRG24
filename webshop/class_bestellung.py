from datetime import datetime
import sqlite3
from webshop.class_bestellposten import Bestellposten


class Bestellung():

    def __init__(self, db_path: str, bestell_id=None, bestelldatum=None, bestellstatus='offen'):
        # todo: add enum for bestellstatus, also needs a change in the DB (Text to Integer)

        self.__bestell_id = bestell_id
        self.__bestelldatum = bestelldatum
        self.__bestellstatus = bestellstatus
        self.__bestellposten = []
        self.__db_path = db_path

        if self.__bestell_id is not None:
            self.__get_bestellposten_from_db()

    # öffentliche Schnitstellen - sollen über andere Klassen angesprochen werden

    def _add_bestellposten(self, produkt_id: int, menge: int):
        if self.__bestellstatus == 'offen':
            conn = sqlite3.connect(self.__db_path)
            cursor = conn.cursor()

            # add to BESTELLPOSTEN-DB
            cursor.execute(
                f"INSERT INTO BESTELLPOSTEN (BESTELL_ID, PRODUKT_ID, MENGE)"
                f"VALUES(:bestell_id, :prdukt_id, :menge);",
                {'bestell_id': self.__bestell_id, 'produkt_id': produkt_id, 'menge': menge})
            conn.commit()

            print(f'Adresse in der {strasse} {hausnummer} in {stadt} erfolgreich angelegt.')

            self.__get_bestellposten_from_db()

    # interne Methoden

    def __load_from_db(self):
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * from BETELLUNGEN WHERE BESTELL_ID = :bestell_id;", {'bestell_id': self.__bestell_id})

        res = cursor.fetchall()
        for ds in res:
            adresse = Adresse(ds['ADRESS_ID'], ds['STRASSE'], ds['HAUSNUMMER'], ds['PLZ'], ds['STADT'])
            self.__adressen.append(adresse)
        conn.close()

        pass

    def __get_bestellposten_from_db(self):
        self.__bestellposten = []

        conn = sqlite3.connect(self.__db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * from BESTELLPOSTEN WHERE BESTELL_ID = :bestell_id;",
                       {'bestell_id': self.__bestell_id})

        res = cursor.fetchall()
        conn.close()

        for ds in res:
            bestellposten = Bestellung(ds['POSTEN_ID'], ds['PRODUKT_ID'], ds['MENGE'])
            self.__bestellposten.append(bestellposten)



