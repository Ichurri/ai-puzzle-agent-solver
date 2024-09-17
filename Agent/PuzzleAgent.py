from .SearchAgent import SearchAgent
import math
from copy import deepcopy

class PuzzleAgent(SearchAgent):
    def __init__(self, n, technique, heuristic):
        super().__init__()
        self.n = n
        self.heuristic = heuristic
        self.set_technique(technique)
        self.add_function(self.move_up)
        self.add_function(self.move_down)
        self.add_function(self.move_left)
        self.add_function(self.move_right)

    def move_up(self, state):
        return self.move(state, -1, 0)

    def move_down(self, state):
        return self.move(state, 1, 0)

    def move_left(self, state):
        return self.move(state, 0, -1)

    def move_right(self, state):
        return self.move(state, 0, 1)

    def move(self, state, dx, dy):
        new_location = deepcopy(state)
        x, y = [(ix, iy) for ix, row in enumerate(state) for iy, i in enumerate(row) if i == 0][0]
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < self.n and 0 <= new_y < self.n:
            new_location[x][y], new_location[new_x][new_y] = new_location[new_x][new_y], new_location[x][y]
            return new_location
        return None

    def find_goal_position(self, value, goal):
        for ix, row in enumerate(goal):
            if value in row:
                return ix, row.index(value)

    def get_heuristic(self, path):
        current_state = path[-1]
        if self.heuristic == "out_of_place":
            return self.heuristic_pieces_out_of_place(current_state)
        elif self.heuristic == "manhattan_distance":
            return self.heuristic_manhattan(current_state)
        elif self.heuristic == "euclidean_distance":
            return self.heuristic_euclidean(current_state)

    def heuristic_pieces_out_of_place(self, state):
        goal = self.get_goal_state()
        return sum(1 for i in range(self.n) for j in range(self.n) if state[i][j] != 0 and state[i][j] != goal[i][j])

    def heuristic_manhattan(self, state):
        goal = self.get_goal_state()
        distance = 0
        for i in range(self.n):
            for j in range(self.n):
                if state[i][j] != 0:
                    x_goal, y_goal = self.find_goal_position(state[i][j], goal)
                    distance += abs(x_goal - i) + abs(y_goal - j)
        return distance

    def heuristic_euclidean(self, state):
        goal = self.get_goal_state()
        distance = 0
        for i in range(self.n):
            for j in range(self.n):
                if state[i][j] != 0:
                    x_goal, y_goal = self.find_goal_position(state[i][j], goal)
                    distance += math.sqrt((x_goal - i)**2 + (y_goal - j)**2)
        return distance