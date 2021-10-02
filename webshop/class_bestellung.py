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

    def _warenkorb_anzeigen(self) -> str:
        returnstring = ''
        returnstring += '\nIhr aktueller Warenkorb enthält:'
        gesamtpreis = 0
        for bestellposten in self.__bestellposten:
            returnstring += bestellposten.get_info()
            gesamtpreis += bestellposten.get_total()

        returnstring += f'\n\nDer Gesamtpreis aller Produkte im aktuellen Warenkorbes beträgt: {gesamtpreis:.2f}€'

        return returnstring

    def _save_to_db(self, kunden_id: int):
        # todo: create method to save to db after order is placed
        conn = sqlite3.connect(self.__db_path)
        cursor = conn.cursor()

        # add to BESTELLUNGEN-DB
        cursor.execute(
            f"INSERT INTO BESTELLUNGEN (BENUTZER_ID, BESTELLDATUM, STATUS) "
            f"VALUES(:benutzer_id, :bestelldatum, :status);",
            {'benutzer_id': kunden_id, 'bestelldatum': datetime.now(), 'status': 'in Bearbeitung'})
        conn.commit()
        self.__bestellstatus = 'in Bearbeitung'

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
