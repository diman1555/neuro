import pygame
from time import sleep
from control import Control
from snake import Snake
from food import Food
from neyro import Neuro
from numpy import array

pygame.init()
window = pygame.display.set_mode((400,400))
pygame.display.set_caption("Snake")
control = Control()
control1 = Control()
snake = Snake()
snake1 = Snake()
food = Food()
food.position = [60,60]

while control.game:
    control.control()
    if snake.dead or snake1.dead:
        break
    

    
    window.fill(pygame.Color("Gray"))
    snake.draw(window)
    snake1.draw(window)
    food.draw_food(window)

    if control.pause or control1.pause:
        snake.move(control)
        snake1.move(control1)
        neuro = Neuro(array([[
            snake.head[0],
            snake.head[1],
            food.position[0], 
            food.position[1],
            (food.position[0] - snake.head[0]),
            (food.position[1] - snake.head[1]),
            ]]), 
            control.way)
        neuro1 = Neuro(array([[
            snake1.head[0],
            snake1.head[1],
            food.position[0], 
            food.position[1],
            (food.position[0] - snake1.head[0]),
            (food.position[1] - snake1.head[1]),
            ]]), 
            control1.way)
        neuro.train()
        neuro1.train()
        neuro.errors()
        neuro1.errors()
        control.way = neuro.lol()
        control1.way = neuro1.lol()
        snake.eat(food)
        snake1.eat(food)
        snake.check_end_window()
        snake1.check_end_window()
        snake.animation()
        snake1.animation()
    pygame.display.flip()