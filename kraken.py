#! usr/bin/env python 3.8.5
# coding: utf-8

import hashlib
from urllib.request import urlopen
from PyDictionary import PyDictionary as wordDict
from english_words import english_words_set as words
import time
import pandas as pd
pd.options.mode.chained_assignment = None
import pprint
pp = pprint.PrettyPrinter(indent=4)

# Second word list for later frequency analysis
# wordsDF = pd.read_csv('wordsDF.csv', dtype=str)
# pp.pprint(wordsDF.head())
# print(wordsDF.info())
# print(len(wordsDF))

# Thinking about testing each value in the imported csv ask true if there is a definition
# if wordDict.meaning(wordsDF['a'][0]):
#     print('True')

def read_word_list(url):
    try:
        word_list_file = urlopen(url).read()
    except Exception as e:
        print('ERROR READING WORDLIST', e)
        exit()
    return word_list_file

def hash(word_list_password):
    result = hashlib.sha1(word_list_password.encode())
    return result.hexdigest()

def brute_force(guess_password_list, actual_password_hash, start_timer):
    for guess_password in guess_password_list:
        if hash(guess_password) == actual_password_hash:
            print(f'PASSWORD IS :: {guess_password} \nCHANGE PASSWORD NOW')
            print(f'{start_timer - time.perf_counter():0.4f} SECONDS TO EXECUTE CRACK\n')
            exit()

def main():
    url= 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
    actual_password = input('\n\nWhat is the password to test?\n').lower()
    actual_password_hash = hash(actual_password)
    start_timer = time.perf_counter()
    word_list = read_word_list(url).decode('UTF-8')
    guess_password_list = word_list.split('\n')
    brute_force(guess_password_list, actual_password_hash, start_timer)
    print(f'{start_timer - time.perf_counter():0.4f} TO EXECUTE\n')
    print('PASSWORD NOT GUESSABLE USING WORLIST')


if __name__ == "__main__":
    main()

