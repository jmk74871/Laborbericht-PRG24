from webshop.class_produkt import Produkt


class Starterset(Produkt):

    def __init__(self, produkt_id, produktbezeichnung, preis, hersteller, akkutraeger, verdampfer, verdampferkopf):
        super().__init__(produkt_id, produktbezeichnung, preis, hersteller)
        # toDO: load/create objects for the components on creation.

    def get_info(self):
        print(f'Das Set {self.__prodoktbezeichnung} enthält:\n')

        # for component in components:
        #     component.display_info()

        print(f'Preis:{self._preis}  /  Produkt-ID: {self._produkt_id}')
