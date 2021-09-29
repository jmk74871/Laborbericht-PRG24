from webshop.class_benutzer import Benutzer
import sqlite3


class Administrator(Benutzer):
    def __init__(self, benutzer_name: str, passwort: str, personal_nummer: str = 'none', abteilung: str = 'none',
                 benutzer_id: int = None):
        super().__init__(benutzer_name, passwort, benutzer_id)
        self.__personal_nummer = str(personal_nummer)
        self.__abteilung = str(abteilung)

    def __add_product(self, produktbezeichnung, preis, hersteller):
        conn = sqlite3.connect('../test_db.db')
        cursor = conn.cursor()

        # add to PRODUKT-DB
        cursor.execute(f"INSERT INTO PRODUKTE(PRODUKTBEZEICHNUNG,PREIS, HERSTELLER) VALUES('{produktbezeichnung}','{preis}, {hersteller}');")
        cursor.commit()

        produkt_id = cursor.lastrowid()

        conn.close()

        return int(produkt_id)


    def __add_kunde(benutzer_name, passwort, vorname, nachname):

        conn = sqlite3.connect('../test_db.db')

        # add Benutzer to DB
        conn.execute(f"INSERT INTO BENUTZER(BENUTZERNAME,PASSWORT) VALUES('{benutzer_name}','{passwort}');")
        conn.commit()

        # find benutzer_id
        cursor = conn.execute(f"SELECT ID,BENUTZERNAME from BENUTZER")
        for row in cursor:
            if benutzer_name == row[1]:
                benutzer_id = row[0]

        # add Kunde to DB
        conn.execute(f"INSERT INTO KUNDE(BENUTZER_ID,VORNAME,NACHNAME) VALUES({benutzer_id},'{vorname}','{nachname}');")
        conn.commit()

        conn.close()
