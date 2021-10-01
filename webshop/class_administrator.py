from webshop.class_benutzer import Benutzer
import sqlite3


class Administrator(Benutzer):
    def __init__(self, benutzer_name: str, passwort: str, personal_nummer: str = 'none', abteilung: str = 'none',
                 benutzer_id: int = None):
        super().__init__(benutzer_name, passwort, benutzer_id)
        self.__personal_nummer = str(personal_nummer)
        self.__abteilung = str(abteilung)



    def __save_to_prod_db(self, produktbezeichnung: str, preis: float, hersteller: str, db_path: str) -> int:
        try:
            conn = sqlite3.connect(db_path)
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

        except SQLiteException as eception:
            print(eception)
            return None

        return produkt_id

    def add_verdampfer(self, produktbezeichnung: str, preis: float, hersteller: str, durchmesser: float, hoehe: float,
                       fuellsystem: str, db_path: str) -> None:

        # write to product table and get produkt_id:
        produkt_id = self.__save_to_prod_db(produktbezeichnung, preis, hersteller, db_path)

        if produkt_id is not None:
            conn = sqlite3.connect(db_path)
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
                           wiederstand: float, db_path: str) -> None:
        # write to product table and get produkt_id:
        produkt_id = self.__save_to_prod_db(produktbezeichnung, preis, hersteller, db_path)

        if produkt_id is not None:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # add to VERDAMPFERKOEPFE-DB
            cursor.execute(
                f"INSERT INTO VERDAMPFERKOEFE(PRODUKT_ID, DRAHTMATERIAL, WIEDERSTAND) "
                f"VALUES(:produkt_id, :drahtmaterial, :wiederstand);",
                {'produkt_id': produkt_id, 'drahtmaterial': drahtmaterial,
                 'wiederstand': wiederstand})
            conn.commit()

            print(f'{produktbezeichnung} saved to db  with id: {produkt_id}')
        else:
            print('Insertion to db failed!')

    def add_akkutaeger(self, produktbezeichnung: str, preis: float, hersteller: str, funktionsweise: str, hoehe: float,
                       breite: float, akkutyp: str, db_path: str) -> None:
        # write to product table and get produkt_id:
        produkt_id = self.__save_to_prod_db(produktbezeichnung, preis, hersteller, db_path)

        if produkt_id is not None:
            conn = sqlite3.connect(db_path)
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
                verdampferkopf_id: int, db_path: str) -> None:
        # write to product table and get produkt_id:
        produkt_id = self.__save_to_prod_db(produktbezeichnung, preis, hersteller, db_path)

        if produkt_id is not None:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()

            # add to AKKUTRAEGER-DB
            cursor.execute(
                f"INSERT INTO STARTER_SETS(PRODUKT_ID, AKKUTRAEGER, VERDAMPFER, VERDAMPFERKOPF) "
                f"VALUES(:produkt_id, :akkutaeger_id, :verdampfer_id, :verdampferkopf_id);",
                {'produkt_id': produkt_id, 'akkutraeger_id': akkutraeger_id, 'verdampfer_id': verdampfer_id,
                 'verdampferkopf_id': verdampferkopf_id})
            conn.commit()

            print(f'{produktbezeichnung} saved to db  with id: {produkt_id}')
        else:
            print('Insertion to db failed!')

    def add_admin(self, benutzername: str, passwort: str, personalnummer: str, abteilung: str) -> None:

        conn = sqlite3.connect('../test_db.db')
        cursor = conn.cursor()

        # add to BENUTZER-TABLE:
        cursor.execute("INSERT INTO BENUTZER (BENUTZERNAME, PASSWORT, IS_ADMIN, ISKUNDE, PERSONALNUMMER, ABTEILUNG) "
                       "VALUES(:benutzername, :password, :is_admin, :is_kunde, :personalnummer, :abteilung)",
                       {'benutzername': benutzername, 'passwort': passwort, 'is_admin': True, 'is_kunde': False,
                        'personal_nummer': personalnummer, 'abteilung': abteilung})
        print(f'{benutzername} wurde als administrator angelegt.')
        conn.commit()
        conn.close()
