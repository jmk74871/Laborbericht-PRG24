import sqlite3

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

    conn.execute('''CREATE TABLE "BESTELLUNG" (
	        "ID"	INTEGER NOT NULL UNIQUE,
            "KUNDEN_ID"	INTEGER NOT NULL,
            "BESTELLDATUM"	TEXT NOT NULL,
            "STATUS"	TEXT NOT NULL,
            "BESTELLPOSTEN"	INTEGER NOT NULL UNIQUE,
            FOREIGN KEY("KUNDEN_ID") REFERENCES KUNDE(ID),
            PRIMARY KEY("ID" AUTOINCREMENT));''')
    print('Table BESTELLUNG created successfully!')

    conn.execute('''CREATE TABLE "BESTELLPOSTEN" (
        "ID"	INTEGER NOT NULL UNIQUE,
        "BESTELL_ID"	INTEGER NOT NULL,
        "PRODUKT_ID"	INTEGER NOT NULL,
        "MENGE"	INTEGER NOT NULL,
        PRIMARY KEY("ID" AUTOINCREMENT),
        FOREIGN KEY("BESTELL_ID") REFERENCES BESTELLUNG(ID),
        FOREIGN KEY("PRODUKT_ID") REFERENCES PRODUKT(ID));''')
    print('Table BESTELLPOSTEN created successfully!')

    conn.close()
    print('Connection to DB closed')

    add_admin()

def add_admin():

    print('creating initial admin user')

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

    conn.close()
    print('admin created successfully')

def run_setup():
    setup_database()
    add_admin()