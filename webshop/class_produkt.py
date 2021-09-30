import sqlite3
from webshop.class_administrator import Administrator


class Produkt():

    def __init__(self, produktbezeichnung: str, preis: float, hersteller: str, produkt_id: int = None):
        self._produktbezeichnung = str(produktbezeichnung)
        self._hersteller = str(hersteller)
        self._preis = float(preis)
        if produkt_id is not None:
            self._produkt_id = int(produkt_id)
        else:
            self._produkt_id = None

    def _save_to_prod_db(self, db_path: str, user: object) -> bool:
        if isinstance(user, Administrator):
            try:
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()

                # add to PRODUKT-DB
                cursor.execute(
                    f"INSERT INTO PRODUKTE(PRODUKTBEZEICHNUNG,PREIS, HERSTELLER) VALUES(:produktbezeichnung,:preis,:hersteller);",
                    {'produktbezeichnung': self._produktbezeichnung, 'preis': self._preis, 'hersteller': self._hersteller})
                conn.commit()
                # get id
                self._produkt_id = int(cursor.lastrowid)
                conn.close()

            except SQLiteException as eception:
                print(eception)
                return False

            return True
        else:
            return False