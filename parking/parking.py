import shelve
import sys
from time import *
from parking import int
# rate change


def rate_change():
    global base, rate, period  # global variables
    print("\nChanging fees\n")
    print("Current fees is %.2f $ for %i minute(s)\n") % (rate, period)
    try:
          r = float(input("Enter new fees level:\n"))
          p = int(input("Enter new time counter in minutes:\n"))
    except:
          print("Error data input! The rate has not been changed!")
          return
    try:
          base['_rate'] = (r, p)  # save in database
    except:
          print("Error data input!The rate has not beed changed:")
    else:
          rate = r  # copy to
          period = p  # global variables

# Database initialization


def init():
    global base, rate, period
    try:
          base = shelve.open('parking_base')  # open
    except:
          print("Critical error! The database is not open!")
          sys.exit(0)  # program exit
    print("Initialization seccessful! Database has been opened.")
    if '_rate' in base.keys():  # exist?
          (rate, period) = base['_rate']  # yes- copy rates
    else:
          (rate, period) = (0.0, 1)  # no
          rate_change()  # load users
# main menu

    def menu():
          while True:
              print(),
              print('-' * 70)
              print('Parking'.center(70))
              print('-' * 70)
              print('[E] Entry [X] Exit [V] Vehicles [R] Rate [C] Close'.center(70))
              print('-' * 70)
          e = input()[0].upper()  # first sign (big letter)
          if e in 'CRVXE':  # known?
              return e  # yes- show result
          print('Unknown command-',)

# Vehicles list on parking


def vehicles():
    global base
    print()
    print('Vehicles list on parking'.center(33))
    print('-' * 33)
    print('|' + 'Registration number.'.center(10) +
          '|' + 'Park hours'.center(20) + '|')
    print('-' * 33)


for reg, hour in base.items():
    if reg != '_rate':
        print("|%9r |" % reg, strftime("%H:%M (%Y-%m-%d)", hour, '|')
               and
               print('-' * 33)
# car exit
def exit_():
    global base, rate, period
    print('Vehicle exit- hour', strftime("%H:%M (%Y-%m-%d)"))
reg=input('Insert vehicle registration number: ')
if reg in base.keys():    # is this vehicle was parked?
    hour=base[reg]
    print("Exit time:", strftime("%H:%M (%Y-%m-%d)", hour))
    minutes=int((mktime(localtime()) - mktime(hour)) / 60)
    units=((minutes + period - 1) / period)  # count from the beggining
    print("\nTo pay: %.2f $" % (unit * rate))
    del base[reg]  # delete registration
else:
    print("Error! Such a vehicle is not in parking lot!")

# Vehicle enter registration
def enter():
    global base
    hour=localtime()
    print('Vehicle enter- hour', strftime("%H:%M (%Y-%m-%d)", hour))
    reg=input('Please enter the registration number of the vehicle:\n ')[:9]
    if reg == '_rate': return      # security
    if reg not in base.keys():    # It is not parked?
        base[reg]=hour
        print("Insered.")
    else:
        print("Error! Such a vehicle is already not in the parking lot!")

# User choice implementation

def choice():
    while True:
        w=menu()
        if w == 'C':
            break
        elif w == 'R':
            rate_change()
        elif w == 'V':
            vehicle()
        elif w == 'X':
            exit_()
        elif w == 'E':
            enter()

# main program
init()     # open database
try:
    choice()         # user interface
except:
    print("Critical error.")
base.close()    # close database
