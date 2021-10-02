from webshop.class_produkt import Produkt


class Starterset(Produkt):

    def __init__(self, produkt_id: int, produktbezeichnung: str, preis: float, hersteller: str, akkutraeger: int,
                 verdampfer: int, verdampferkopf: int):
        super().__init__(produkt_id=produkt_id, produktbezeichnung=produktbezeichnung, preis=preis,
                         hersteller=hersteller)
        self.__akkutaeger = akkutraeger
        self.__verdampfer = verdampfer
        self.__verdampferkopf = verdampferkopf

    def get_info(self):
        return {'head': f'\nDas Set {self._produktbezeichnung} enthält:',
                'components': [self.__akkutaeger, self.__verdampfer, self.__verdampferkopf],
                'tail': f'Setpreis: {self._preis}€  /  Set-Produkt-ID: {self._produkt_id}\n'}




