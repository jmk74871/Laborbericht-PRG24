from webshop.class_produkt import Produkt


class Verdampfer(Produkt):

    def __init__(self, produkt_id, produktbezeichnung, preis, hersteller, durchmesser, hoehe, fuellsystem):
        super().__init__(produkt_id, produktbezeichnung, preis, hersteller)
        self.__hoehe = float(hoehe)
        self.__durchmesser = float(durchmesser)
        self.__fuellsystem = str(fuellsystem)


    def display_info(self):
        print(f'Verdampfer {self.__prodoktbezeichnung} mit einem Durchmesser von {self.__durchmesser}mm und Höhe '
              f'von {self.__hoehe}mm.\n Preis:{self.__preis}')

