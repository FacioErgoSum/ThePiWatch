import pygame
import os
import datetime
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
lcd = pygame.display.set_mode((320, 240))

class item:

    def __init__(self,imagename,colorkey,left,top):
        self.img = pygame.image.load(imagename).convert()
        if colorkey == -1:
            ckey = self.img.get_at((0,0))
            self.img.set_colorkey(ckey, RLEACCEL)
        self.rect = self.img.get_rect()
        self.left = left
        self.top = top
        self.width = self.rect.width
        self.height = self.rect.height
        self.center = self.rect.center

    def draw(self):
        screen.blit(self.img,(self.left, self.top))

    def setaxis(self,axis):
        self.axis = axis

    def drawrot(self,axis,angle):
        #Create new rotated image: preserve original
        self.newimg = pygame.transform.rotate(self.img,angle).convert()
        self.newrect = self.newimg.get_rect()
        #Now center the new rectangle to the rotation axis
        self.newrect.left = axis[0]-(self.newrect.w/2)
        self.newrect.top = axis[1]-(self.newrect.h/2)
        lcd.blit(self.newimg,(self.newrect.left, self.newrect.top))

def DisplayTime():
    #Color Palette
    WHITE = (255,255,255)
    GREY = (54,54,54)
    BLACK = (0,0,0)

    #Clear Screen
    lcd.fill(GREY)
    pygame.display.update()

    #Set Clock Font
    font = pygame.font.Font('Quicksand-Bold.otf', 63)

    #Load Clock Background       
    bg = item("WatchBkg.jpg",0,0,0)
    bg.setaxis((bg.width/2,86))

    #Load Hand Images
    longhand = item("minute-hand.bmp",-1,90,23)
    shorthand = item("hour-hand.bmp",-1,90,40)
    secondhand = item("second-hand.bmp",-1,90,23)

    showingClock = 1

    #Displays the Clock
    while showingClock == 1:

        #Time Variables
        dt=str(datetime.datetime.today())
        hr = float(dt[11:13])
        min = float(dt[14:16])
        sec = float(dt[17:19])
        time = dt[11:19]

        #Redraw Background
        bg.draw()
    
        #Calculate Angles For Times
        second = -360.0/60*sec +1
        minute = -360.0/60*min +1     

        hour = hr % 12
        hour1 = -360.0/12*hour +1

        #Calculate Rotation
        offset = 360.0/12/60*min
        hour = hour1-offset

        #Draw The Hands
        longhand.drawrot(bg.axis,minute)
        shorthand.drawrot(bg.axis,hour)
        secondhand.drawrot(bg.axis,second)

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

DisplayTime()
