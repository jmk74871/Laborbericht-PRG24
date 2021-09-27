from class_produkt import Produkt


class Verdampferkopf(Produkt):

    def __init__(self, produkt_id, produktbezeichnung, preis, hersteller, drahtmaterial, wiederstand):
        super().__init__(produkt_id, produktbezeichnung, preis, hersteller)
        self.__drahtmaterial = str(drahtmaterial)
        self.__wiederstand = float(wiederstand)

    def display_info(self):
        print(f'Verdampferkopf {self.__prodoktbezeichnung} mit {self.__drahtmaterial}-Draht und einem Wiederstand '
              f'von {self.__wiederstand} Ohm. \nPreis:{self.__preis}')

    def display_matching(self):
        # todo: method to display matching verdampfer.
        pass
