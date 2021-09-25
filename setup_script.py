import sqlite3

def setup_database():
    conn = sqlite3.connect('test_db.db')
    print('DB created successfully!')

    conn.execute("PRAGMA foreign_keys=on;")

    conn.execute('''CREATE TABLE "BENUTZER" (
        "ID"	INTEGER NOT NULL UNIQUE,
        "BENUTZERNAME"	TEXT NOT NULL UNIQUE,
        "PASSWORT"	TEXT NOT NULL,
        "IS_ADMIN"	INTEGER NOT NULL,
        "IS_KUNDE"	INTEGER NOT NULL,
        "PERSONALNUMMER" TEXT,
        "ABTEILUNG" TEXT,
        "VORNAME" TEXT ,
        "NACHNAME" TEXT,
        "ADRESSE"	INTEGER,
        "BANKVERBINDUNG"	INTEGER,
        "BESTELLUNGEN" INTEGER UNIQUE,
        PRIMARY KEY("ID" AUTOINCREMENT)
        FOREIGN KEY("ADRESSE") REFERENCES ADRESSEN(ID),
        FOREIGN KEY("BESTELLUNGEN") REFERENCES BESTELLUNGEN(ID),
        FOREIGN KEY("BANKVERBINDUNG") REFERENCES BANKVERBINDUNGEN(ID));
             ''')
    print('Table BENUTZER created successfully!')

    # conn.execute('''CREATE TABLE "ADMINISTRATOREN"
    #      (ID INTEGER NOT NULL UNIQUE,
    #      BENUTZER_ID INT NOT NULL,
    #      PERSONALNUMMER TEXT NOT NULL,
    #      ABTEILUNG TEXT,
    #      PRIMARY KEY("ID" AUTOINCREMENT),
    #      FOREIGN KEY(BENUTZER_ID) REFERENCES BENUTZER(ID) ON DELETE CASCADE);
    #          ''')
    # print('Table ADMINISTRATOR created successfully!')
    #
    # conn.execute('''CREATE TABLE "KUNDEN"
    #         ("ID"	INTEGER NOT NULL UNIQUE,
    #         "BENUTZER_ID"	INTEGER NOT NULL,
    #         "VORNAME" TEXT NOT NULL,
    #         "NACHNAME" TEXT NOT NULL,
    #         "ADRESSE"	INTEGER,
    #         "BANKVERBINDUNG"	INTEGER,
    #         PRIMARY KEY("ID" AUTOINCREMENT),
    #         FOREIGN KEY("ADRESSE") REFERENCES ADRESSEN(ID),
    #         FOREIGN KEY("BANKVERBINDUNG") REFERENCES BANKVERBINDUNGEN(ID),
    #         FOREIGN KEY("BENUTZER_ID") REFERENCES BENUTZER(ID) ON DELETE CASCADE);
    #         ''')
    # print('Table KUNDEN created successfully!')

    conn.execute('''CREATE TABLE "ADRESSEN" 
                ("ID"	INTEGER NOT NULL UNIQUE,
                "BENUTZER_ID"	INTEGER NOT NULL,
                "STRASSE"	TEXT NOT NULL,
                "HAUSNUMMER"	INTEGER NOT NULL,
                "PLZ" TEXT NOT NULL,
                "STADT" TEXT NOT NULL,
                PRIMARY KEY("ID" AUTOINCREMENT),
                FOREIGN KEY("BENUTZER_ID") REFERENCES BENUTZER(ID) ON DELETE CASCADE);
                ''')
    print('Table ADRESSEN created successfully!')

    conn.execute('''CREATE TABLE "BANKVERBINDUNGEN" 
                ("ID"	INTEGER NOT NULL UNIQUE,
                "BENUTZER_ID"	INTEGER NOT NULL,
                "KONTOINHABER"	TEXT NOT NULL,
                "IBAN"	TEXT NOT NULL,
                "BIC" TEXT NOT NULL,
                PRIMARY KEY("ID" AUTOINCREMENT),
                FOREIGN KEY("BENUTZER_ID") REFERENCES BENUTZER(ID) ON DELETE CASCADE);
                ''')
    print('Table BANKVERBINDUNGEN created successfully!')

    conn.execute('''CREATE TABLE "BESTELLUNGEN" (
	        "ID"	INTEGER NOT NULL UNIQUE,
            "BENUTZER_ID"	INTEGER NOT NULL,
            "BESTELLDATUM"	TEXT NOT NULL,
            "STATUS"	TEXT NOT NULL,
            "BESTELLPOSTEN"	INTEGER NOT NULL UNIQUE,
            FOREIGN KEY("BENUTZER_ID") REFERENCES BENUTZER(ID),
            FOREIGN KEY("BESTELLPOSTEN") REFERENCES BESTELLPOSTEN(ID),
            PRIMARY KEY("ID" AUTOINCREMENT));
            ''')
    print('Table BESTELLUNGEN created successfully!')

    conn.execute('''CREATE TABLE "BESTELLPOSTEN" (
        "ID"	INTEGER NOT NULL UNIQUE,
        "BESTELL_ID"	INTEGER NOT NULL,
        "PRODUKT_ID"	INTEGER NOT NULL,
        "MENGE"	INTEGER NOT NULL,
        PRIMARY KEY("ID" AUTOINCREMENT),
        FOREIGN KEY("BESTELL_ID") REFERENCES BESTELLUNGEN(ID) ON DELETE CASCADE,
        FOREIGN KEY("PRODUKT_ID") REFERENCES PRODUKTE(ID));
        ''')
    print('Table BESTELLPOSTEN created successfully!')

    conn.execute('''CREATE TABLE "PRODUKTE" (
        "ID"	INTEGER NOT NULL UNIQUE,
        "PRODUKTBEZEICHNUNG"	TEXT NOT NULL,
        "PREIS"	INTEGER NOT NULL,
        "HERSTELLER"	TEXT,
        PRIMARY KEY("ID" AUTOINCREMENT));
        ''')
    print('Table PRODUKTE created successfully!')

    conn.execute('''CREATE TABLE "AKKUTRAEGER" (
        "ID"	INTEGER NOT NULL UNIQUE,
        "PRODUKT_ID"	INTEGER NOT NULL UNIQUE,
        "FUNKTIONSWEISE"	TEXT NOT NULL,
        "HÖHE"	INTEGER NOT NULL,
        "BREITE"	INTEGER NOT NULL,
        "AKKUTYP"	TEXT NOT NULL,
        PRIMARY KEY("ID" AUTOINCREMENT),
        FOREIGN KEY("PRODUKT_ID") REFERENCES PRODUKTE(ID) ON DELETE CASCADE);    
        ''')
    print('Table AKKUTRAEGER created successfully!')

    conn.execute('''CREATE TABLE "VERDAMPFER" (
        "ID"	INTEGER NOT NULL UNIQUE,
        "PRODUKT_ID"	INTEGER NOT NULL UNIQUE,
        "DURCHMESSER"	INTEGER NOT NULL,
        "HÖHE"	INTEGER NOT NULL,
        "GEWICHT"	INTEGER NOT NULL,
        "FÜLLSYSTEM"	TEXT NOT NULL,
        "PASSENDE_VERDAMPFERKOEPFE"	INTEGER,
        PRIMARY KEY("ID" AUTOINCREMENT),
        FOREIGN KEY("PASSENDE_VERDAMPFERKOEPFE") REFERENCES VERDAMPFERKEPFE(ID),
        FOREIGN KEY("PRODUKT_ID") REFERENCES PRODUKTE(ID) ON DELETE CASCADE);    
        ''')
    print('Table VERDAMPFER created successfully!')

    conn.execute('''CREATE TABLE "VERDAMPFERKOEPFE" (
        "ID"	INTEGER NOT NULL UNIQUE,
        "PRODUKT_ID"	INTEGER NOT NULL UNIQUE,
        "DRAHTMATERIAL"	TEXT NOT NULL,
        "WIEDERSTAND"	INTEGER NOT NULL,
        "PASSENDE_VERDAMPFER"	INTEGER,
        PRIMARY KEY("ID" AUTOINCREMENT),
        FOREIGN KEY("PASSENDE_VERDAMPFER") REFERENCES VERDAMPFER(ID),
        FOREIGN KEY("PRODUKT_ID") REFERENCES PRODUKTE(ID) ON DELETE CASCADE);    
        ''')
    print('Table VERDAMPFERKOEPFE created successfully!')

    conn.execute('''CREATE TABLE "STARTER_SETS" (
        "ID"	INTEGER NOT NULL UNIQUE,
        "PRODUKT_ID"	INTEGER NOT NULL UNIQUE,
        "AKKUTRAEGER"	INTEGER NOT NULL,
        "VERDAMPFER"	INTEGER NOT NULL,
        "VERDAMPFERKOPF"	INTEGER NOT NULL,
        PRIMARY KEY("ID" AUTOINCREMENT),
        FOREIGN KEY("VERDAMPFER") REFERENCES VERDAMPFER(ID) ON DELETE CASCADE,
        FOREIGN KEY("AKKUTRAEGER") REFERENCES AKKUTRAEGER(ID) ON DELETE CASCADE,
        FOREIGN KEY("VERDAMPFERKOPF") REFERENCES VERDAMPFERKOEPFE(ID) ON DELETE CASCADE,
        FOREIGN KEY("PRODUKT_ID") REFERENCES PRODUKTE(ID) ON DELETE CASCADE);
        ''')

    conn.close()
    print('Connection to DB closed')

def add_admin():

    print('creating initial admin user')

    conn = sqlite3.connect('test_db.db')

    conn.execute(f"INSERT INTO BENUTZER(BENUTZERNAME,PASSWORT,IS_ADMIN,IS_KUNDE,PERSONALNUMMER,ABTEILUNG) VALUES('admin','admin',True, False,'SHOPADMIN','IT');")
    conn.commit()

    # cursor = conn.execute(f"SELECT ID,BENUTZERNAME from BENUTZER")
    # for row in cursor:
    #     if 'admin' == row[1]:
    #         benutzer_id = row[0]
    #
    # conn.execute(
    #     f"INSERT INTO ADMINISTRATOREN(BENUTZER_ID,PERSONALNUMMER,ABTEILUNG) VALUES({benutzer_id},'SHOPADMIN','IT');")
    # conn.commit()

    conn.close()
    print('admin created successfully')

def run_setup():
    setup_database()
    add_admin()