from webshop.class_benutzer import Benutzer
import sqlite3


class Administrator(Benutzer):
    def __init__(self, benutzer_name: str, passwort: str, personal_nummer: str = 'none', abteilung: str = 'none',
                 benutzer_id: int = None):
        super().__init__(benutzer_name, passwort, benutzer_id)
        self.__personal_nummer = str(personal_nummer)
        self.__abteilung = str(abteilung)

    def __get_product_by_id(self, produkt_id: str, tabelle: str, db_path: str):
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * from :tabelle WHERE PRODUKT_ID = :produkt_id",
                       {'tabelle': tabelle, 'produkt_id': produkt_id})
        produkt = cursor.fetchone()

        return produkt

    def add_produkt(self, produkt: object, db_path: str):
        try:
            produkt.save_to_db(db_path, self)
        except AttributeError as exception:
            print(exception)
            print('Es steht keine passende Funktionalität zum speichern dieses Produktes zur Verfügung.')

    def add_admin(self, benutzername: str, passwort: str, personalnummer: str, abteilung:str):

        conn = sqlite3.connect('../test_db.db')
        cursor = conn.cursor()

        #add to BENUTZER-TABLE:
        cursor.execute("INSERT INTO BENUTZER (BENUTZERNAME, PASSWORT, IS_ADMIN, ISKUNDE, PERSONALNUMMER, ABTEILUNG) "
                       "VALUES(:benutzername, :password, :is_admin, :is_kunde, :personalnummer, :abteilung)",
                       {'benutzername': benutzername, 'passwort':passwort, 'is_admin':True, 'is_kunde': Flase,
                        'personal_nummer': personalnummer, 'abteilung': abteilung})
        print(f'{benutzername} wurde als administrator angelegt.')
        conn.commit()
        conn.close()

    def add_set_by_id(self, akkutraeger_id: int, verdampfer_id: int, verdampferkopf_id: int, produktbezeichnung: str, preis: float, hersteller: str):
        # todo: find way to create new sets from existing products.
        pass
