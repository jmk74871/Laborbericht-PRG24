class Bestellposten():

    def __init__(self, posten_id, produkt_id, menge):
        self.__posten_id = int(posten_id)
        self.__produkt_id = int(produkt_id)

    def get_total(self):
        # todo: implement method to lookup the price the product and multiply by the quantity.
        pass
