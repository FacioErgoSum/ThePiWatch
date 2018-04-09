import pygame
import os
import time
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()

def LoadingScreen(x):
    lcd = pygame.display.set_mode((320, 240))
    my_image = pygame.image.load('PiWatchLogo.png')

    lcd.blit(my_image, (0, 0))
    pygame.display.update()

    progress = x
    while progress <= 320 :
        pygame.draw.rect(lcd, (0,255,0), pygame.Rect(0,235,progress,5))
        pygame.display.update()
        progress += 5
        time.sleep(0.05)
