from class_produkt import Produkt


class Starterset(Produkt):

    def __init__(self, produkt_id, produktbezeichnung, preis, hersteller, akkutraeger, verdampfer, verdampferkopf):
        super().__init__(produkt_id, produktbezeichnung, preis, hersteller)
        # toDO: load/create objects for the components on creation.

    def display_info(self):
        print(f'Verdampferkopf {self.__prodoktbezeichnung} mit {self.__drahtmaterial}-Draht und einem Wiederstand '
              f'von {self.__wiederstand} Ohm. \nPreis:{self.__preis}')
