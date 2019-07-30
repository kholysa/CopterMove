from PathPlanning.AStarRosetta import AStarGraph, AStarSearch
import numpy

class PathPlan:

    stepSize = 0.1
    def __init__(self, start, goal, barriers, display):
        self.goal = goal
        self.barriers = barriers
        self.start = start
        self.previousPosition = start
        self.graph = AStarGraph(barriers)
        AStarSearch(start, goal, self.graph,  display)
        self.index = 0

    def getExpectedPosition(self):
        nextJump = self.graph.getJumpValues()[self.index]
        expectedPosition = numpy.add(nextJump,self.previousPosition)
        self.index += 1
        self.previousPosition = expectedPosition
        return expectedPosition

    def getResult(self):
        return self.graph.getJumpValues()
