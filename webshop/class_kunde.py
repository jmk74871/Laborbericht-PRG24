import sqlite3
from webshop.class_adresse import Adresse
from webshop.class_bankverbindung import Bankverbindung
from webshop.class_benutzer import Benutzer
from webshop.class_bestellung import Bestellung


class Kunde(Benutzer):
    def __init__(self, benutzer_name: str, passwort: str) -> object:
        super().__init__(benutzer_name, passwort)
        self.__vorname = None
        self.__nachname = None
        self.__adresse = []
        self.__bankverbindung = []
        self.__bestellungen = []

        self.__einloggen()

    def __einloggen(self):
        if self._benutzer_einloggen():
            conn = sqlite3.connect(self._db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            cursor.execute("SELECT * from BENUTZER WHERE BENUTZER_ID = :benutzer_id",
                           {"benutzer_id": self._benutzer_id})

            res = cursor.fetchall()

            if len(res) == 1 and bool(res[0]['IS_KUNDE']):
                ds = res[0]
                self.__vorname = ds['VORNAME']
                self.__nachname = ds['NACHNAME']
                self._login_status = True
                print(f'Wilkommen {self._benutzername} Ihre Anmeldung war erfolgreich!')
            else:
                print('Login fehlgeschlagen! Bitte stellen SIe sicher, dass Sie das richtige Anmeldeportal verwenden.')
        else:
            self.create_new_account()

    def create_new_account(self) -> None:

        new_account = input('Möchten Sie ein neues Kundenkonto anlegen? (ja/nein)')
        if new_account == 'ja':
            vorname = input('Geben Sie ihren Vornamen an:')
            nachname = input('Geben Sie ihren Nachnamen an:')

            self.__benutzername = None
            while self.__benutzername is None:
                check_name = input('Bitte wählen Sie einen Benutzernamen aus.')
                if self._check_verfuegbar_benutzername(check_name):
                    self.__benutzername = check_name
                else:
                    print('Benutzername ist bereits vergeben.')

            self.__passwort = input('Geben Sie ein Passwort an:')

            conn = sqlite3.connect(self._db_path)
            cursor = conn.cursor()

            # add to BENUTZER-TABLE:
            cursor.execute("INSERT INTO BENUTZER (BENUTZERNAME, PASSWORT, IS_ADMIN, IS_KUNDE, VORNAME, NACHNAME) "
                           "VALUES(:benutzername, :passwort, :is_admin, :is_kunde, :vorname, :nachname)",
                           {'benutzername': benutzername, 'passwort': passwort, 'is_admin': False, 'is_kunde': True,
                            'vorname': vorname, 'nachname': nachname})
            print(f'{vorname} {nachname} wurde als Kunde mit dem Benutzernamen {self._benutzername} angelegt.')

            conn.commit()
            conn.close()

            self.__einloggen()

    def add_adresse(self, strasse: str, hausnummer: int, plz: str, stadt: str):
        new_adress = Adresse(strasse, hausnummer, plz, stadt)
        if new_adress.save_to_db():
            self.__adresse.append(new_adress.get_id())
        pass

    def add_bankverbindung(self, kontoinhaber, iban, bic):
        new_bank_info = Bankverbindung(kontoinhaber, iban, bic)
        if new_bank_info.save_to_db():
            self.__bankverbindung.append(new_bank_info.get_id())

    def __get_adresses_from_db(self):

        conn = sqlite3.connect(self.__db_path)

        cursor = conn.cursor()
        cursor.execute(f"SELECT from ADRESSEN WHERE BENUTZER_ID == {self.__benutzer_id}")
        for row in cursor:
            self.__adresse.append(Adresse(row[0], row[1], row[3], row[4], row[5]))

        conn.close()

    def __get_bankinfo_from_db(self):
        # todo: implement method to get adresses from db.
        pass

    def __get_bestellungen_from_db(self):
        # todo: implement method to get adresses from db.
        pass
