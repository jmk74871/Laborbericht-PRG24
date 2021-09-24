import os

class Adresse():

    def __init__(self, strasse, hausnummer, plz, stadt, adress_id=None):
        self.__strasse = strasse
        self.__hausnummer = hausnummer
        self.__plz = plz
        self.__stadt = stadt
        self.__adress_id = adress_id
        if adress_id is None:
            self.__adress_id = self.request_id()
        self.db_path = '../csv_db/adress_db.csv'

    def __request_id():
        # ToDO: create method to get a unique id
        pass

    def change_adresse(self, strasse_neu=None, hausnummer_neu=None, plz_neu=False, stadt_neu=None):

        if strasse_neu is not None:
            self.__strasse = strasse_neu
        if hausnummer_neu is not None:
            self.__hausnummer = hausnummer_neu
        if plz_neu is not None:
            self.__plz = plz_neu
        if stadt_neu is not None:
            self.__stadt = stadt_neu

    def display_adresse(self):
        print(f'{self.__strasse} {self.__hausnummer} \n {self.__plz} {self.__stadt}')

    def get_id(self):
        return self.__adress_id

    def save_to_db(self):
        # ToDO: create method to save to db
        return True




