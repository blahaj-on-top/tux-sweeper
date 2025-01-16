import pygame
import grid
from fieldgen import Mines

# pygame setup
pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TUX-SWEEPER')
clock = pygame.time.Clock()
pygame.display.set_icon(pygame.image.load('assets/icon.png'))
running = True
minecoords = Mines.generateMines()
print(minecoords)

# some more vars
font = pygame.font.Font('Comic Sans MS.ttf', 32)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
mousepress = pygame.mouse.get_pressed()
x, y = 0, 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        grid.drawGrid()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            grid.unselectBlock(x, y)
            x, y = pygame.mouse.get_pos()
            print(x, y)
            pos = grid.getGridPos()
            print(pos)
            if pos in minecoords:
                gameover()
            grid.selectBlock()


    # game over
    def gameover():
        text = font.render('hahahdhdh get wreckd', True, green, blue)
        textRect = text.get_rect()
        textRect.center = (screen_width // 2, screen_height // 2)
        while True:
            screen.blit(text, textRect)
            pygame.display.flip()
            pygame.display.update()
            pygame.time.wait(100)
            running = False
 

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
