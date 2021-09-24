import os.path

from setup_script import run_setup


def main():
    if not os.path.exists('test_db.db'):
        run_setup()

    pass


if __name__ == "__main__":
    main()
