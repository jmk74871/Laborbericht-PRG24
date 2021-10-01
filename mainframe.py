import webshop, sqlite3


class Mainframe():
    def __init__(self):
        self.db_path = 'test_db.db'
        self.user = None

    def einloggen(self, username, password) -> None:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * from BENUTZER WHERE BENUTZERNAME = :name AND PASSWORT = :pw",
                       {"name": username, "pw": password})

        res = cursor.fetchall()

        if len(res) == 1:
            ds = res[0]
            if bool(ds['IS_ADMIN']) and self.__class__:
                self.user = webshop.class_administrator.Administrator(benutzer_id=ds['BENUTZER_ID'],
                                                                      benutzer_name=ds['BENUTZERNAME'],
                                                                      passwort=ds['PASSWORT'],
                                                                      personal_nummer=ds['PERSONALNUMMER'],
                                                                      abteilung=ds['ABTEILUNG'])
            elif bool(ds['IS_KUNDE']):
                self.user = webshop.class_kunde.Kunde(benutzer_id=ds['BENUTZER_ID'],
                                                      benutzer_name=ds['BENUTZERNAME'],
                                                      passwort=ds['PASSWORT'],
                                                      vorname=ds['VORNAME'],
                                                      nachname=ds['NACHNAME'])
        else:
            print('Login fehlgeschlagen!')

        conn.close()

    def ausloggen(self):
        self.user = None
        print('Abmeldung erfolgreich!')
