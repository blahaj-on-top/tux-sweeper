import pygame

pygame.init()

font = pygame.font.Font('Comic Sans MS.ttf', 32)
screen_width = 500
screen_height = 500
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
 
def gameover(screen):
    text = font.render('GeeksForGeeks', True, green, blue)
    textRect = text.get_rect()
    textRect.center = (screen_width // 2, screen_height // 2)
    while True:
        screen.blit(text, textRect)