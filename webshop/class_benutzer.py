class Benutzer():
    def __init__(self, benutzer_id, benutzername, passwort):
        self.__logged_in = False
        self.__benutzer_id = int(benutzer_id)
        self.__benutzername = str(benutzername)
        self.__passwort = str(passwort)

    def einloggen(self, passwort):
        if passwort == self.__passwort:
            self.__logged_in = True




