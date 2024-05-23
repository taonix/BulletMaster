import pygame

from SpriteManager import BULLETS, BACKGROUND
from config import bullet_path, WIDTH, HEIGHT


class Bullet:

    def __init__(self, coord, vx, vy, type, angle):
        self.coord = coord
        self.vx = vx
        self.vy = vy
        self.type = type
        self.angle = angle

        self.animation_frame = 1

    def display(self):
        self.coord = bullet_path(self.coord[0], self.coord[1], self.animation_frame, self.vx*80, self.vy, self.angle)
        self.animation_frame += 0.02

        BULLETS.display((self.coord[0], HEIGHT-self.coord[1]), self.type)