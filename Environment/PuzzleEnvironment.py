from .Environment import  Environment
import random

class PuzzleEnvironment(Environment):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.initial_state = self.generate_initial_state()
        self.goal_state = self.generate_goal_state()

    def set_initial_state(self, s):
        self.initial_state = s

    def generate_goal_state(self):
        goal = list(range(1, self.n * self.n)) + [0]
        return [goal[i:i + self.n] for i in range(0, len(goal), self.n)]

    def generate_initial_state(self):
        state = list(range(self.n * self.n))
        while True:
            random.shuffle(state)
            if self.is_valid_state(state):
                return [state[i:i + self.n] for i in range(0, len(state), self.n)]

    def is_valid_state(self, state):
        inversions = 0
        flat_state = [num for num in state if num != 0]
        for i in range(len(flat_state)):
            for j in range(i + 1, len(flat_state)):
                if flat_state[i] > flat_state[j]:
                    inversions += 1
        if self.n % 2 == 1:
            return inversions % 2 == 0
        else:
            row_of_zero = state.index(0) // self.n
            return (inversions + row_of_zero) % 2 == 0