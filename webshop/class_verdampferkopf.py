from webshop.class_produkt import Produkt


class Verdampferkopf(Produkt):

    def __init__(self, produkt_id: int, produktbezeichnung: str, preis: float, hersteller: str, drahtmaterial: str, wiederstand: float):
        super().__init__(produkt_id=produkt_id, produktbezeichnung=produktbezeichnung, preis=preis, hersteller=hersteller)
        self.__drahtmaterial = str(drahtmaterial)
        self.__wiederstand = float(wiederstand)

    def display_info(self):
        print(f'Verdampferkopf {self._produktbezeichnung} mit {self.__drahtmaterial}-Draht und einem Wiederstand '
              f'von {self.__wiederstand} Ohm. \nPreis:{self._preis}')

    def display_matching(self):
        # todo: method to display matching verdampfer.
        print('Passende Verdampfer zu diesem Verdampferkopf sind:\n')
        #
        # for row in search:
        #     pass
        #
        pass
