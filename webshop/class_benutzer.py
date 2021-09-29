import sqlite3


class Benutzer():
    def __init__(self, benutzername: str, passwort: str, benutzer_id: int = None):
        if benutzer_id is not None:
            self.__benutzer_id = int(benutzer_id)
        else:
            self.__benutzer_id = None
        self.__benutzername = str(benutzername)
        self.__passwort = str(passwort)
        self.__db_path = 'test_db.db'

    # def _einloggen(self) -> object:
    #
    #     conn = sqlite3.connect(self.__db_path)
    #     conn.row_factory = sqlite3.Row
    #     cursor = conn.cursor()
    #
    #     cursor.execute("SELECT * from BENUTZER WHERE BENUTZERNAME = :name AND PASSWORT = :pw", {"name": self.__benutzername, "pw": self.__passwort})
    #
    #     res = cursor.fetchall()
    #
    #     if len(res) == 1:
    #         ds = res[0]
    #         if bool(ds['IS_ADMIN']) and self.__class__:
    #             user = Administrator(benutzer_id=ds['BENUTZER_ID'], benutzer_name=ds['BENUTZERNAME'], passwort=ds['PASSWORT'], personal_nummer=ds['PERSONALNUMMER'], abteilung=ds['ABTEILUNG'])
    #         elif bool(ds['IS_KUNDE']):
    #             user = Kunde(benutzer_id=ds['BENUTZER_ID'], benutzer_name=ds['BENUTZERNAME'], passwort=ds['PASSWORT'], vorname=ds['VORNAME'], nachname=ds['NACHNAME'])
    #         return user
    #     else:
    #         print('Login fehlgeschlagen!')
    #         return self