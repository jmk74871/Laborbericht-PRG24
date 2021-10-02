import sqlite3
from datetime import datetime
from webshop.class_verdampfer import Verdampfer
from webshop.class_akkutaeger import Akkutraeger
from webshop.class_verdampferkopf import Verdampferkopf
from webshop.class_starterset import Starterset


class Warenhaus():

    def __init__(self):
        self.__db_path = 'test_db.db'
        self.__katalog = dict()

        self.__last_update = None

        if self.__last_update is None:
            self.__build_katalog()

    # öffentliche Schnittstellen

    def get_by_id(self, id: int) -> object:
        if self.__chek_if_update_needed():
            try:
                return self.__katalog[id]
            except KeyError:
                print('Item not found in catalog.')

    def display_produktinfo(self, verdampfer: bool =False, verdampferkoepfe: bool =False, akkutraeger: bool =False,
                            startersets: bool =False, all: bool =True):

        if self.__chek_if_update_needed():
            if all:
                for product in self.__katalog.values():
                    product.display_info()
            else:
                for product in self.__katalog.values():
                    if verdampfer and isinstance(product, Verdampfer):
                        product.display_info()
                    elif verdampferkoepfe and isinstance(product, Verdampferkopf):
                        product.display_info()
                    elif akkutraeger and isinstance(product, Akkutraeger):
                        product.display_info()
                    elif startersets and isinstance(product, Starterset):
                        product.display_info()

    # interne Methoden

    def __build_katalog(self):

        conn = sqlite3.connect(self.__db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        cursor.execute("SELECT * from PRODUKTE;")
        produkte = cursor.fetchall()

        cursor.execute("SELECT * from VERDAMPFER;")
        verdampfer = cursor.fetchall()

        cursor.execute("SELECT * from VERDAMPFERKOEPFE;")
        verdampferkoepfe = cursor.fetchall()

        cursor.execute("SELECT * from AKKUTRAEGER;")
        akkutaeger = cursor.fetchall()

        cursor.execute("SELECT * from STARTER_SETS;")
        startersets = cursor.fetchall()

        conn.close()

        p_ds = dict()
        for ds in produkte:
            p_id = ds['PRODUKT_ID']
            p_ds[p_id] = {'produktbezeichnung': ds['PRODUKTBEZEICHNUNG'], 'preis': ds['PREIS'],
                          'hersteller': ds['Hersteller']}

        for ds in verdampfer:
            id = ds['PRODUKT_ID']
            prod = Verdampfer(produkt_id=id, produktbezeichnung=p_ds[id]['produktbezeichnung'], preis=p_ds[id]['preis'],
                              hersteller=p_ds[id]['hersteller'], durchmesser=ds['DURCHMESSER'],
                              hoehe=ds['HOEHE'], fuellsystem=ds['FUELLSYSTEM'])
            self.__katalog[id] = prod

        for ds in verdampferkoepfe:
            id = ds['PRODUKT_ID']
            prod = Verdampferkopf(produkt_id=id, produktbezeichnung=p_ds[id]['produktbezeichnung'],
                                  preis=p_ds[id]['preis'],
                                  hersteller=p_ds[id]['hersteller'], drahtmaterial=ds['DRAHTMATERIAL'],
                                  wiederstand=ds['WIEDERSTAND'])
            self.__katalog[id] = prod

        for ds in akkutaeger:
            id = ds['PRODUKT_ID']
            prod = Akkutraeger(produkt_id=id, produktbezeichnung=p_ds[id]['produktbezeichnung'],
                               preis=p_ds[id]['preis'],
                               hersteller=p_ds[id]['hersteller'], funktionsweise=ds['FUNKTIONSWEISE'],
                               hoehe=ds['HOEHE'], breite=ds['BREITE'], akkutyp=ds['AKKUTYP'])
            self.__katalog[id] = prod

        self.__last_update = datetime.now()
        print('Katalog updated!')

    def __chek_if_update_needed(self) -> bool:
        delta = datetime.now() - self.__last_update
        if delta.total_seconds() > 60:
            self.__build_katalog()

        return True

