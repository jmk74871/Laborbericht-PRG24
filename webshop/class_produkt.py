import sqlite3


class Produkt():

    def __init__(self, produktbezeichnung: str, preis: float, hersteller: str, produkt_id: int = None):
        self.__produktbezeichnung = str(produktbezeichnung)
        self.__hersteller = str(hersteller)
        self.__preis = float(preis)
        if produkt_id is not None:
            self.__produkt_id = int(produkt_id)
        else:
            self.__produkt_id = None

    def save_to_db(self) -> int:
        conn = sqlite3.connect('test_db.db')
        cursor = conn.cursor()

        cursor.execute(f'INSERT INTO PRODUKTE(PRODUKTBEZEICHNUNG,PREIS, HERSTELLER) '
                       f'VALUES(:produktbezeichnung,:preis, :hersteller);',
                       {'produktbezeichnung': self.__produktbezeichnung,
                        'preis': self.__preis,
                        'hersteller': self.__hersteller})
        conn.commit()

        self.__produkt_id = int(cursor.lastrowid)

        conn.close()

        return int(self.__produkt_id)
