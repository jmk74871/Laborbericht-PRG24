from webshop.class_produkt import Produkt


class Verdampferkopf(Produkt):

    def __init__(self, produkt_id, produktbezeichnung, preis, hersteller, drahtmaterial, wiederstand):
        super().__init__(produkt_id, produktbezeichnung, preis, hersteller)
        self.__drahtmaterial = str(drahtmaterial)
        self.__wiederstand = float(wiederstand)

    def display_info(self):
        print(f'Verdampferkopf {self.__prodoktbezeichnung} mit {self.__drahtmaterial}-Draht und einem Wiederstand '
              f'von {self.__wiederstand} Ohm. \nPreis:{self._preis}')

    def save_to_db(self, db_path) -> None:
        if self._save_to_prod_db(db_path):
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # add to VERDAMPFERKOEPFE-DB
            cursor.execute(
                f"INSERT INTO VERDAMPFERKOEFE(PRODUKT_ID, DRAHTMATERIAL, WIEDERSTAND) VALUES(:produkt_id, :drahtmaterial, :wiederstand);",
                {'produkt_id': self._produkt_id, 'drahtmaterial': self.__drahtmaterial, 'wiederstand': self.__wiederstand})
            conn.commit()

            print(f'{self._produktbezeichnung} saved to db  with id: {self._produkt_id}')
        else:
            print('insertion to db failed!')

    def display_matching(self):
        # todo: method to display matching verdampfer.
        print('Passende Verdampfer zu diesem Verdampferkopf sind:\n')
        #
        # for row in search:
        #     pass
        #
        pass
