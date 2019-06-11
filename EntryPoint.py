"""
Demos the tricks on the bebop. Make sure you have enough room to perform them!

Author: Amy McGovern
"""

from pyparrot.Bebop import Bebop
from CopterMove import CopterMove

# iterResult = iter(result)
# next(iterResult)
# bebop.move_relative(0, 0, 0, math.radians(-90))
#
# for target in result:
#     # dx = target[0] - currentPosition[0]
#     # dy = target[1] - currentPosition[1]
#     # bebop.fly_direct(0,10*dx,0,0,1)
#     # bebop.fly_direct(10*dy,0,0,0,1)
#     bebop.move_relative(-target[0], target[1], 0, 0)
#     currentPosition = target
#

print("DONE - disconnecting")

if __name__ == "__main__":
    bebop = Bebop(ip_address="10.202.0.1")

    print("connecting")
    success = bebop.connect(10)
    if (success):
        print("Successfully connected to the Bebop. Starting ")
        start = (4, 5)
        end = (7, 7)
        barriers = [[(2, 5), (1, 5), (0, 5)],
                    [(4, 3), (4, 4), (4, 5)],
                    [(2, 4), (2, 5), (2, 6), (3, 6), (4, 6), (5, 6), (5, 5), (5, 4), (5, 3), (5, 2), (4, 2), (3, 2)]]
        cm = CopterMove(bebop, start, end, barriers, True)
        cm.Move()
        bebop.disconnect()
    else:
        print("Error connecting to bebop.  Retry")
