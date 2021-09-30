import sqlite3

from webshop.class_produkt import Produkt

class Akkutraeger(Produkt):

    def __init__(self, produktbezeichnung: str, preis: float, hersteller: str, funktionsweise: str, hoehe: float, breite: float, akkutyp: str, produkt_id=None):
        super().__init__(produkt_id, produktbezeichnung, preis, hersteller, produkt_id)
        self.__funktionsweise = str(funktionsweise)
        self.__hoehe = float(hoehe)
        self.__bereite = float(breite)
        self.__akkutyp = str(akkutyp)

    def display_info(self):
        print(f'Verdampfer {self.__prodoktbezeichnung} mit einer Breite von {self.__breite} mm und Höhe '
              f'von {self.__hoehe}mm.\n Preis:{self._preis}')

    def save_to_db(self, db_path) -> None:
        if self._save_to_prod_db(db_path):
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # add to AKKUTRAEGER-DB
            cursor.execute(
                f"INSERT INTO AKKUTRAEGER(PRODUKT_ID, FUNKTIONSWEISE, HOEHE, BREITE, AKKUTYP) VALUES(:produkt_id, :funktionsweise, :hoehe, :breite, :akkutyp);" ,
                {'produkt_id': self._produkt_id, 'funktionsweise': self.__funktionsweise, 'hoehe': self.__hoehe, 'breite': self.__bereite, 'akkutyp': self.__akkutyp})
            conn.commit()

            print(f'{self._produktbezeichnung} saved to db  with id: {self._produkt_id}')
        else:
            print('Insertion to db failed!')

