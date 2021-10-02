import os

class Adresse():

    def __init__(self, adress_id: int, strasse: str, hausnummer: int, plz: str, stadt: str):
        self.__adress_id = int(adress_id)
        self.__strasse = str(strasse)
        self.__hausnummer = int(hausnummer)
        self.__plz = str(plz)
        self.__stadt = str(stadt)

        self.db_path = '../csv_db/adress_db.csv'

    def change_adresse(self, strasse_neu=None, hausnummer_neu=None, plz_neu=False, stadt_neu=None):

        if strasse_neu is not None:
            self.__strasse = strasse_neu
        if hausnummer_neu is not None:
            self.__hausnummer = hausnummer_neu
        if plz_neu is not None:
            self.__plz = plz_neu
        if stadt_neu is not None:
            self.__stadt = stadt_neu

    def get_adressinfo(self):
        return f'\n{self.__strasse} {self.__hausnummer} \n{self.__plz} {self.__stadt}\nID: {self.__adress_id}\n'





