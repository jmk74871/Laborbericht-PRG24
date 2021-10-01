class Bestellposten():

    def __init__(self, posten_id: int, produkt_id: int, menge: int):
        self.__posten_id = posten_id
        self.__produkt_id = produkt_id
        self.__menge = menge


    def get_total(self):
        # todo: implement method to lookup the price the product and multiply by the quantity.
        pass

    def __get_produkt_from_db(self):
        # todo: implement method to get the object for the product, so pricelookup and display info are available.
        pass
