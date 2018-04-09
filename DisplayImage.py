import pygame
import os
import time
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()

def LoadingScreen(x):
    lcd = pygame.display.set_mode((320, 240))
    pygame.mouse.set_visible(False)

    my_image = pygame.image.load('PiWatchLogo.png')

    lcd.blit(my_image, (0, 0))
    pygame.display.update()

    progress = x
    while progress <= 100 :
        percentage = progress/100;
        pygame.draw.rect(lcd, (255-(255*percentage),255*percentage,0), pygame.Rect(0,235,320*percentage,5))
        pygame.display.update()
        progress += 1
        time.sleep(.05)
