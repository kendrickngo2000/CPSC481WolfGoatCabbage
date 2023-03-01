from search import *

class WolfGoatCabbage(Problem):
    def __init__(self, initial=frozenset({'F', 'W', 'G', 'C'}), goal=set()):
        super().__init__(initial, goal)

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
