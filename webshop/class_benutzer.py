class Benutzer():
    def __init__(self, benutzer_id, benutzer_name, passwort):
        self.__logged_in = False
        self.__benutzer_id = int(benutzer_id)
        self.__benutzer_name = str(benutzer_name)
        self.__passwort = str(passwort)

    def einloggen(self, passwort):
        if passwort == self.__passwort:
            self.__logged_in = True




