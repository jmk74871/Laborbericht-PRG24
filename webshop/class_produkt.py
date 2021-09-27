class Produkt():

    def __init__(self, produkt_id: int, produktbezeichnung: str, preis: float, hersteller: str):
        self.__produkt_id = int(produkt_id)
        self.__produktbezeichnung = str(produktbezeichnung)
        self.__hersteller = str(hersteller)
        self.__preis = float(preis)

    def save_to_db(self):
        # todo: implement method to save data to db and return product_id.
        pass