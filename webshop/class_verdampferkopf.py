from webshop.class_produkt import Produkt


class Verdampferkopf(Produkt):

    def __init__(self, produkt_id: int, produktbezeichnung: str, preis: float, hersteller: str, drahtmaterial: str,
                 wiederstand: float, passende_produkte: list):
        super().__init__(produkt_id=produkt_id, produktbezeichnung=produktbezeichnung, preis=preis, hersteller=hersteller)
        self.__drahtmaterial = str(drahtmaterial)
        self.__wiederstand = float(wiederstand)
        self.__passende_produkte = passende_produkte

    def get_info(self):
        return f'Verdampferkopf {self._produktbezeichnung} mit {self.__drahtmaterial}-Draht und einem Wiederstand ' \
               f'von {self.__wiederstand} Ohm. \n   Preis:{self._preis}  /  Produkt-ID: {self._produkt_id}'

    def display_matching(self):
        print('Passende Verdampfer zu diesem Verdampferkopf sind:\n')


        pass
