from PathPlanning.AStarRosetta import AStarGraph, AStarSearch
import numpy

class PathPlan:

    def __init__(self, start, goal, barriers, display):
        self.goal = goal
        self.barriers = barriers
        self.start = start
        self.graph = AStarGraph(barriers)
        self.result, self.cost, self.path = AStarSearch(start, goal, self.graph, display)
        self.index = 0
        self.prevCoordinate = start

    def getNextCoordinate(self):
        nextStep = self.result[self.index]
        nextCoordinate = numpy.add(self.prevCoordinate, nextStep)
        self.prevCoordinate = nextCoordinate
        self.index += 1
        return nextCoordinate

    def getResult(self):
        return self.result
