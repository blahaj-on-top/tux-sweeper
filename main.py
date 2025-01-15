import pygame
import grid

# pygame setup
pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('TUX-SWEEPER')
clock = pygame.time.Clock()
pygame.display.set_icon(pygame.image.load('assets/icon.png'))
running = True

# some more vars
WHITE = pygame.Color(255, 255, 255)
mousepress = pygame.mouse.get_pressed()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        grid.drawGrid()
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, y)
            print(grid.getGridPos())
            grid.selectBlock()


    # fill the screen with a color to wipe away anything from last frame
    

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
