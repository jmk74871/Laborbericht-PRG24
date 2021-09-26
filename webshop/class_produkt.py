class Produkt():

    def __init__(self, produkt_id, produktbezeichnung, preis, hersteller, beschreibung):
        self.__produkt_id = int(produkt_id)
        self.__produktbezeichnung = str(produktbezeichnung)
        self.__hersteller = str(hersteller)
        self.__preis = float(preis)
        self.__beschreibung = str(beschreibung)

    def get_price(self):
        return self.__preis