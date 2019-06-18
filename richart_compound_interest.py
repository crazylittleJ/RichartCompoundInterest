#!/usr/bin/env python
#Compound interest principal
import os
import sys
def quit_program():
    os.system("pause")
    sys.exit()
    return
try:
    x=float(input("Enter your amount: "))
except Exception as e:
    print('Invalid input!')
    quit_program()
try:
    y=float(input("Enter your rate: "))
except Exception as e:
    print('Invalid input!')
    quit_program()
try:
    z=float(input("Enter your time: "))
except Exception as e:
    print('Invalid input!')
    quit_program()
def invest(amount,rate,time):
    try:
        principal=amount*(1+rate)**time
    except Exception as e:
        print('Result is too large!')
        quit_program()
    return principal
print('Result : {0}'.format(invest(x,y,z)))
quit_program()
