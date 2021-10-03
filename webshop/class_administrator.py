from webshop.class_benutzer import Benutzer
import sqlite3


class Administrator(Benutzer):
    def __init__(self, benutzer_name: str, passwort: str):
        super().__init__(benutzer_name, passwort)
        self.__personal_nummer = None
        self.__abteilung = None
        self.__einloggen()

    def add_verdampfer(self, produktbezeichnung: str, preis: float, hersteller: str, durchmesser: float, hoehe: float,
                       fuellsystem: str) -> None:

        # write to product table and get produkt_id:
        produkt_id = self.__save_to_prod_db(produktbezeichnung, preis, hersteller)

        if produkt_id > 0:
            conn = sqlite3.connect(self._db_path)
            cursor = conn.cursor()

            # add to VERDAMPFER-DB
            cursor.execute(
                f"INSERT INTO VERDAMPFER (PRODUKT_ID, DURCHMESSER,HOEHE, FUELLSYSTEM)"
                f"VALUES(:produkt_id, :durchmesser, :hoehe, :fuellsysystem);",
                {'produkt_id': produkt_id, 'durchmesser': durchmesser, 'hoehe': hoehe, 'fuellsysystem': fuellsystem})
            conn.commit()

            print(f'{produktbezeichnung} saved to db  with id: {produkt_id}')
        else:
            print('Insertion to db failed!')

    def add_verdampferkopf(self, produktbezeichnung: str, preis: float, hersteller: str, drahtmaterial: str,
                           wiederstand: float) -> None:
        # write to product table and get produkt_id:
        produkt_id = self.__save_to_prod_db(produktbezeichnung, preis, hersteller)

        if produkt_id > 0:
            conn = sqlite3.connect(self._db_path)
            cursor = conn.cursor()

            # add to VERDAMPFERKOEPFE-DB
            cursor.execute(
                f"INSERT INTO VERDAMPFERKOEPFE(PRODUKT_ID, DRAHTMATERIAL, WIEDERSTAND) "
                f"VALUES(:produkt_id, :drahtmaterial, :wiederstand);",
                {'produkt_id': produkt_id, 'drahtmaterial': drahtmaterial,
                 'wiederstand': wiederstand})
            conn.commit()

            print(f'{produktbezeichnung} saved to db  with id: {produkt_id}')
        else:
            print('Insertion to db failed!')

    def add_akkutaeger(self, produktbezeichnung: str, preis: float, hersteller: str, funktionsweise: str, hoehe: float,
                       breite: float, akkutyp: str) -> None:
        # write to product table and get produkt_id:
        produkt_id = self.__save_to_prod_db(produktbezeichnung, preis, hersteller)

        if produkt_id > 0:
            conn = sqlite3.connect(self._db_path)
            cursor = conn.cursor()

            # add to AKKUTRAEGER-DB
            cursor.execute(
                f"INSERT INTO AKKUTRAEGER(PRODUKT_ID, FUNKTIONSWEISE, HOEHE, BREITE, AKKUTYP) "
                f"VALUES(:produkt_id, :funktionsweise, :hoehe, :breite, :akkutyp);",
                {'produkt_id': produkt_id, 'funktionsweise': funktionsweise, 'hoehe': hoehe,
                 'breite': breite, 'akkutyp': akkutyp})
            conn.commit()

            print(f'{produktbezeichnung} saved to db  with id: {produkt_id}')
        else:
            print('Insertion to db failed!')

    def add_set(self, produktbezeichnung: str, preis: float, hersteller: str, akkutraeger_id: int, verdampfer_id: int,
                verdampferkopf_id: int) -> None:
        # write to product table and get produkt_id:
        produkt_id = self.__save_to_prod_db(produktbezeichnung, preis, hersteller)

        if produkt_id > 0:
            conn = sqlite3.connect(self._db_path)
            cursor = conn.cursor()

            # add to AKKUTRAEGER-DB
            cursor.execute(f"INSERT INTO STARTER_SETS(PRODUKT_ID, AKKUTRAEGER, VERDAMPFER, VERDAMPFERKOPF) "
                           f"VALUES(:produkt_id, :akkutaeger_id, :verdampfer_id, :verdampferkopf_id);",
                           {'produkt_id': produkt_id, 'akkutaeger_id': akkutraeger_id, 'verdampfer_id': verdampfer_id,
                            'verdampferkopf_id': verdampferkopf_id})
            conn.commit()

            print(f'{produktbezeichnung} saved to db  with id: {produkt_id}')
        else:
            print('Insertion to db failed!')

    def add_admin(self, benutzername: str, passwort: str, personalnummer: str, abteilung: str) -> None:

        conn = sqlite3.connect(self._db_path)
        cursor = conn.cursor()

        # add to BENUTZER-TABLE:
        cursor.execute("INSERT INTO BENUTZER (BENUTZERNAME, PASSWORT, IS_ADMIN, IS_KUNDE, PERSONALNUMMER, ABTEILUNG) "
                       "VALUES(:benutzername, :password, :is_admin, :is_kunde, :personalnummer, :abteilung)",
                       {'benutzername': benutzername, 'passwort': passwort, 'is_admin': True, 'is_kunde': False,
                        'personal_nummer': personalnummer, 'abteilung': abteilung})
        print(f'{benutzername} wurde als administrator angelegt.')
        conn.commit()
        conn.close()

    def define_matching(self, verdampfer_id: int, verdampferkopf_id: int):
        conn = sqlite3.connect(self._db_path)
        cursor = conn.cursor()

        # add to PASST_ZU-TABLE:
        cursor.execute("INSERT INTO PASST_ZU (VERDAMPFER_ID, VERDAMPFERKOPF_ID) "
                       "VALUES(:verdampfer_id, :verdampferkopf_id)",
                       {'verdampfer_id': verdampfer_id, 'verdampferkopf_id': verdampferkopf_id})
        conn.commit()
        conn.close()

    def __einloggen(self):
        if self._benutzer_einloggen():
            conn = sqlite3.connect(self._db_path)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()

            cursor.execute("SELECT * from BENUTZER WHERE BENUTZER_ID = :benutzer_id",
                           {"benutzer_id": self._benutzer_id})

            res = cursor.fetchall()

            if len(res) == 1 and bool(res[0]['IS_ADMIN']):
                ds = res[0]
                self.__personal_nummer = ds['PERSONALNUMMER']
                self.__abteilung = ds['ABTEILUNG']
                self._login_status = True
            else:
                print('Login fehlgeschlagen! Bitte benutze das Anmeldeportal für Kunden!')

    def __save_to_prod_db(self, produktbezeichnung: str, preis: float, hersteller: str) -> int:
        try:
            conn = sqlite3.connect(self._db_path)
            cursor = conn.cursor()

            # add to PRODUKT-DB
            cursor.execute(
                f"INSERT INTO PRODUKTE(PRODUKTBEZEICHNUNG,PREIS, HERSTELLER) "
                f"VALUES(:produktbezeichnung,:preis,:hersteller);",
                {'produktbezeichnung': produktbezeichnung, 'preis': preis, 'hersteller': hersteller})
            conn.commit()
            # get id
            produkt_id = int(cursor.lastrowid)
            conn.close()

            return produkt_id

        except Exception as e:
            print(e)
            return 0