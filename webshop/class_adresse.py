import os

class Adresse():

    def __init__(self, adress_id: int, strasse: str, hausnummer: int, plz: str, stadt: str):
        self.__adress_id = int(adress_id)
        self.__strasse = str(strasse)
        self.__hausnummer = int(hausnummer)
        self.__plz = str(plz)
        self.__stadt = str(stadt)

    def get_adressinfo(self) -> str:
        return f'\n{self.__strasse} {self.__hausnummer} \n{self.__plz} {self.__stadt}\nID: {self.__adress_id}\n'





