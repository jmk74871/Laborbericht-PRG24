class Bankverbindung():

    def __init__(self, bank_id, kontoinhaber, iban, bic):
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

    def get_bankinfo(self):
        return f'\nKontoinhaber: {self.__kontoinhaber}\nIban: {self.__iban} \nBIC: {self.__bic}' \
               f'\nID: {self.__bank_id}\n'

    def get_id(self):
        return self.__bank_id


