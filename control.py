import pygame
from pygame.locals import *

class Control:
    def __init__(self):
        self.game = True
        self.way = "R"
        self.pause = True
    
    def control(self):
        """Управление"""
        for event in pygame.event.get():
            if event.type == QUIT:
                self.game = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.game = False
                elif event.key == K_RIGHT   and self.way != "L":
                    self.way = "R"
                elif event.key == K_LEFT    and self.way != "R":
                    self.way = "L"
                elif event.key == K_UP      and self.way != "DOWN":
                    self.way = "UP"
                elif event.key == K_DOWN    and self.way != "UP":
                    self.way = "DOWN"
                elif event.key == K_SPACE:
                    if self.pause:
                        self.pause = False
                    else:
                        self.pause = True