from webshop.class_produkt import Produkt
import sqlite3


class Verdampfer(Produkt):

    def __init__(self, produktbezeichnung: str, preis: float, hersteller: str, durchmesser: float, hoehe: float,
                 fuellsystem: str, produkt_id=None):
        super().__init__(produktbezeichnung, preis, hersteller, produkt_id)
        self.__hoehe = float(hoehe)
        self.__durchmesser = float(durchmesser)
        self.__fuellsystem = str(fuellsystem)

    def display_info(self):
        print(f'Verdampfer {self._produktbezeichnung} mit einem Durchmesser von {self.__durchmesser}mm und Höhe '
              f'von {self.__hoehe}mm.\n Preis:{self._preis}')
