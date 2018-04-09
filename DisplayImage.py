import pygame
import os
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
lcd = pygame.display.set_mode((320, 240))
pygame.mouse.set_visible(False)

my_image = pygame.image.load('ThePiWatch.png')

while 1 != 0:
    lcd.blit(my_image, (0, 0))
    pygame.display.update()
