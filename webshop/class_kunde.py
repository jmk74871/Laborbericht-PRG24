import sqlite3, datetime
from webshop.class_adresse import Adresse
from webshop.class_bankverbindung import Bankverbindung
from webshop.class_benutzer import Benutzer
from webshop.class_bestellung import Bestellung
from webshop.class_warenhaus import Warenhaus


class Kunde(Benutzer):
    def __init__(self, benutzer_name: str, passwort: str, warenhaus: Warenhaus) -> object:
        super().__init__(benutzer_name, passwort)
        self.__warenhaus = warenhaus
        self.__vorname = None
        self.__nachname = None
        self.__adressen = []
        self.__bankverbindungen = []
        self.__warenkorb = self.__neuer_warenkorb()
        self.__bestellhistorie = []

        self.__einloggen()

        if self._login_status:
            self.__get_adressen_from_db()
            self.__get_bankinfo_from_db()
            self.__get_bestellungen_from_db()

    # Öffentliche Schnittstellen:

    def add_adresse(self, strasse: str, hausnummer: int, plz: str, stadt: str):
        if self._login_status:
            conn = sqlite3.connect(self._db_path)
            cursor = conn.cursor()

            # add to ADRESS-DB
            cursor.execute(
                f"INSERT INTO ADRESSEN (BENUTZER_ID, STRASSE, HAUSNUMMER, PLZ, STADT)"
                f"VALUES(:benutzer_id, :strasse, :hausnummer, :plz, :stadt);",
                {'benutzer_id': self._benutzer_id, 'strasse': strasse, 'hausnummer': hausnummer,
                 'plz': plz, 'stadt': stadt})
            conn.commit()

            print(f'Adresse in der {strasse} {hausnummer} in {stadt} erfolgreich angelegt.')

            self.__get_adressen_from_db()

        else:
            print('Bitte zuerst anmelden.')

    def add_bankverbindung(self, kontoinhaber: str, iban: str, bic: str):
        if self._login_status:
            conn = sqlite3.connect(self._db_path)
            cursor = conn.cursor()

            # add to ADRESS-DB
            cursor.execute(
                f"INSERT INTO BANKVERBINDUNGEN (BENUTZER_ID, KONTOINHABER, IBAN, BIC)"
                f"VALUES(:benutzer_id, :kontoinhaber, :iban, :bic);",
                {'benutzer_id': self._benutzer_id, 'kontoinhaber': kontoinhaber, 'iban': iban, 'bic': bic})
            conn.commit()

            print(f'Bankverbindung mit der IBAN endend auf {iban[-4:]} erfolgreich angelegt.')

            self.__get_bankinfo_from_db()

        else:
            print('Bitte zuerst anmelden.')

    def zum_warenkorb_hinzufuegen(self, produkt_id: int, menge: int):
        self.__warenkorb._add_bestellposten(produkt_id, menge)

    def warenkorb_anzeigen(self) -> None:
        print(self.__warenkorb._warenkorb_anzeigen())



    # Interne Methoden:

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
            self.__create_new_account()

    def __create_new_account(self) -> None:

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
                           {'benutzername': self.__benutzername, 'passwort': self.__passwort, 'is_admin': False, 'is_kunde': True,
                            'vorname': vorname, 'nachname': nachname})
            print(f'{vorname} {nachname} wurde als Kunde mit dem Benutzernamen {self._benutzername} angelegt.')

            conn.commit()
            conn.close()

            self.__einloggen()

    def __get_adressen_from_db(self):

        self.__adressen = []

        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * from ADRESSEN WHERE BENUTZER_ID = :benutzer_id;", {'benutzer_id': self._benutzer_id,})

        res = cursor.fetchall()
        conn.close()

        for ds in res:
            adresse = Adresse(ds['ADRESS_ID'], ds['STRASSE'], ds['HAUSNUMMER'], ds['PLZ'], ds['STADT'])
            self.__adressen.append(adresse)

    def __get_bankinfo_from_db(self):
        self.__bankverbindungen = []

        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * from BANKVERBINDUNGEN WHERE BENUTZER_ID = :benutzer_id;", {'benutzer_id': self._benutzer_id, })

        res = cursor.fetchall()
        conn.close()

        for ds in res:
            bankverbindung = Bankverbindung(ds['BANK_ID'], ds['KONTOINHABER'], ds['IBAN'], ds['BIC'])
            self.__bankverbindungen.append(bankverbindung)

    def __get_bestellungen_from_db(self):
        self.__bestellhistorie = []

        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * from BESTELLUNGEN WHERE BENUTZER_ID = :benutzer_id;",
                       {'benutzer_id': self._benutzer_id})

        res = cursor.fetchall()
        conn.close()

        for ds in res:
            bestellung = Bestellung(db_path=self._db_path, bestell_id=ds['BESTELL_ID'],
                                    bestelldatum=ds['BESTELLDATUM'], bestellstatus=ds['STATUS'], warenhaus=self.__warenhaus)
            self.__bestellhistorie.append(bestellung)

    def __neuer_warenkorb(self):
        # todo: methode wirklich nötig?
        bestellung = Bestellung(db_path=self._db_path, warenhaus=self.__warenhaus)
        return bestellung

