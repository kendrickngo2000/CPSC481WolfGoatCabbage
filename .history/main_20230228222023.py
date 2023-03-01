from search import *

class myProblem(Problem):
    def __init__(self, initial, goal=None):
        # constructor
        self.initial = initial
        self.goal = goal

    def actions(self, state):
        pass

    def result(self, state, action):
        pass

    def goal_test(self, state):


if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
