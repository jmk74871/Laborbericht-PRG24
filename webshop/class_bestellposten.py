from webshop.class_warenhaus import Warenhaus
import sqlite3


class Bestellposten():

    def __init__(self, produkt_id: int, menge: int, warenhaus: Warenhaus, db_path: str, posten_id=None):
        self.__warenhaus = warenhaus
        self.__posten_id = posten_id
        self.__produkt_id = produkt_id
        self.__menge = menge
        self.__db_path = db_path

    def get_total(self) -> float:
        return float(self.__warenhaus.get_by_id(self.__produkt_id).get_price() * self.__menge)

    def get_info(self) -> str:
        prod = self.__warenhaus.get_by_id(self.__produkt_id)
        return f"\n{self.__menge} mal {prod.get_produktbezeichnung()} (ID: {prod.get_produkt_id()}) " \
               f"mit einem Stückpreis von {prod.get_price():.2f}€\n Gesammtpreis: {self.get_total():.2f}€"

    def get_produkt_id(self) -> int:
        return self.__produkt_id

    def _save_to_db(self, bestell_id: int) -> None:
        conn = sqlite3.connect(self.__db_path)
        cursor = conn.cursor()

        # add to BESTELLPOSTEN-DB
        cursor.execute("INSERT INTO BESTELLPOSTEN (BESTELL_ID, PRODUKT_ID, MENGE) "
                       "VALUES(:bestell_id, :pordukt_id, :menge);",
                       {'bestell_id': bestell_id, 'pordukt_id': self.__produkt_id, 'menge': self.__menge})
        conn.commit()
        pass
