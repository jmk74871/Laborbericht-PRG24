import os.path
import webshop
from mainframe import Mainframe
from setup_script import run_setup

def test_script():
    mf = Mainframe()
    mf.einloggen('admin', 'admin')
    prod = webshop.class_verdampfer.Verdampfer('Verdampfer123', 1.02, 'VaperG', 2.4, 3, 'top fill')
    mf.user.add_produkt(prod, mf.db_path)



def main():
    if not os.path.exists('test_db.db'):
        run_setup()
    test_script()
    pass


if __name__ == "__main__":
    main()
