import pygame
import time
import random

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0, 255, 0)
blue = (0, 0, 255)

WIDTH = 1000
HEIGHT = 1000

INIT_FOOD = [ 10,10 ]

TICK_TIME = .02
SPAWN_FOOD_TIME = 10

BRICK_SIZE = 20

FOOD_SIZE = 20

class pySnake:

    def __init__(self):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('py-dventure')
        self.clock = pygame.time.Clock()
    
    def player_move(self, direction):
        pass

    def move(self):
        pass

    def draw(self):
        pygame.draw.rect(self.gameDisplay, green, (10, 10, 10, 10))

    def start(self):
        self.end = False
        while not self.end:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        self.player_move('up')
                    if event.key == pygame.K_a:
                        self.player_move('left')
                    if event.key == pygame.K_s:
                        self.player_move('down')
                    if event.key == pygame.K_d:
                        self.player_move('right')
                    if event.key == pygame.K_r:
                        self.__init__()
                    if event.key == pygame.K_q:
                        self.end = True
                if event.type == pygame.QUIT:
                    self.end = True
            self.gameDisplay.fill(white)
            self.move()
            self.draw()
            pygame.display.update()
            self.clock.tick(60)

a = pySnake()
a.start()
