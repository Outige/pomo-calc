from datetime import datetime
import sys
from math import floor
from random import randrange as rr
import os

PLEN = 25
OFF = 3

def test_file():
    try:
        fp = open('file.txt', 'r')
        fp.close()
    except IOError:
        return 0
    return 1

def delete_state():
    if len(sys.argv) < 3:
        return
    if sys.argv[2].lower() != 'delete':
        return
    D = input('Delete state? (y/n)').lower()
    if D != 'yes' and D != 'y':
        print('state not deleted')
        return
    os.remove('file.txt')
    print('state deleted')
    
    # if test_file():
    #     return
    # fp = open('file.txt', 'w')
    # fp.write(str(rr(PLEN-OFF, PLEN+OFF+1)))
    # fp.close()

def save_state():
    if test_file():
        return
    fp = open('file.txt', 'w')
    fp.write(str(rr(PLEN-OFF, PLEN+OFF+1)))
    fp.close()

def load_state():
    for line in open('file.txt'):
        line = int(line)
    return line

def handle_input():
    if len(sys.argv) >= 2:
        a = sys.argv[1]
    else:
        a = input("Start time(hh-mm):")
    a = datetime.strptime(a, "%H:%M")
    return a

if __name__ == "__main__":
    delete_state()
    save_state()
    oset = load_state()
    # a = input("Start time(hh-mm):")
    # b = str(datetime.now().hour) + ":" + str(datetime.now().minute) #input("Start time(hh-mm):")
    # a = datetime.strptime(a, "%H:%M")
    # b = datetime.strptime(b, "%H:%M")
    a = handle_input()
    b = datetime.now()

    hours = int(b.hour-a.hour)
    mins = int(b.minute-a.minute) + hours*60
    
    x = floor(mins/oset)
    m = mins - x*oset
    if x > 1:
        print("X" + str(x) + " + " + str(m))
    elif x == 1:
        print("+" + str(m))
    elif x == 0:
        m = oset - m
        print("-" + str(m))