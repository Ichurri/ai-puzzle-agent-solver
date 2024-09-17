import pygame
import sys
import random

pygame.init()

# Colores
BACKGROUND_COLOR = (187, 173, 160)
TILE_COLOR = (238, 228, 218)
TILE_EMPTY_COLOR = (205, 193, 180)
TEXT_COLOR = (119, 110, 101)

n = 3
TILE_SIZE = 150
WINDOW_SIZE = TILE_SIZE * n

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Puzzle NxN")

font = pygame.font.Font(None, 100)
win_font = pygame.font.Font(None, 80)

def draw_board(screen, state, TILE_SIZE):
    screen.fill(BACKGROUND_COLOR)
    for i in range(n):
        for j in range(n):
            tile = state[i][j]
            if tile != 0:
                pygame.draw.rect(screen, TILE_COLOR, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE), 0, 15)
                text = font.render(str(tile), True, TEXT_COLOR)
                text_rect = text.get_rect(center=(j * TILE_SIZE + TILE_SIZE // 2, i * TILE_SIZE + TILE_SIZE // 2))
                screen.blit(text, text_rect)
            else:
                pygame.draw.rect(screen, TILE_EMPTY_COLOR, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE), 0, 15)
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

def show_win_message(screen):
    win_text = win_font.render("¡Felicidades!", True, (255, 255, 255))
    text_rect = win_text.get_rect(center=(WINDOW_SIZE // 2, WINDOW_SIZE // 2))
    screen.blit(win_text, text_rect)
    pygame.display.flip()
    pygame.time.wait(2000)

board_state = generate_puzzle(n)

running = True
game_won = False
while running:
    draw_board(screen, board_state, TILE_SIZE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and not game_won:
            if event.key == pygame.K_UP:
                board_state = move_tile(board_state, 'up')
            if event.key == pygame.K_DOWN:
                board_state = move_tile(board_state, 'down')
            if event.key == pygame.K_LEFT:
                board_state = move_tile(board_state, 'left')
            if event.key == pygame.K_RIGHT:
                board_state = move_tile(board_state, 'right')

            # Comprobar si el jugador ha ganado
            if check_win(board_state):
                game_won = True
                show_win_message(screen)

pygame.quit()
