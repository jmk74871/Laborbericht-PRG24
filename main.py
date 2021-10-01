import os.path
import webshop
from mainframe import Mainframe
from setup_script import run_setup

def test_script():
    mf = Mainframe()
    mf.einloggen('admin', 'admin')
    mf.user.add_verdampfer('Verdampfer247', 1.52, 'VaperG', 2.8, 2.74, 'top fill', mf.db_path)



def main():
    if not os.path.exists('test_db.db'):
        run_setup()
    test_script()
    pass


if __name__ == "__main__":
    main()
