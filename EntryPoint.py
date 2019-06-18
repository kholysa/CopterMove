"""
Demos the tricks on the bebop. Make sure you have enough room to perform them!

Author: Amy McGovern
"""

from pyparrot.Bebop import Bebop
from CopterMove import CopterMove
from Localisation import Localisation

def initBarriers(stepSizeBarriers):
    barriers = list()
    barrierA = list()
    barrierB = list()
    barrierC = list()
    for i in range(21):
        stepSize = round(i * stepSizeBarriers, 2)
        barrierA.append((stepSize, 5.0))

    for i in range(21):
        stepSize = round(i * stepSizeBarriers, 2)
        barrierB.append((4.0, 3 + stepSize))

    for i in range(21):
        stepSize = round(i * stepSizeBarriers, 2)
        barrierC.append((2.0, 4 + stepSize))

    for i in range(31):
        stepSize = round(i * stepSizeBarriers, 2)
        barrierC.append((2 + stepSize, 6.0))

    for i in range(41):
        stepSize = round(i * stepSizeBarriers, 2)
        barrierC.append((5.0, 6 - stepSize))

    for i in range(21):
        stepSize = round(i * stepSizeBarriers, 2)
        barrierC.append((3 + stepSize, 2.0))

    barriers.append(barrierA)
    barriers.append(barrierB)
    barriers.append(barrierC)
    return barriers

if __name__ == "__main__":
    bebop = Bebop(ip_address="10.202.0.1")

    print("connecting")
    success = bebop.connect(2)

    if success:
        print("Successfully connected to the Bebop. Starting ")
        start = (2.8, 2.9)
        end = (2.8, 7.9)
        stepSizeDrone = 0.1
        barriers = initBarriers(stepSizeDrone)
        try:
            cm = CopterMove(bebop, start, end, barriers, stepSizeDrone, display=True)
            cm.Move()
            bebop.disconnect()
        except:
            bebop.emergency_land()
            bebop.disconnect()
    else:
        print("Error connecting to bebop.  Retry")
