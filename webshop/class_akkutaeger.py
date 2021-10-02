import sqlite3

from webshop.class_produkt import Produkt

class Akkutraeger(Produkt):

    def __init__(self, produktbezeichnung: str, preis: float, hersteller: str, funktionsweise: str, hoehe: float, breite: float, akkutyp: str, produkt_id=None):
        super().__init__(produkt_id=produkt_id, produktbezeichnung=produktbezeichnung, preis=preis, hersteller=hersteller)
        self.__funktionsweise = str(funktionsweise)
        self.__hoehe = float(hoehe)
        self.__breite = float(breite)
        self.__akkutyp = str(akkutyp)

    def display_info(self):
        print(f'Akkuträger {self._produktbezeichnung} mit einer Breite von {self.__breite} mm und Höhe '
              f'von {self.__hoehe}mm.\n Preis:{self._preis}')
