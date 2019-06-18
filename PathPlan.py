from PathPlanning.AStarRosetta import AStarGraph, AStarSearch


class PathPlan:

    def __init__(self, start, goal, barriers, display):
        self.goal = goal
        self.barriers = barriers
        self.start = start
        self.graph = AStarGraph(barriers)
        self.result, self.cost, self.path = AStarSearch(start, goal, self.graph, display)
        self.index = 0

    def getNextMove(self):
        self.index += 1
        nextStep = self.path[self.index]
        return nextStep

    def getResult(self):
        return self.result
