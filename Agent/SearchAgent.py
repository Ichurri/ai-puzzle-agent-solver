from .Agent import Agent
from copy import deepcopy
import time

class SearchAgent(Agent):
    def __init__(self):
        super().__init__()
        self.__initial_state = None
        self.__goal_state = None
        self.__successor_functions = []
        self.__technique = None

    def set_initial_state(self, e0):
        self.__initial_state = e0

    def set_goal_state(self, ef):
        self.__goal_state = ef

    def get_initial_state(self):
        return self.__initial_state

    def get_goal_state(self):
        return self.__goal_state

    def set_technique(self, t):
        self.__technique = t

    def add_function(self, f):
        self.__successor_functions.append(f)

    def test_goal(self, e):
        return e == self.__goal_state

    def generate_children(self, e):
        children = []
        for func in self.__successor_functions:
            new_state = func(e)
            if new_state is not None:
                children.append(new_state)
        return children

    def get_cost(self, path):
        return len(path) - 1  # Number of moves made

    def get_heuristic(self, path):
        raise NotImplementedError("This method must be implemented in subclasses")

    def get_A_function(self, path):
        return self.get_cost(path) + self.get_heuristic(path)

    def measure_time(function):
        def measured_function(*args, **kwargs):
            start = time.time()
            result = function(*args, **kwargs)
            print("Execution time: ", time.time() - start)
            return result
        return measured_function

    @measure_time
    def program(self):
        frontier = [[self.__initial_state]]
        visited = []
        while frontier:
            if self.__technique == "depth":
                path = frontier.pop()
            else:
                path = frontier.pop(0)
            node = path[-1]
            visited.append(node)
            if self.test_goal(node):
                self.set_actions(path)
                break
            else:
                for child in self.generate_children(node):
                    if child not in visited:
                        aux = deepcopy(path)
                        aux.append(child)
                        frontier.append(aux)
                if self.__technique == "uniform_cost":
                    frontier.sort(key=lambda x: self.get_cost(x))
                elif self.__technique == "greedy":
                    frontier.sort(key=lambda x: self.get_heuristic(x))
                elif self.__technique == "a_star":
                    frontier.sort(key=lambda x: self.get_A_function(x))
