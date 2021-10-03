class Bankverbindung():

    def __init__(self, bank_id, kontoinhaber, iban, bic):
        self.__kontoinhaber = str(kontoinhaber)
        self.__iban = str(iban)
        self.__bic = str(bic)
        self.__bank_id = int(bank_id)

    def get_bankinfo(self) -> str:
        return f'\nKontoinhaber: {self.__kontoinhaber}\nIban: {self.__iban} \nBIC: {self.__bic}' \
               f'\nID: {self.__bank_id}\n'

    def get_id(self) -> int:
        return self.__bank_id


