import pygame

#vars
screen_width = 600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
WHITE = pygame.Color(255, 255, 255)

#draw grid
def drawGrid():
    blockSize = 50 #Set the size of the grid block
    for x in range(0, screen_width, blockSize):
        for y in range(0, screen_height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, WHITE, rect, 1)

#calculate mouse position in grid
def getGridPos():
    blockSize = 50
    x, y = pygame.mouse.get_pos()
    gridX = x // blockSize
    gridY = y // blockSize
    return gridX, gridY