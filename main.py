import os.path
import webshop
from setup_script import run_setup

def test_admin_creating_products():
    user = webshop.class_administrator.Administrator('admin', 'admin')

    user.add_verdampfer('SuperVape24', 1.52, 'VaperG', 2.8, 2.74, 'top fill')
    user.add_verdampfer('Nebelmaschine V3', 1.52, 'B-Vape', 2.8, 2.74, 'top fill')

    user.add_akkutaeger('Powerbank24', 15.99, 'aspire', 'geregelt', 5.4, 3.2, '2 x 18650er Standard Akku')
    user.add_akkutaeger('Glint II', 9.99, 'aspire', 'geregelt', 4.8, 3.1, '18650er Standard Akku')

    user.add_verdampferkopf('B-Vape V3', 0.33, 'B-Vape', 'Stainles Steel', 0.5)
    user.add_verdampferkopf('B-Vape V3-Mesh', 0.5, 'B-Vape', 'Stainles Steel Mesh', 0.33)

def test_user_loging_in():
    warenhaus = webshop.class_warenhaus.Warenhaus()
    user = webshop.class_kunde.Kunde('PeterV', 'pass234', warenhaus)
    # user.add_adresse('Stuttgarter Str.', 3, '74700', 'Stuttgart')
    user.zum_warenkorb_hinzufuegen(1, 1)
    user.zum_warenkorb_hinzufuegen(7, 3)
    user.zum_warenkorb_hinzufuegen(4, 2)
    user.warenkorb_anzeigen()



def main():
    if not os.path.exists('test_db.db'):
        run_setup()
    test_user_loging_in()
    # test_admin_creating_products()
    pass


if __name__ == "__main__":
    main()
