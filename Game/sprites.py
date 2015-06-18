"""
All the game sprites that will be used
"""

from Base.generics import GenericSprite

import pygame
import math
from pygame import sprite


class GameSprite(GenericSprite):
    def __init__(self, image, position):
        GenericSprite.__init__(self, image, position)
        self.speed = 0
        self.size = self.iamge.get_rect().size


    def update(self, time):
        multiplier = time / 1000.0
        self.move(multiplier)
        self.update_rect()

    def move(self, multiplier):
        pass

    def remove(self):
        self.kill()
        del self



class Sprite(sprite.Sprite):
    def __init__(self, event_manager, position, image):
        sprite.Sprite.__init__(self)
        self.event_manager = event_manager
        self.event_manager.register_listener(self)
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.speed = 0
        self.position = position
        self.image = image
        self.width, self.height = self.image.get_rect().size

    def update_rect(self):
        left = self.position[0] - self.width / 2
        top = self.position[1] - self.height / 2
        self.rect = pygame.Rect(left, top, self.width, self.height)

    def update(self, time):
        multiplier = time / 1000.0
        self.move(multiplier)
        self.update_rect()

    def move(self, multiplier):
        pass

    def remove(self):
        self.kill()
        del self


class MissileSprite(Sprite):
    def __init__(self, event_manager, position, image):
        Sprite.__init__(self, event_manager, position, image)
        self.image_copy = image
        self.minor, self.major = self.width, self.height
        self.a, self.b = self.width / 2, self.height / 2
        self.angle = 0

    def change_direction(self, multiplier):
        pass

    def check_collision(self):
        pass

    def rotate_image(self):
        self.image = pygame.transform.rotate(self.image_copy, math.degrees(self.angle + math.pi / 2))

    def update(self, time):
        multiplier = time / 1000.0
        self.change_direction(multiplier)
        self.move(multiplier)
        self.update_rect()
        self.rotate_image()
