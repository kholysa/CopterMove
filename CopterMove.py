from Localisation import Localisation
from PathPlan import PathPlan
import numpy


class CopterMove:
    def __init__(self, bebop, start, goal, barriers, stepSizeDrone, display=False):
        self.bebop = bebop
        self.localisation = Localisation()
        self.pathPlan = PathPlan(start, goal, barriers, stepSizeDrone, display)
        bebop.set_max_altitude(1.4)
        bebop.safe_takeoff(10)
        bebop.move_relative(0, 0, -0.6,0 )

    def Move(self):
        # print(self.localisation.GetPosition())
        for target in self.pathPlan.getResult():
            self.bebop.move_relative(target[1], target[0], 0, 0)
            self.OrientCopter(self.pathPlan.getNextMove())
        # print(self.localisation.GetPosition())
        self.bebop.safe_land(10)

    def OrientCopter(self, expectedLocation):
        self.bebop.smart_sleep(5)
        # realLocation = Localisation.GetPosition()
        print('Expected location ' + str(expectedLocation))
        # print('Real location ' + str(realLocation))
        # error = numpy.subtract(realLocation, expectedLocation)
        # print('Error ' + str(error))
        # self.bebop.move_relative(-error[1], -error[0], 0, 0)
