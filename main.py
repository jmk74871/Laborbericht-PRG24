import sqlite3
import os.path


def setup_database():
    conn = sqlite3.connect('test_db.db')

    print('DB created successfully!')

    conn.execute('''CREATE TABLE BENUTZER
             (ID INTEGER NOT NULL UNIQUE,
             BENUTZERNAME TEXT NOT NULL UNIQUE,
             PASSWORT TEXT NOT NULL,
             PRIMARY KEY("ID" AUTOINCREMENT));''')
    print('Table BENUTZER created successfully!')

    conn.execute('''CREATE TABLE ADMINISTRATOR
             (ID INTEGER NOT NULL UNIQUE,
             BENUTZER_ID INT NOT NULL,             
             PERSONALNUMMER TEXT NOT NULL,
             ABTEILUNG TEXT,
             PRIMARY KEY("ID" AUTOINCREMENT),
             FOREIGN KEY(BENUTZER_ID) REFERENCES BENUTZER(ID) ON DELETE CASCADE);''')
    print('Table ADMINISTRATOR created successfully!')

    conn.execute('''CREATE TABLE "ADRESSE" 
                ("ID"	INTEGER NOT NULL UNIQUE,
                "KUNDEN_ID"	INTEGER NOT NULL,
                "STRASSE"	TEXT NOT NULL,
                "HAUSNUMMER"	INTEGER NOT NULL,
                "PLZ" INTEGER NOT NULL,
                "STADT" TEXT NOT NULL,
                PRIMARY KEY("ID" AUTOINCREMENT),
                FOREIGN KEY("KUNDEN_ID") REFERENCES KUNDE(ID) ON DELETE CASCADE);''')
    print('Table ADRESSE created successfully!')

    conn.execute('''CREATE TABLE "BANKVERBINDUNG" 
                ("ID"	INTEGER NOT NULL UNIQUE,
                "KUNDEN_ID"	INTEGER NOT NULL,
                "KONTOINHABER"	TEXT NOT NULL,
                "IBAN"	TEXT NOT NULL,
                "BIC" TEXT NOT NULL,
                PRIMARY KEY("ID" AUTOINCREMENT),
                FOREIGN KEY("KUNDEN_ID") REFERENCES BENUTZER(ID) ON DELETE CASCADE);''')
    print('Table BANKVERBINDUNG created successfully!')

    conn.execute('''CREATE TABLE "KUNDE" 
            ("ID"	INTEGER NOT NULL UNIQUE,
            "BENUTZER_ID"	INTEGER NOT NULL,
            "ADRESSE"	INTEGER,
            "BANKVERBINDUNG"	INTEGER,
            PRIMARY KEY("ID" AUTOINCREMENT),
            FOREIGN KEY("ADRESSE") REFERENCES ADRESSE(ID),
            FOREIGN KEY("BANKVERBINDUNG") REFERENCES BANKVERBINDUNG(ID),
            FOREIGN KEY("BENUTZER_ID") REFERENCES BENUTZER(ID) ON DELETE CASCADE);''')
    print('Table KUNDE created successfully!')

    conn.close()
    print('Connection to DB closed')

    add_admin()


def add_admin():
    conn = sqlite3.connect('test_db.db')

    conn.execute(f"INSERT INTO BENUTZER(BENUTZERNAME,PASSWORT) VALUES('admin','admin');")
    conn.commit()

    cursor = conn.execute(f"SELECT ID,BENUTZERNAME from BENUTZER")
    for row in cursor:
        if 'admin' == row[1]:
            benutzer_id = row[0]

    conn.execute(
        f"INSERT INTO ADMINISTRATOR(BENUTZER_ID,PERSONALNUMMER,ABTEILUNG) VALUES({benutzer_id},'SHOPADMIN','IT');")
    conn.commit()

    print('admin created successfully')

    conn.close()


def main():
    if not os.path.exists('test_db.db'):
        setup_database()
    pass


if __name__ == "__main__":
    main()
