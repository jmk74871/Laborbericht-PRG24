from class_bestellung import Bestellung


class Bestellposten():

    def __init__(self, id, bestell_id, produkt_id, menge):
        self.__id = id
        self.__bestell_id = bestell_id
        self.__produkt_id = produkt_id
        self.__menge = menge
