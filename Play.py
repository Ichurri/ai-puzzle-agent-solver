import sys
from Environment.PuzzleEnvironment import PuzzleEnvironment
from Agent.PuzzleAgent import PuzzleAgent

def print_state(state):
    for row in state:
        print(row)
    print()

def move_user(state, move):
    new_position = [row[:] for row in state]
    x, y = [(ix, iy) for ix, row in enumerate(state) for iy, i in enumerate(row) if i == 0][0]

    if move == 'w' and x > 0:
        new_position[x][y], new_position[x - 1][y] = new_position[x - 1][y], new_position[x][y]
    elif move == 's' and x < len(state) - 1:
        new_position[x][y], new_position[x + 1][y] = new_position[x + 1][y], new_position[x][y]
    elif move == 'a' and y > 0:
        new_position[x][y], new_position[x][y - 1] = new_position[x][y - 1], new_position[x][y]
    elif move == 'd' and y < len(state[0]) - 1:
        new_position[x][y], new_position[x][y + 1] = new_position[x][y + 1], new_position[x][y]
    else:
        print("Invalid move.")
        return state
    return new_position

def play(n):
    environment = PuzzleEnvironment(n)
    initial_state = environment.initial_state
    goal_state = environment.goal_state

    current_state = initial_state

    print("NxN Puzzle")
    print_state(current_state)

    while True:
        print("Moves: w (up), s (down), a (left), d (right), r (solve with agent), q (quit)")
        action = input("Enter your move: ").lower()

        if action == 'q':
            sys.exit()

        elif action == 'r':
            print("Agent solving the puzzle")
            technique = input("Choose technique ('a_star' or 'greedy'): ").lower()
            heuristic = input(
                "Choose heuristic (1: 'out_of_place', 2: 'manhattan_distance', 3: 'euclidean_distance'): ")

            agent = PuzzleAgent(n, technique=technique, heuristic=heuristic)
            agent.set_initial_state(current_state)
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
                print("The agent could not find a solution.")
            break

        elif action in ['w', 's', 'a', 'd']:
            current_state = move_user(current_state, action)
            print_state(current_state)

            if current_state == goal_state:
                break
        else:
            print("Invalid command. Try again.")

n = int(input("Enter the size of the board (nxn): "))
play(n)