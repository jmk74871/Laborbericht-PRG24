import sqlite3
from webshop.class_administrator import Administrator


class Produkt():

    def __init__(self, produktbezeichnung: str, preis: float, hersteller: str, produkt_id: int):
        self._produktbezeichnung = str(produktbezeichnung)
        self._hersteller = str(hersteller)
        self._preis = float(preis)
        if produkt_id is not None:
            self._produkt_id = int(produkt_id)
        else:
            self._produkt_id = None

    def get_price(self):
        return self._preis

    def get_produktbezeichnung(self):
        return self._produktbezeichnung
