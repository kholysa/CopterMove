from PathPlanning.AStarRosetta import AStarGraph, AStarSearch


class PathPlan:

    stepSize = 0.1
    def __init__(self, start, goal, barriers, stepSizeDrone, display):
        PathPlan.stepSize = stepSizeDrone
        self.goal = goal
        self.barriers = barriers
        self.start = start
        self.graph = AStarGraph(barriers, PathPlan.stepSize)
        self.result, self.cost, self.path = AStarSearch(start, goal, self.graph, PathPlan.stepSize, display)
        self.index = 0

    def getNextMove(self):
        self.index += 1
        nextStep = self.path[self.index]
        return nextStep

    def getResult(self):
        return self.result
