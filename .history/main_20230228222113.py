from search import *

class WolfGoatCabbage(Problem):
    def __init__(self, initial=frozenset({'F', 'W', 'G', 'C'}), goal=set()):
        super().__init__(initial, goal)

    def goal_test(self, state):
        return state == self.goal

    def result(self, state, action):
        pass

    def result(self, state, actions):
        new_state = set(state)
        new_state.update(set(actions - state))
        new_state.difference_update(state.intersection(actions))
        return frozenset(new_state)
if __name__ == '__main__':
    wgc = WolfGoatCabbage()
    solution = depth_first_graph_search(wgc).solution()
    print(solution)
    solution = breadth_first_graph_search(wgc).solution()
    print(solution)
