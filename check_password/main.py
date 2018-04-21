from sys import argv
import argparse
import time


def argparse_():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default='common_passwords.txt')
    parser.add_argument('--password')
    args = parser.parse_args(argv[1:])
    return vars(args)

def open_file_and_check(filepath, password):
    try:
        with open(filepath) as data:
            for common_password in data:
                if password == common_password:
                    print('YOUR PASSWORD IS SHIT')
                    return 1
                else:
                    return 0
    except FileNotFoundError:
        print('Bad filepath, you bastard')

def scoring(password):
    


if __name__ == '__main__':
    args = argparse.values()
    print(open_file_and_check())
