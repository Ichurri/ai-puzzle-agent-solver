import time
from Environment.PuzzleEnvironment import PuzzleEnvironment
from Agent.PuzzleAgent import PuzzleAgent

def run_tests(n, num_tests, heuristic):
    results = {
        "a_star": {"solved": 0, "total_moves": 0, "total_time": 0, "max_frontier": 0, "total_steps": 0},
        "greedy": {"solved": 0, "total_moves": 0, "total_time": 0, "max_frontier": 0, "total_steps": 0}
    }

    for i in range(num_tests):
        print(f"Test {i + 1}/{num_tests}")

        environment = PuzzleEnvironment(n)
        initial_state = environment.initial_state
        goal_state = environment.goal_state

        for technique in ["a_star", "greedy"]:
            agent = PuzzleAgent(n, technique, heuristic)
            agent.set_initial_state(initial_state)
            agent.set_goal_state(goal_state)

            start = time.time()
            agent.program()
            solve_time = time.time() - start

            actions = agent.get_actions()
            if actions:
                moves = agent.get_cost(actions)
                steps = len(actions)

                results[technique]["solved"] += 1
                results[technique]["total_moves"] += moves
                results[technique]["total_steps"] += steps

            results[technique]["total_time"] += solve_time

            max_frontier = len(actions) if actions else 0
            results[technique]["max_frontier"] = max(results[technique]["max_frontier"], max_frontier)

    print(f"Results for Heuristic {heuristic}")

    for technique in ["a_star", "greedy"]:
        print(f"\nResults for {technique}:")
        print(f"  - Solved: {results[technique]['solved']}/{num_tests}")
        print(f"  - Average solve time: {results[technique]['total_time'] / num_tests:.4f} seconds")
        if results[technique]["solved"] > 0:
            print(f"  - Average moves: {results[technique]['total_moves'] / results[technique]['solved']:.2f}")
            print(f"  - Average steps: {results[technique]['total_steps'] / results[technique]['solved']:.2f}")
        print(f"  - Maximum frontier size: {results[technique]['max_frontier']}")

n = int(input("Enter the size of the board: "))
num_tests = int(input("Enter the number of tests to run: "))
heuristic = input("Enter the heuristic to use ('out_of_place', 'manhattan_distance', 'euclidean_distance'): ")

run_tests(n, num_tests, heuristic)