#Author Lauri Putkonen
# Mobs
from random import randint
import pygame
import math



class Mob:
    def __init__(self, screen, y, width, height):
        self.mobX = randint(0, width)
        self.mobY = y
        self.pic = randint(1,2)
        self.way = "right"
        self.width = width
        self.height = height
        self.image = pygame.image.load("mob_goright.png")
        self.mob_speed = randint(2,6)
        self.screen = screen

        if self.pic == 1:
            self.image = pygame.image.load("mob_goright.png")
        else:
            self.image = pygame.image.load("mob2_goright.png")

    def isCollided(self, playerX, playerY):
        #Check if mob hits to player
        distance = math.sqrt((math.pow(self.mobX - playerX, 2)) + (math.pow(playerY - self.mobY, 2)))
        if distance < 27:
            return True
    
    def move(self):           
        # Move mob and change color when hit to walls
        if self.mobX >= (self.width - 50):
            self.way = "left"
            if self.pic == 1:
                self.image = pygame.image.load("mob2_goleft.png")
            else:
                self.image = pygame.image.load("mob_goleft.png")
        elif self.mobX <= 1:
            self.way = "right"
            if self.pic == 1:
                self.image = pygame.image.load("mob_goright.png")
            else:
                self.image = pygame.image.load("mob2_goright.png")
        if self.way == "right":
            self.mobX += self.mob_speed
        else:
            self.mobX -= self.mob_speed

    def draw(self):
        self.screen.blit(self.image, (self.mobX, self.mobY))
    

