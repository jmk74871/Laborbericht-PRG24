from class_benutzer import Benutzer
from class_adresse import Adresse
from class_bankverbindung import Bankverbindung

class Kunde(Benutzer):
    def __init__(self, benutzer_id, benutzer_name, passwort, vorname, nachname):
        super().__init__(benutzer_id, benutzer_name, passwort)
        self.__vorname = str(vorname)
        self.__nachname = str(nachname)
        self.__adresse = []
        self.__bankverbindung = []
        self.__bestellungen = []
        self.db_path = '../test_db.db'

    def add_adresse(self, strasse, hausnummer, plz, stadt):
        new_adress = Adresse(strasse, hausnummer, plz, stadt)
        if new_adress.save_to_db():
            self.__adresse.append(new_adress.get_id())
        pass

    def add_bankverbindung(self, kontoinhaber, iban, bic):
        new_bank_info = Bankverbindung(kontoinhaber, iban, bic)
        if new_bank_info.save_to_db():
            self.__bankverbindung.append(new_bank_info.get_id())

    def __get_adresses_from_db(self):
        #todo: implement method to get adresses from db.
        pass

    def __get_bankinfo_from_db(self):
        # todo: implement method to get adresses from db.
        pass

    def __get_bestellungen_from_db(self):
        # todo: implement method to get adresses from db.
        pass
