import pygame
import sys
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

n = 3
TILE_SIZE = 150
WINDOW_SIZE = TILE_SIZE * n

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Rompecabezas NxN")

font = pygame.font.Font(None, 72)

def draw_board(screen, state, TILE_SIZE):
    screen.fill(WHITE)
    for i in range(n):
        for j in range(n):
            tile = state[i][j]
            pygame.draw.rect(screen, BLACK, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE), 2)
            text = font.render(str(tile), True, BLACK)
            text_rect = text.get_rect(center=(j * TILE_SIZE + TILE_SIZE // 2, i * TILE_SIZE + TILE_SIZE // 2))
            screen.blit(text, text_rect)
    pygame.display.flip()

def move_tile(state, direction):
    x, y = [(ix, iy) for ix, row in enumerate(state) for iy, i in enumerate(row) if i == 0][0]

    if direction == 'up' and x > 0:  # Mover hacia arriba
        state[x][y], state[x - 1][y] = state[x - 1][y], state[x][y]
    elif direction == 'down' and x < n - 1:  # Mover hacia abajo
        state[x][y], state[x + 1][y] = state[x + 1][y], state[x][y]
    elif direction == 'left' and y > 0:  # Mover hacia la izquierda
        state[x][y], state[x][y - 1] = state[x][y - 1], state[x][y]
    elif direction == 'right' and y < n - 1:  # Mover hacia la derecha
        state[x][y], state[x][y + 1] = state[x][y + 1], state[x][y]
    return state

def generate_puzzle(n):
    numbers = list(range(n * n))
    random.shuffle(numbers)
    board = [numbers[i * n:(i + 1) * n] for i in range(n)]
    return board

def check_win(state):
    correct = list(range(1, n * n)) + [0]
    flat_state = [num for row in state for num in row]
    return flat_state == correct

board_state = generate_puzzle(n)

running = True
while running:
    draw_board(screen, board_state, TILE_SIZE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                board_state = move_tile(board_state, 'up')
            if event.key == pygame.K_DOWN:
                board_state = move_tile(board_state, 'down')
            if event.key == pygame.K_LEFT:
                board_state = move_tile(board_state, 'left')
            if event.key == pygame.K_RIGHT:
                board_state = move_tile(board_state, 'right')

            if check_win(board_state):
                print("¡Felicidades! Has resuelto el rompecabezas.")
                running = False

pygame.quit()
