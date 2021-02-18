from sys import argv
import argparse
import time
import re


def argparse_():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', default='common_passwords.txt')
    parser.add_argument('--password', default='computer,science228')
    args = parser.parse_args(argv[1:])
    return vars(args)

def open_file_and_check(filepath, password):
    try:
        with open(filepath) as data:
            for common_password in data:
                if password == common_password.split('\n')[0]:
                    print('Your password is bad')
                    return 1
            return 0
    except FileNotFoundError:
        print('Wrong filepath')

def scoring(password):
    pattern_up = r'[A-Z]'
    pattern_low = r'[a-z]'
    pattern_digit = r'\d'
    pattern_character = r'\W'
    score = 0
    if re.search(pattern_up, password):
        score += 1
    if re.search(pattern_low, password):
        score += 1
    if re.search(pattern_digit, password):
        score += 1
    if re.search(pattern_character, password):
        score += 1
    if len(password) < 4:
        pass
    elif 4 <= len(password) <= 7:
        score += 1
    elif 8 <= len(password) <= 13:
        score += 2
    elif 14 <= len(password) <= 19:
        score += 3
    else:
        score += 4
    print('Safety of your password:', str(score)+'*')



if __name__ == '__main__':
    start = time.time()
    args = list(argparse_().values())
    if open_file_and_check(args[0], args[1]) == 0:
        scoring(args[1])
    else:
        exit(0)
    end = time.time()
    print('time =', end - start)
