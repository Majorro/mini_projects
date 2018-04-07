import time
import re
import argparse
import operator
from sys import argv

def filepath_enter():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', action='store', default='data.txt')
    args = parser.parse_args(argv[1:])
    return vars(args)['file']

def open_file(filepath):
    with open(filepath) as data:
        text = data.read()
        return text

def search_popular_words(file):
    pattern = '\w+'
    list_of_words = [word.lower() for word in re.findall(pattern, file)]
    num_of_words = {word: list_of_words.count(word) for word in set(list_of_words)}
    sorted_words = sorted(num_of_words.items(), key=operator.itemgetter(1), reverse=True)
    length = len(sorted_words)
    if length > 10:
        length = 10
    for i in range(length):
        print(sorted_words[i][0], sorted_words[i][1])


if __name__ == '__main__':
    start = time.time()
    search_popular_words(open_file(filepath_enter()))
    end = time.time()
    print('time =', end - start)
