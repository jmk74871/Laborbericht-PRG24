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

    def save_to_db(self, db_path) -> None:
        if self._save_to_prod_db(db_path):
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # add to VERDAMPFER-DB
            cursor.execute(
                f"INSERT INTO VERDAMPFER(PRODUKT_ID, DURCHMESSER,HOEHE, FUELLSYSTEM) VALUES(:produkt_id, :durchmesser, :hoehe, :fuellsysystem);",
                {'produkt_id': self._produkt_id, 'durchmesser': self.__durchmesser, 'hoehe': self.__hoehe,
                 'fuellsysystem': self.__fuellsystem})
            conn.commit()

            print(f'{self._produktbezeichnung} saved to db  with id: {self._produkt_id}')
        else:
            print('insertion to db failed!')
