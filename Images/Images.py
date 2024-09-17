import pygame
import time
from Environment.PuzzleEnvironment import PuzzleEnvironment
from Agent.PuzzleAgent import PuzzleAgent

pygame.init()

n = 3
TILE_SIZE = 250
WINDOW_SIZE = TILE_SIZE * n

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("NxN Puzzle")

images = [
    pygame.image.load("image0_0.png"),
    pygame.image.load("image0_1.png"),
    pygame.image.load("image0_2.png"),
    pygame.image.load("image1_0.png"),
    pygame.image.load("image1_1.png"),
    pygame.image.load("image1_2.png"),
    pygame.image.load("image2_0.png"),
    pygame.image.load("image2_1.png"),
    pygame.image.load("image2_2.png"),
]


def draw_board(screen, state):
    for i in range(n):
        for j in range(n):
            tile = state[i][j]
            if tile != 0:
                screen.blit(images[tile - 1], (j * TILE_SIZE, i * TILE_SIZE))

    pygame.display.flip()


environment = PuzzleEnvironment(n)
initial_state = environment.initial_state
goal_state = environment.goal_state

agent = PuzzleAgent(n, "a_star", "manhattan_distance")
agent.set_initial_state(initial_state)
agent.set_goal_state(goal_state)

agent.program()

actions = agent.get_actions()

for state in actions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))
    draw_board(screen, state)

    time.sleep(0.05)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
