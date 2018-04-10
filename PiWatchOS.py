import pygame
import os
import time
import DisplayImage
import MainMenu

os.putenv('SDL_FBDEV', '/dev/fb1')
pygame.init()
pygame.mouse.set_visible(False)

DisplayImage.LoadingScreen(0)

MainMenu.DrawMenu()
MainMenu.MenuButtons()

