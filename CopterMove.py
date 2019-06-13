from Localisation import Localisation
from PathPlan import PathPlan
import numpy


class CopterMove:
    maxHoverHeight = 1.4

    def __init__(self, bebop, start, goal, barriers, display=False):
        self.bebop = bebop
        self.localisation = Localisation()
        self.pathPlan = PathPlan(start, goal, barriers, display)
        self.bebop.set_max_altitude(CopterMove.maxHoverHeight)
        self.bebop.safe_takeoff(10)
        self.bebop.move_relative(0, 0, -0.6, 0)

    def Move(self):
        for target in self.pathPlan.getResult():
            self.bebop.move_relative(target[1], target[0], 0, 0)
            self.OrientCopter(self.pathPlan.getNextCoordinate())
        self.bebop.safe_land(10)

    def OrientCopter(self, expectedLocation):
        print("Orienting Copter to " + str(expectedLocation))
        realLocation = Localisation.GetPosition()
        error = numpy.subtract(expectedLocation, expectedLocation)
        self.bebop.move_relative(error[1], error[0], 0, 0)
