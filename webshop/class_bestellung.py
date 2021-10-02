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
            posten = Bestellposten(produkt_id=produkt_id, menge=menge, warenhaus=self.__warenhaus)
            self.__bestellposten.append(posten)
        else:
            print(f'Das Produkt mit der ID {produkt_id} konnte nicht im Produktkatalog gefunden werden.')

    def _display_warenkorb(self):
        print('\nIhr aktueller Warenkorb enthält:')
        gesamtpreis = 0
        for bestellposten in self.__bestellposten:
            bestellposten.display_info()
            gesamtpreis += bestellposten.get_total()

        print(f'Der Gesamtpreis aller Produkte im aktuellen Warenkorbes beträgt: {gesamtpreis:.2f}€')

    def _save_to_db(self, kunden_id: int):
        # todo: create method to save to db after order is placed
        pass

    # interne Methoden

    def __load_from_db(self):
        # todo: is this method needed?
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
            bestellposten = Bestellung(ds['POSTEN_ID'], ds['PRODUKT_ID'], ds['MENGE'], self.__warenhaus)
            self.__bestellposten.append(bestellposten)



