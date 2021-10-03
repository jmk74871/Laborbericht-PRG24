import sqlite3


class Benutzer():
    def __init__(self, benutzername: str, passwort: str):

        self._benutzername = str(benutzername)
        self.__passwort = str(passwort)

        self._db_path = 'test_db.db'
        self._login_status = False
        self._benutzer_id = None

    def ausloggen(self) -> None:
        self._login_status = False

    def _benutzer_einloggen(self) -> bool:
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * from BENUTZER WHERE BENUTZERNAME = :name AND PASSWORT = :pw",
                       {"name": self._benutzername, "pw": self.__passwort})

        res = cursor.fetchall()

        if len(res) == 1:
            ds = res[0]
            self._benutzer_id = ds['BENUTZER_ID']
            return True
        else:
            print('Login fehlgeschlagen! Bitte lege ein passendes Benutzerkonto an.')
            return False

    def _check_verfuegbar_benutzername(self, name_to_check: str) -> bool:
        conn = sqlite3.connect(self._db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * from BENUTZER WHERE BENUTZERNAME = :name", {"name": name_to_check})
        res = cursor.fetchall()

        if len(res) == 0:
            conn.close()
            return True
        else:
            conn.close()
            return False
