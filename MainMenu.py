import pygame
import os
from time import sleep
import RPi.GPIO as GPIO
import PiClock
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
lcd = pygame.display.set_mode((320, 240))

#Creates Button Map
button_map = {23:(255,0,0), 22:(0,255,0), 27:(0,0,255), 17:(0,0,0)}

#Sets Buttons to Normally Open
GPIO.setmode(GPIO.BCM)
for k in button_map.keys():
    GPIO.setup(k, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Color Pallette
WHITE = (255,255,255)
GREY = (240,240,240)

#Code to Draw The Menu
def DrawMenu():
    my_image = pygame.image.load('MenuImage.png')

    lcd.blit(my_image, (0, 0))
    pygame.display.update()
    
#Code to Check For Button Presses
def MenuButtons():
    DrawMenu()
    MenuIsDrawn = 1
    font_medium = pygame.font.Font(None, 50)

    while MenuIsDrawn == 1:
        # Scan the buttons
        for (k,v) in button_map.items():
            if GPIO.input(k) == False:
                if k == 27:
                    PiClock.DisplayTime()
                elif k == 23:
                    lcd.fill((0,0,0)) 
                    text_surface = font_medium.render('Weather', True, WHITE)
                    rect = text_surface.get_rect(center=(160,120))
                    lcd.blit(text_surface, rect)
                    pygame.display.update()
                    sleep(1)
                    MenuIsDrawn = 0
                elif k == 22:
                    lcd.fill((0,0,0))
                    text_surface = font_medium.render('Games', True, WHITE)
                    rect = text_surface.get_rect(center=(160,120))
                    lcd.blit(text_surface, rect)
                    pygame.display.update()
                    sleep(1)
                    MenuIsDrawn = 0
                else:
                    lcd.fill((0,0,0))
                    text_surface = font_medium.render('Return', True, WHITE)
                    rect = text_surface.get_rect(center=(160,120))
                    lcd.blit(text_surface, rect)
                    pygame.display.update()
                    sleep(1)
                    MenuIsDrawn = 0
        sleep(1)
