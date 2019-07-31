"""
Demos the tricks on the bebop. Make sure you have enough room to perform them!

Author: Amy McGovern
"""

from pyparrot.Bebop import Bebop
from CopterMove import CopterMove
from Localisation import Localisation

def initBarriers():
    #barriers = [
     #   [(2, 5), (1, 5), (0, 5)],
#
 #       [(4, 3), (4, 4), (4, 5)],
#
 #       [(2, 4), (2, 5), (2, 6),
  #        (3, 6), (4, 6), (5, 6),
   #       (5, 5), (5, 4), (5, 3), (5, 2),
    #      (4, 2), (3, 2)]
     #]
    barriers = []

    barrier1 = []
    for i in range(20):
        for j in range(10):
            barrier1.append((27+i,45+j))
#    barrier2 = []
#    for i in range(20):
#        for j in range(10):
#            barrier2.append((27+i,45+j))

    barriers.append(barrier1)
#    barriers.append(barrier2)
    return barriers

if __name__ == "__main__":
    bebop = Bebop()

    print("connecting")
    success = bebop.connect(2)

    if success:
        print("Successfully connected to the Bebop. Starting ")
        start = (31, 30)
        end = (31, 80)
        barriers = initBarriers()
        scale = 10
        try:
            cm = CopterMove(bebop, start, end, barriers, scale, display=True)
            cm.Move()
            print('Remaining Battery: ',bebop.sensors.battery)
            bebop.disconnect()
        except:
            bebop.emergency_land()
            bebop.disconnect()
    else:
        print("Error connecting to bebop.  Retry")
