from datetime import datetime
import sqlite3
from webshop.class_bestellposten import Bestellposten
from webshop.class_warenhaus import Warenhaus


class Bestellung():

    def __init__(self, db_path: str, warenhaus: Warenhaus, bestell_id=None, bestelldatum=None, bestellstatus='offen'):
        # todo: add enum for bestellstatus, also needs a change in the DB (Text to Integer)
        self.__warenhaus = warenhaus
        self.__bestell_id = bestell_id
        self.__bestelldatum = bestelldatum
        self.__bestellstatus = bestellstatus
        self.__bestellposten = []
        self.__db_path = db_path

        if self.__bestell_id is not None:
            self.__get_bestellposten_from_db()

    # öffentliche Schnitstellen - sollen über andere Klassen angesprochen werden

    def _add_bestellposten(self, produkt_id: int, menge: int):
        if self.__bestellstatus == 'offen' and self.__warenhaus._check_exist(produkt_id):
            posten = Bestellposten(produkt_id=produkt_id, menge=menge, warenhaus=self.__warenhaus,
                                   db_path=self.__db_path)
            self.__bestellposten.append(posten)
        else:
            print(f'Das Produkt mit der ID {produkt_id} konnte nicht im Produktkatalog gefunden werden.')

    def _show_bestellposten(self) -> str:
        returnstring = ''
        returnstring += '\nIhr aktueller Warenkorb enthält:'
        gesamtpreis = 0
        for bestellposten in self.__bestellposten:
            returnstring += bestellposten.get_info()
            gesamtpreis += bestellposten.get_total()

        returnstring += f'\n\nDer Gesamtpreis aller Produkte im aktuellen Warenkorbes beträgt: {gesamtpreis:.2f}€'

        return returnstring

    def _delete_bestellposten(self, produkt_id: int):
        self.__bestellposten = [posten for posten in self.__bestellposten if posten.get_produkt_id() != produkt_id]

    def _save_to_db(self, benutzer_id: int, adress_id: int, bank_id: int):
        # todo: create method to save to db after order is placed
        conn = sqlite3.connect(self.__db_path)
        cursor = conn.cursor()

        # add to BESTELLUNGEN-DB
        cursor.execute(
            f"INSERT INTO BESTELLUNGEN (BENUTZER_ID, BESTELLDATUM, STATUS, ADRESS_ID, BANK_ID) "
            f"VALUES(:benutzer_id, :bestelldatum, :status, :adress_id, :bank_id);",
            {'benutzer_id': benutzer_id, 'bestelldatum': datetime.now(), 'status': 'in Bearbeitung',
             'adress_id': adress_id, 'bank_id': bank_id})
        conn.commit()

        self.__bestell_id = cursor.lastrowid
        self.__bestellstatus = 'in Bearbeitung'

        for posten in self.__bestellposten:
            posten._save_to_db(bestell_id=self.__bestell_id)

    # interne Methoden

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
            bestellposten = Bestellposten(posten_id=ds['POSTEN_ID'], produkt_id=ds['PRODUKT_ID'], menge=ds['MENGE'],
                                          warenhaus=self.__warenhaus, db_path=self.__db_path)
            self.__bestellposten.append(bestellposten)
