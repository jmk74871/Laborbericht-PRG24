from class_benutzer import Benutzer

class Administrator(Benutzer):
    def __init__(self, benutzer_id, benutzer_name, passwort, personal_nummer, abteilung):
        super().__init__(benutzer_id, benutzer_name, passwort)
        self.__personal_nummer = personal_nummer
        self.__abteilung = abteilung

    def add_product(self):
        pass