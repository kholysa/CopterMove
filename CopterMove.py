from Localisation import Localisation
from PathPlan import PathPlan
import numpy


class CopterMove:
    def __init__(self, bebop, start, goal, barriers, scale, display=False):
        self.bebop = bebop
        self.localisation = Localisation()
        self.pathPlan = PathPlan(start, goal, barriers, display)
        self.setScaleFactor(scale)
        bebop.set_max_altitude(1.4)
        bebop.safe_takeoff(10)
        bebop.move_relative(0, 0, -0.6,0 )
        self.OrientCopter(start)

    def setScaleFactor(self,scale):
        self.scale = scale

    def Move(self):
        # print(self.localisation.GetPosition())
        for target in self.pathPlan.getResult():
            self.bebop.move_relative(target[1]/self.scale, target[0]/self.scale, 0, 0)
            self.OrientCopter(self.pathPlan.getExpectedPosition())
        # print(self.localisation.GetPosition())
        self.bebop.safe_land(10)

    def OrientCopter(self, expectedLocation):
        self.bebop.smart_sleep(5)
        realLocation = Localisation.GetPosition()
        print('Expected location ' + str(numpy.divide(expectedLocation,self.scale)))
        print('Real location ' + str(realLocation))
        error = numpy.subtract(realLocation, numpy.divide(expectedLocation,self.scale))
        print('Error ' + str(error))
        self.bebop.move_relative(-error[1], -error[0], 0, 0)
