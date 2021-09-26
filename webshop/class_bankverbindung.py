class Bankverbindung():

    def __init__(self, kontoinhaber, iban, bic, bank_id=None):
        self.__kontoinhaber = str(kontoinhaber)
        self.__iban = str(iban)
        self.__bic = str(bic)
        self.__bank_id = int(bank_id)
        self.db_path = '../csv_db/bank_info_db.csv'

    def change_bankinfo(self, kontoinhaber_neu=None, iban_neu=None, bic_neu=False):

        if kontoinhaber_neu is not None:
            self.__kontoinhaber = kontoinhaber_neu
        if iban_neu is not None:
            self.__iban = iban_neu
        if bic_neu is not None:
            self.__bic = bic_neu

    def display_bankinfo(self):
        print(f'Kontoinhaber: {self.__kontoinhaber} \n\n Iban: {self.__iban} \n\n bic: {self.__bic}')

    def get_id(self):
        return self.__bank_id

    def save_to_db(self):
        # ToDO: create method to save to db
        pass

