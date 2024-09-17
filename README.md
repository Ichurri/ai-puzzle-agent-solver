
# NxN Puzzle Solver and Environment

## Project Overview

This project implements an **NxN puzzle solver** using different search techniques and heuristics. The puzzle-solving environment supports both **automated agents** and **manual player interaction**. The primary goal is to develop an AI agent that can solve NxN puzzles, such as the 8-puzzle problem, using various techniques like **A* search** and **greedy search**, with the choice of heuristics to guide the search process.

The project is structured in a modular way to allow ease of expansion. It comprises different components, including **environment simulation**, **search agents**, and **graphical interface** using **Pygame** for visualization of the puzzle-solving process.

## Table of Contents

- [Project Overview](#project-overview)
- [Theoretical Foundations](#theoretical-foundations)
  - [Search Techniques](#search-techniques)
  - [Heuristics](#heuristics)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [How to Run](#how-to-run)
- [Usage](#usage)
  - [Automated Agent](#automated-agent)
  - [Manual Player](#manual-player)
- [Future Improvements](#future-improvements)

## Theoretical Foundations

### Search Techniques

This project is built around the classical AI search techniques used for solving combinatorial puzzles, specifically the NxN puzzle:

- **A* Search Algorithm**: A* is an informed search algorithm that uses both the cost to reach a node (actual path cost) and a heuristic estimate of the cost to reach the goal. It guarantees finding the optimal solution by balancing exploration of known costs with future heuristics.

- **Greedy Search Algorithm**: Greedy search focuses solely on minimizing the heuristic function without considering the actual path cost. This can lead to quicker but non-optimal solutions since it may overlook more promising paths.

### Heuristics

Heuristics are essential in guiding the search algorithms toward the solution efficiently. The project supports three common heuristics:

- **Out of Place Heuristic**: This heuristic counts the number of tiles that are not in their goal positions. It is simple but less informative than other heuristics.

- **Manhattan Distance Heuristic**: This heuristic sums the vertical and horizontal distances of tiles from their goal positions. It is more informative and commonly used in A* algorithms for puzzle solving.

- **Euclidean Distance Heuristic**: This heuristic calculates the straight-line distance between the current tile position and its goal. It can provide an estimate of the effort needed to move the tiles but may not always be as efficient as the Manhattan distance.

## Project Structure

The project is organized into several Python modules:

- **`Agent.py`**: Defines the base class for agents, including the perception and action handling for the environment.
  
- **`SearchAgent.py`**: Implements a search agent capable of solving the puzzle using various search techniques.
  
- **`PuzzleAgent.py`**: Extends the search agent to handle the specific movement rules and heuristics for the NxN puzzle.

- **`Environment.py`**: Provides the general framework for an environment where agents operate.

- **`PuzzleEnvironment.py`**: Specializes the environment class for NxN puzzle states, including the generation of random initial states and goal states.

- **`Images.py`**: Provides a graphical visualization of the puzzle using Pygame.

- **`Play.py`**: Allows manual user interaction with the puzzle, letting players solve the puzzle or invoke the AI agent to do it.

- **`main.py`**: The main execution file that allows testing different configurations of the puzzle, techniques, and heuristics.

- **`Test.py`**: Provides automated testing functions to evaluate the performance of the agents across multiple trials.

## Setup and Installation

To run the project, you need Python 3.x and the following libraries:

- **Pygame**: For graphical visualization
- **time**: Standard Python library for time measurement
- **copy**: Standard Python library for state copying

To install the required packages, run:
```bash
pip install pygame
```

## How to Run

### Run the Automated Puzzle Solver:

You can execute the puzzle solver with an automated agent by running the `main.py` file. This allows you to configure the puzzle size, search technique, and heuristic.

```bash
python main.py
```

You will be prompted to enter the size of the board (e.g., 3 for a 3x3 board), the search technique (`a_star` or `greedy`), and the heuristic (`out_of_place`, `manhattan_distance`, or `euclidean_distance`).

### Run the Images Puzzle Solved Step by Step:

You can run the script that provides a graphical interface to visualize the puzzle-solving process. The agent will automatically solve the puzzle, and you can watch the progress on the screen by running `Images.py`.

```bash
python Images.py
```

### Run the Automated Testing Functions:

You can run the script that is used for running multiple automated tests to evaluate the performance of the puzzle solver. You can specify the size of the board, the number of tests, and the heuristic you want to use by running `Tests.py`. 

```bash
python Tests.py
```

### Run the Interactive Puzzle Game:

You can play the NxN puzzle interactively or let the agent solve it for you by running `Play.py`.

```bash
python Play.py
```

You will have the following options during the game:

- **w**: Move the blank tile up
- **s**: Move the blank tile down
- **a**: Move the blank tile left
- **d**: Move the blank tile right
- **r**: Solve the puzzle with the agent
- **q**: Quit the game

## Usage

### Automated Agent

In automated mode, the agent will solve the puzzle using the technique and heuristic you provide. The solution steps, along with the total number of moves, will be displayed in the terminal.

### Manual Player

In manual mode, the user can solve the puzzle interactively by moving the blank tile in the puzzle. Additionally, the player can request the AI agent to solve the puzzle at any point by pressing `r`.

## Future Improvements

Here are a few areas where the project can be further improved:

- **Performance Optimizations**: The current implementation can be optimized further by refining the data structures and algorithm efficiency.
  
- **Additional Heuristics**: Adding more sophisticated heuristics could improve agent performance for larger puzzles.

- **Graphical Interface**: Enhancing the graphical interface with better visuals and more detailed progress tracking during agent execution.

- **Support for Other Search Techniques**: Implementing additional search algorithms.
