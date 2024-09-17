from Environment.PuzzleEnvironment import PuzzleEnvironment
from Agent.PuzzleAgent import PuzzleAgent

def print_state(state):
    for row in state:
        print(row)
    print()

n = int(input("Enter the size of the board (nxn): "))
technique = input("Enter the technique to use ('a_star' or 'greedy'): ").lower()
heuristic = input("Enter the heuristic to use ('out_of_place', 'manhattan_distance', 'euclidean_distance'): ").lower()

environment = PuzzleEnvironment(n)

# initial_state = [[7, 1, 3], [8, 0, 2], [5, 4, 6]]
# initial_state = [[1,2,3], [4, 5, 6], [8, 7, 0]]
initial_state = environment.initial_state # to use a random state
environment.set_initial_state(initial_state)

goal_state = environment.goal_state

print(f"Initial state ({n}x{n}):")
print_state(initial_state)

print(f"Goal state ({n}x{n}):")
print_state(goal_state)

agent = PuzzleAgent(n, technique, heuristic)

agent.set_initial_state(initial_state)
agent.set_goal_state(goal_state)

agent.program()

actions = agent.get_actions()

if actions:
    print("The agent found the solution. The steps are:")
    for step, state in enumerate(actions):
        print(f"Step {step}:")
        print_state(state)
    print(f"Total moves: {agent.get_cost(actions)}")
else:
    print("No solution found.")
