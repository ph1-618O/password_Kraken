#! usr/bin/env python 3.8.5
# coding: utf-8

#Skipping the symbols only conditional
import secrets

a = 26
n = 10
s = 33


def combos(pos_chars, num=5, alp="Yes", nos='Yes', symb='Yes', uL='No'):
    #default 5, bc avg word length in English is 4.7
    var = pos_chars**int(num)
    return f'\tYour randomly generated password {str(secrets.token_urlsafe(int(num)))}\n\
    \tThere are {"{:e}".format(var)} possible combinations for a {num} digit long password\n\
        Alpha = {alp.title()}, Numbers = {nos.title()}, Symbols = {symb.title()}, and Upper and Lower = {uL.title()}\n'


# For Alphabetic passwords only
print('This program calculates number of possible combinations for a password')
print('Please answer Yes or No for the following questions')
alp = input('Alphabetic\n')
if 'y' in alp.lower():
    uL = input('Upper and Lower Included?\n')
    #symb = input('Symbols included?\n')
nos = input('Numbers?\n')
symb = input('Symbols included?\n')
# if 'y' in nos.lower():
#     symb = input('Symbols included?\n')

num = input('How many characters? Numbers only please\n')

# Alph Tree
if 'y' in alp.lower():
    if 'y' in uL.lower(): #alp upper and lower
        if 'y' in nos.lower(): #alph upper, lower and nums
            if 'y' in symb.lower(): #alph upper, lower, nums and symb
                print(f'\n\tOut of {a*2+n+s} characters')
                print(combos(a*2+n+s, num, alp, nos, symb, uL))
            else: #alph upper, lower, and nums
                print(f'\n\tOut of {a*2+n} characters')
                print(combos(a*2+n, num, alp, nos, symb, uL))

        else: #alph upper and lower
            print(f'\n\tOut of {a*2} characters')
            print(combos(a*2, num, alp, nos, symb, uL))
    else: # alph only
        print(f'\n\tOut of {a} characters')
        print(combos(a, num, alp, nos, symb, uL))

# Num Tree
elif 'y' in nos.lower():
    if 'y' in symb.lower():
        print(f'\n\tOut of {n+s} characters')
        print(combos(n+s, num, alp, nos, symb, uL))
    else:
        print(f'Out of {n} characters')
        print(combos(n, num, alp, nos, symb, uL))

#equiprobable - (of two or more things) equally likely to occur; having equal probability
# Notes about Dicewords https://theworld.com/~reinhold/diceware.html#:~:text=Diceware%E2%84%A2%20is%20a%20method,by%20a%20five%20digit%20number
#playing with entropy https://www.pleacher.com/mp/mlessons/algebra/entropy.html
#writing log functions in python https://www.geeksforgeeks.org/log-functions-python/
#https://en.wikipedia.org/wiki/Password_strength#Entropy_as_a_measure_of_password_strength
#notes on calculating CPU hours http://www.gridrepublic.org/joomla/components/com_mambowiki/index.php/GFlops,_G-hours,_and_CPU_hours
#amount of time each thread of the computer has run and then the sum for ea computer
# Choosing Password char amount, ie, 3 nos, 3 chars, etc
#https://docs.python.org/3/library/secrets.html#:~:text=The%20text%20is%20Base64%20encoded,a%20reasonable%20default%20is%20used.

def main():
    combos()

