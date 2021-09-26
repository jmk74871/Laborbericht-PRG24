import sqlite3


def setup_database():
    conn = sqlite3.connect('test_db.db')
    print('DB created successfully!')

    conn.execute("PRAGMA foreign_keys=on;")

    conn.execute('''CREATE TABLE "BENUTZER" (
        "BENUTZER_ID"	INTEGER NOT NULL UNIQUE,
        "BENUTZERNAME"	TEXT NOT NULL UNIQUE,
        "PASSWORT"	TEXT NOT NULL,
        "IS_ADMIN"	INTEGER NOT NULL,
        "IS_KUNDE"	INTEGER NOT NULL,
        "PERSONALNUMMER" TEXT,
        "ABTEILUNG" TEXT,
        "VORNAME" TEXT ,
        "NACHNAME" TEXT,
        PRIMARY KEY("BENUTZER_ID" AUTOINCREMENT));
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
        ("ADRESS_ID"	INTEGER NOT NULL UNIQUE,
        "BENUTZER_ID"	INTEGER NOT NULL,
        "STRASSE"	TEXT NOT NULL,
        "HAUSNUMMER"	INTEGER NOT NULL,
        "PLZ" TEXT NOT NULL,
        "STADT" TEXT NOT NULL,
        PRIMARY KEY("ADRESS_ID" AUTOINCREMENT),
        FOREIGN KEY("BENUTZER_ID") REFERENCES BENUTZER(BENUTZER_ID) ON DELETE CASCADE);
        ''')
    print('Table ADRESSEN created successfully!')

    conn.execute('''CREATE TABLE "BANKVERBINDUNGEN" 
        ("BANK_ID"	INTEGER NOT NULL UNIQUE,
        "BENUTZER_ID"	INTEGER NOT NULL,
        "KONTOINHABER"	TEXT NOT NULL,
        "IBAN"	TEXT NOT NULL,
        "BIC" TEXT NOT NULL,
        PRIMARY KEY("BANK_ID" AUTOINCREMENT),
        FOREIGN KEY("BENUTZER_ID") REFERENCES BENUTZER(BENUTZER_ID) ON DELETE CASCADE);
        ''')
    print('Table BANKVERBINDUNGEN created successfully!')

    conn.execute('''CREATE TABLE "BESTELLUNGEN" (
        "BESTELL_ID"	INTEGER NOT NULL UNIQUE,
        "BENUTZER_ID"	INTEGER NOT NULL,
        "BESTELLDATUM"	TEXT NOT NULL,
        "STATUS"	TEXT NOT NULL,
        FOREIGN KEY("BENUTZER_ID") REFERENCES BENUTZER(BENUTZER_ID),
        PRIMARY KEY(BESTELL_ID AUTOINCREMENT));
            ''')
    print('Table BESTELLUNGEN created successfully!')

    conn.execute('''CREATE TABLE "BESTELLPOSTEN" (
        "POSTEN_ID"	INTEGER NOT NULL UNIQUE,
        "BESTELL_ID"	INTEGER NOT NULL,
        "PRODUKT_ID"	INTEGER NOT NULL,
        "MENGE"	INTEGER NOT NULL,
        PRIMARY KEY("POSTEN_ID" AUTOINCREMENT),
        FOREIGN KEY("BESTELL_ID") REFERENCES BESTELLUNGEN(BESTELL_ID) ON DELETE CASCADE,
        FOREIGN KEY("PRODUKT_ID") REFERENCES PRODUKTE(ID));
        ''')
    print('Table BESTELLPOSTEN created successfully!')

    conn.execute('''CREATE TABLE "PRODUKTE" (
        "PRODUKT_ID"	INTEGER NOT NULL UNIQUE,
        "PRODUKTBEZEICHNUNG"	TEXT NOT NULL,
        "PREIS"	INTEGER NOT NULL,
        "HERSTELLER"	TEXT,
        PRIMARY KEY("PRODUKT_ID" AUTOINCREMENT));
        ''')
    print('Table PRODUKTE created successfully!')

    conn.execute('''CREATE TABLE "AKKUTRAEGER" (
        "PRODUKT_ID"	INTEGER NOT NULL UNIQUE,
        "FUNKTIONSWEISE"	TEXT NOT NULL,
        "HOEHE"	INTEGER NOT NULL,
        "BREITE"	INTEGER NOT NULL,
        "AKKUTYP"	TEXT NOT NULL,
        PRIMARY KEY("PRODUKT_ID"),
        FOREIGN KEY("PRODUKT_ID") REFERENCES "PRODUKTE"("PRODUKT_ID") ON DELETE CASCADE);    
        ''')
    print('Table AKKUTRAEGER created successfully!')

    conn.execute('''CREATE TABLE "VERDAMPFER" (
        "PRODUKT_ID"	INTEGER NOT NULL UNIQUE,
        "DURCHMESSER"	INTEGER NOT NULL,
        "HOEHE"	INTEGER NOT NULL,
        "FUELLSYSTEM"	TEXT NOT NULL,
        PRIMARY KEY("PRODUKT_ID"),
        FOREIGN KEY("PRODUKT_ID") REFERENCES "PRODUKTE"("PRODUKT_ID") ON DELETE CASCADE);    
        ''')
    print('Table VERDAMPFER created successfully!')

    conn.execute('''CREATE TABLE "VERDAMPFERKOEPFE" (
        "PRODUKT_ID"	INTEGER NOT NULL UNIQUE,
        "DRAHTMATERIAL"	TEXT NOT NULL,
        "WIEDERSTAND"	INTEGER NOT NULL,
        PRIMARY KEY("PRODUKT_ID"),
        FOREIGN KEY("PRODUKT_ID") REFERENCES "PRODUKTE"("ID") ON DELETE CASCADE);    
        ''')
    print('Table VERDAMPFERKOEPFE created successfully!')

    conn.execute('''CREATE TABLE "PASST_ZU" (
        "PASSUNG_ID"	INTEGER NOT NULL UNIQUE,
        "VERDAMPFER_ID"	INTEGER NOT NULL,
        "VERDAMPFERKOPF_ID"	INTEGER NOT NULL,
        FOREIGN KEY("VERDAMPFER_ID") REFERENCES VERDAMPFER(PRODUKT_ID) ON DELETE CASCADE ,
        FOREIGN KEY("VERDAMPFERKOPF_ID") REFERENCES VERDAMPFERKOEPFE(PRODUKT_ID) ON DELETE CASCADE,
        PRIMARY KEY("PASSUNG_ID" AUTOINCREMENT));
        ''')
    print('Table PASST_ZU created successfully!')

    conn.execute('''CREATE TABLE "STARTER_SETS" (
        "PRODUKT_ID"	INTEGER NOT NULL UNIQUE,
        "AKKUTRAEGER"	INTEGER NOT NULL,
        "VERDAMPFER"	INTEGER NOT NULL,
        "VERDAMPFERKOPF"	INTEGER NOT NULL,
        PRIMARY KEY("PRODUKT_ID"),
        FOREIGN KEY("VERDAMPFER") REFERENCES VERDAMPFER(PRODUKT_ID) ON DELETE CASCADE,
        FOREIGN KEY("AKKUTRAEGER") REFERENCES AKKUTRAEGER(PRODUKT_ID) ON DELETE CASCADE,
        FOREIGN KEY("VERDAMPFERKOPF") REFERENCES VERDAMPFERKOEPFE(PRODUKT_ID) ON DELETE CASCADE,
        FOREIGN KEY("PRODUKT_ID") REFERENCES PRODUKTE(ID) ON DELETE CASCADE);
        ''')
    print('Table STARTER_SETS created successfully!')

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