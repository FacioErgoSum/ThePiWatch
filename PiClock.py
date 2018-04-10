import pygame
import os
import datetime
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
lcd = pygame.display.set_mode((320, 240))

def DisplayTime():
    WHITE = (255,255,255)
    GREY = (54,54,54)
    BLACK = (0,0,0)

    lcd.fill(GREY)
    pygame.display.update()

    font = pygame.font.Font('Quicksand-Bold.otf', 63)

    showingClock = 1
    while showingClock == 1:
        dt=str(datetime.datetime.today())
        time = dt[11:19]

        #Set the font - Create an offset white shadow behind black
        lcd.fill(GREY)

        #Font Border
        fontimg = font.render(time,1,BLACK)
        lcd.blit(fontimg, (36,80))
        fontimg = font.render(time,1,BLACK)
        lcd.blit(fontimg, (44,80))
        fontimg = font.render(time,1,BLACK)
        lcd.blit(fontimg, (40,76))
        fontimg = font.render(time,1,BLACK)
        lcd.blit(fontimg, (40,84))

        fontimg = font.render(time,1,BLACK)
        lcd.blit(fontimg, (38,78))
        fontimg = font.render(time,1,BLACK)
        lcd.blit(fontimg, (42,82))
        fontimg = font.render(time,1,BLACK)
        lcd.blit(fontimg, (42,78))
        fontimg = font.render(time,1,BLACK)
        lcd.blit(fontimg, (38,82))

        #Actual Font
        fontimg = font.render(time,1,WHITE)
        lcd.blit(fontimg, (40,80))
        pygame.display.update()
        pygame.time.delay(500)
    
