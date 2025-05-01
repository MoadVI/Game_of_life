import pygame
import sys
import random
import math


n = int(input("Enter a huge number in the range of thousands:\n"))
sqrt_n = int(math.sqrt(n))

if int(sqrt_n**2) != n:
    n = int(sqrt_n**2)

cols = rows = int(math.sqrt(n))
grid = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
cells = {i: [] for i in range(1, n + 1)}

def state(cells, grid):
    cell = 1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            vicinity = 0
            if j + 1 < len(grid) and grid[i][j + 1] == 1:
                vicinity += 1
            if j - 1 >= 0 and grid[i][j - 1] == 1:
                vicinity += 1
            if i - 1 >= 0 and grid[i - 1][j] == 1:
                vicinity += 1
            if i - 1 >= 0 and j - 1 >= 0 and grid[i - 1][j - 1] == 1:
                vicinity += 1
            if i - 1 >= 0 and j + 1 < len(grid) and grid[i - 1][j + 1] == 1:
                vicinity += 1
            if i + 1 < len(grid) and grid[i + 1][j] == 1:
                vicinity += 1
            if i + 1 < len(grid) and j - 1 >= 0 and grid[i + 1][j - 1] == 1:
                vicinity += 1
            if i + 1 < len(grid) and j + 1 < len(grid) and grid[i + 1][j + 1] == 1:
                vicinity += 1
            cells[cell] = [grid[i][j], vicinity]
            cell += 1

def check_vicinity(cells):
    for cell in list(cells.keys()):
        vicinity = 0
        if cell % cols != 0:
            vicinity += cells[cell + 1][0]
        if (cell - 1) % cols != 0:
            vicinity += cells[cell - 1][0]
        if cell - cols > 0:
            vicinity += cells[cell - cols][0]
        if cell + cols <= n:
            vicinity += cells[cell + cols][0]
        if cell % cols != 0 and cell + cols <= n:
            vicinity += cells[cell + cols + 1][0]
        if (cell - 1) % cols != 0 and cell + cols <= n:
            vicinity += cells[cell + cols - 1][0]
        if cell % cols != 0 and cell - cols > 0:
            vicinity += cells[cell - cols + 1][0]
        if (cell - 1) % cols != 0 and cell - cols > 0:
            vicinity += cells[cell - cols - 1][0]
        cells[cell][1] = vicinity

def check_state(cells):
    for cell in range(1, n + 1):
        S = cells[cell][1]
        E = cells[cell][0]
        if (S == 3) or (E == 1 and S == 2):
            cells[cell][0] = 1
        else:
            cells[cell][0] = 0

def change_cell_color(row, col, color):
    rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
    pygame.draw.rect(screen, color, rect)

state(cells, grid)

pygame.init()

screen_width = 1000
screen_height = 700
cell_size = screen_width // cols

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Game Of Life')

def draw_grid():
    for x in range(0, cols * cell_size, cell_size):
        for y in range(0, rows * cell_size, cell_size):
            rect = pygame.Rect(x, y, cell_size, cell_size)
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)

clock = pygame.time.Clock()

fps = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    
    check_vicinity(cells)
    check_state(cells)

    draw_grid()

    for cell in range(1, n + 1):
        row = (cell - 1) // cols
        col = (cell - 1) % cols
        color = (0, 0, 0)
        if cells[cell][0] == 1:
            color = (255, 255, 255)
        change_cell_color(row, col, color)

    pygame.display.flip()

    clock.tick(fps)

pygame.quit()
