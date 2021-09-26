from class_bestellung import Bestellung


class Bestellposten():

    def __init__(self, id, bestell_id, produkt_id, menge):
        self.__id = int(id)
        self.__bestell_id = int(bestell_id)
        self.__produkt_id = int(produkt_id)
        self.__menge = int(menge)
