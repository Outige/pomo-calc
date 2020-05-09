from datetime import datetime
import sys
from math import floor
from random import randrange as rr
import os

# ----------------------------------
# globals
# ----------------------------------

PLEN = 25
OFF = 3


# ----------------------------------
# files
# ----------------------------------

def test_file(f):
    try:
        fp = open(f, 'r')
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


def save_state():
    if test_file('file.txt'):
        return
    fp = open('file.txt', 'w')
    fp.write(str(rr(PLEN-OFF, PLEN+OFF+1)))
    fp.close()

def load_state():
    for line in open('file.txt'):
        line = int(line)
    return line

def append_record(time, grade, date):
    if not test_file('record.txt'):
        fp = open('record.txt', 'w')
        fp.write(str(time)+ ','+str(grade)+ ','+str(date.date()))
        fp.close()
    else:
        fp = open('record.txt', 'a')
        fp.write('\n'+str(time)+ ','+str(grade)+ ','+str(date.date()))
        fp.close()

# ----------------------------------
# helper
# ----------------------------------

def handle_input():
    if len(sys.argv) >= 2:
        a = sys.argv[1]
    else:
        a = input("Start time(hh-mm):")
    a = datetime.strptime(a, "%H:%M")
    return a


# ----------------------------------
# systems
# ----------------------------------

def relative_system():
    delete_state()
    save_state()
    oset = load_state()
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

def grade_system():
    a = handle_input()
    b = datetime.now()

    hours = int(b.hour-a.hour)
    mins = int(b.minute-a.minute) + hours*60
    oset = 25
    grade = ''
    if mins < oset:
        grade = 'F'
    elif mins >= oset and mins < oset*1.5:
        grade = 'C'
    elif mins >= oset*1.5 and mins < oset*2:
        grade = 'B'
    elif mins >= oset*2:
        grade = 'A'
    append_record(mins, grade, datetime.now())
    print("%s" %(grade))

if __name__ == "__main__":
    # relative_system()
    grade_system()