from Localisation import Localisation
from PathPlan import PathPlan
import numpy


class CopterMove:
    def __init__(self, bebop, start, goal, barriers, display=False):
        self.bebop = bebop
        self.localisation = Localisation()
        self.pathPlan = PathPlan(start, goal, barriers, display)
        bebop.safe_takeoff(10)
        self.OrientCopter(start)

    def Move(self):
        for target in self.pathPlan.getResult():
            self.bebop.move_relative(target[1], target[0], 0, 0)
            self.OrientCopter(target)
        self.bebop.safe_land(10)

    def OrientCopter(self, expectedLocation):
        realLocation = Localisation.GetPosition()
        error = numpy.subtract(expectedLocation, expectedLocation)
        self.bebop.move_relative(error[1], error[0], 0, 0)
