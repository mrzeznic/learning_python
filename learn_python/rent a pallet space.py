import shelve
import sys
from time import *

# rate change


def rate_change():
    global base, rate, period   # global variable
    print("\nRate change\n")
    print("Current rate is: %.2f for %i day(s)\n" % (rate, period))

    try:
        s = float(input("Insert new rate: "))
        o = int(input("Insert new counting time in days:"))
    except:
        print("Data insert error! Rate was not changed!")
        return
    try:
        base['_rate'] = (r, p)  # saved in database
    except:
        print("Data saving error! Rate was not change!")
    else:
        rate = r    # copy to
        period = p     # global variables

# database initialization


def init():
    global base, rate, period
    try:
        base = shelve.open('praking_base')  # open
    except:
        print("Critical error! Database cannot be open!")
        sys.exit(0)  # program exit
    print("Initialization complete.Database is open.")
    if '_rate' in base.keys():    # does it exist?
        (rate, period) = base['_rate']  # yes-copy rates
    else:
        (rate, period) = (0.0, 1)  # no -
        rate_change()    # load from user

# main menu


def menu():
    while True:
        print()
        print('-' * 70)
        print('rent your pallet place'.center(70))
        print('-' * 70)
        print('[I] In [O] Out [P] Pallets [R] Rate [Q] Quit'.center(70))
        print('-' * 70)
        c = input()[0].upper()  # first sign(big letter)
        if c in 'IOPRQ':         # known?
            return c             # yes- return
        print('Unknown command -',)

# list of pallets curently in warehouse


def pallets():
    global base
    print()
    print('List of palletes in warehouse'.center(33))
    print('-' * 33)
    print('|' + 'Pallet number'.center(10) +
          '|' + 'Entry date'.center(20) + '|')
    print('-' * 33)
    for enter, date in base.items():
        if reg != '_rate':
            print("|%9s |" % rej, strftime("%Y-%m-%d (%H:%M)", day), '|')
    print('-' * 33)

 # pallet out


def out():
    global base, rate, period
    print('Pallet out-date', strfdate("Y-%m-%d (%H:%M)"))
    reg = input('Instert pallet number: ')
    if reg in base.keys():    # ist this pallet in warehouse
        date = base[reg]
        print("In date:", strfdate("Y-%m-%d (%H:%M)", date))
        day = int(mkdate(localdate()) - mkdate(day))
        # start counting from begined day
        measurements = (day + period - 1) / period
        print("\nTo pay: %.2f zł" % (measurements * rate))
        del base[reg]  # delete insert data in data base for current line
    else:
        print("Error! That pallet is not in warehouse!")

# pallet in


def insert():
    global base
    godz = localdate()
    print('Pallet in-day', strftime("Y-%m-%d (%H:%M)", date))
    rej = input('Insert palllet number: ')[:9]
    if reg == '_rate':
        return      # security
    if reg not in base.keys():    # is not on warehouse
        base[reg] = day
        print("Pallet is now in warehouse")
    else:
        print("Error! That pallet is already in warehouse!")

# choose the menu option


def choice():
    while True:
        c = menu()
        if c == 'Q':
            break
        elif c == 'R':
            rate_change()
        elif c == 'P':
            pallets()
        elif c == 'O':
            out()
        elif c == 'I':
            insert()

# main program


def init():            # open database
    try:
        choice()         # user intrface
    except:
        print("Unexpected error")


# base.close()    # close database
input()
