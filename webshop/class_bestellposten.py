class Bestellposten():

    def __init__(self, posten_id: int, produkt_id: int, menge: int):
        self.__posten_id = posten_id
        self.__produkt_id = produkt_id
        self.__menge = menge


    def get_total(self):
        # todo: implement method to lookup the price the product and multiply by the quantity.
        pass

    def __get_produkt_from_db(self):
        self.__bestellposten = []

        conn = sqlite3.connect(self.__db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * from BESTELLPOSTEN WHERE BESTELL_ID = :bestell_id;",
                       {'bestell_id': self.__bestell_id})

        res = cursor.fetchall()
        conn.close()

        for ds in res:
            bestellposten = Bestellung(ds['POSTEN_ID'], ds['PRODUKT_ID'], ds['MENGE'])
            self.__bestellposten.append(bestellposten)
        pass
