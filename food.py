import pygame
import random
import time

lolkek=[40,50,10,70,150,130,170,20,10,30,70,160,140]
lolkek1=[40,50,10,70,150,130,170,20,10,30,70,160,140]
lolkek1.reverse()
class Food:
    def __init__(self):

        self.position = [0,0]
        self.i=0

    def get_food_pos(self):
        random.seed(time.time())
        """Спавнит еду"""
        self.position[0] = lolkek[self.i]#random.randrange(0,190,10)
        self.position[1] = lolkek1[self.i]#random.randrange(0,190,10)
        self.i+=1
        if self.i>12:
            self.i=0

    def draw_food(self, window):
        """Рисует еду"""
        pygame.draw.rect(window,
                        pygame.Color("Red"),
                        pygame.Rect(self.position[0], self.position[1], 10, 10))