import pygame
import os
import time
import DisplayImage
os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()

DisplayImage.LoadingScreen(0)
