"""
Demos the tricks on the bebop. Make sure you have enough room to perform them!

Author: Amy McGovern
"""

from pyparrot.Bebop import Bebop
from CopterMove import CopterMove
from Localisation import Localisation

if __name__ == "__main__":
    bebop = Bebop()

    print("connecting")
    success = bebop.connect(10)

    if success:
        print("Successfully connected to the Bebop. Starting ")
        start = (2.82, 2.94)
        end = (2.82, 5.94)
        barriers = [[(3, 5), (4, 5), (5, 5)]]
        try:
            cm = CopterMove(bebop, start, end, barriers, True)
            cm.Move()
            bebop.disconnect()
        except:
            bebop.emergency_land()
            bebop.disconnect()
    else:
        print("Error connecting to bebop.  Retry")
