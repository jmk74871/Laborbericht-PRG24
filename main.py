import os.path

from setup_script import run_setup

def start_up():
    print('''
    Wilkommen im shop. Bitte wähle aus. Du kannst dich.\n
    /einloggen\n
    /registrieren\n
    oder \n
    /produkte_anzeigen\n
    ''')

    response = input()

    return response



def main():
    if not os.path.exists('test_db.db'):
        run_setup()

    pass


if __name__ == "__main__":
    main()
