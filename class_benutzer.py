class Benutzer():
    def __init__(self, benutzer_id, benutzer_name, passwort):
        self.__logged_in = False
        self.__benutzer_id = benutzer_id
        self.__benutzer_name = benutzer_name
        self.__passwort = passwort

    def einloggen(self, passwort):
        if passwort == self.__passwort:
            self.__logged_in = True




