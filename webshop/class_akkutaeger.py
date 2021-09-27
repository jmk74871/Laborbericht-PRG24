from webshop.class_produkt import Produkt

class Akkutraeger(Produkt):

    def __init__(self, produkt_id, produktbezeichnung, preis, hersteller, funktionsweise, hoehe, breite, akkutyp):
        super().__init__(produkt_id, produktbezeichnung, preis, hersteller)
        self.__funktionsweise = str(funktionsweise)
        self.__hoehe = float(hoehe)
        self.__bereite = float(breite)
        self.__akkutyp = str(akkutyp)

    def display_info(self):
        print(f'Verdampfer {self.__prodoktbezeichnung} mit einer Breite von {self.__breite} mm und Höhe '
              f'von {self.__hoehe}mm.\n Preis:{self.__preis}')

