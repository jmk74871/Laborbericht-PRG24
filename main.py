import os.path
import webshop
from setup_script import run_setup


def test_admin_creating_products():
    user = webshop.class_administrator.Administrator('admin', 'admin')

    user.add_verdampfer('SuperVape24', 8.99, 'VaperG', 2.8, 2.74, 'top fill')
    user.add_verdampfer('Nebelmaschine V3', 9.99, 'B-Vape', 2.8, 2.74, 'top fill')

    user.add_akkutaeger('Powerbank24', 15.99, 'aspire', 'geregelt', 5.4, 3.2, '2 x 18650er Standard Akku')
    user.add_akkutaeger('Glint II', 9.99, 'aspire', 'geregelt', 4.8, 3.1, '18650er Standard Akku')

    user.add_verdampferkopf('B-Vape V3', 0.43, 'B-Vape', 'Stainles Steel', 0.5)
    user.add_verdampferkopf('B-Vape V3-Mesh', 0.6, 'B-Vape', 'Stainles Steel Mesh', 0.33)

    user.define_matching(verdampfer_id=2, verdampferkopf_id=5)
    user.define_matching(verdampfer_id=2, verdampferkopf_id=6)

    user.add_set('Easy Starter Set', 12.99, 'VaperG + aspire', 4, 1, 6)


def test_user_placing_order():
    warenhaus = webshop.class_warenhaus.Warenhaus()
    warenhaus.display_produktinfo()
    user = webshop.class_kunde.Kunde('PeterV', 'pass234', warenhaus)

    user.add_to_warenkorb(1, 1)
    user.add_to_warenkorb(2, 1)

    user.add_to_warenkorb(4, 1)

    user.add_to_warenkorb(5, 2)
    user.add_to_warenkorb(6, 2)
    user.show_warenkorb()

    user.delete_from_warenkorb(2)
    user.show_warenkorb()

    user.add_adresse('Stuttgarter Str.', 3, '74700', 'Stuttgart')
    user.show_adressen()
    user.add_bankverbindung('Peter Vogel', 'DE42XXX7394', 'STVU7DRE')
    user.show_bankverbindungen()

    user.bestellung_aufgeben(adress_id=1, bank_id=1)


def test_user_changing_details_and_deleting_account():
    warenhaus = webshop.class_warenhaus.Warenhaus()
    user = webshop.class_kunde.Kunde('PeterV', 'pass234', warenhaus)

    user.show_kundendaten()
    user.update_kundendaten(nachname='Vogel-Frei')
    user.show_kundendaten()

    user.delete_kundendaten()


def main():
    if not os.path.exists('test_db.db'):
        run_setup()
    # test_admin_creating_products()
    # test_user_placing_order()
    # test_user_changing_details_and_deleting_account()


if __name__ == "__main__":
    main()
