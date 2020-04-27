from datetime import datetime
import sys
from math import floor

if __name__ == "__main__":
    a = input("Start time(hh-mm):")
    b = input("Start time(hh-mm):")
    a = datetime.strptime(a, "%H:%M")
    b = datetime.strptime(b, "%H:%M")

    hours = int(b.hour-a.hour)
    mins = int(b.minute-a.minute) + hours*60
    
    x = floor(mins/25)
    m = mins - x*25
    if x > 1:
        print("X" + str(x) + " + " + str(m))
    elif x == 1:
        print("+" + str(m))
    elif x == 0:
        m = 25 - m
        print("-" + str(m))