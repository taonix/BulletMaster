import pygame
from SpriteManager import *
from config import *
from Player import *
class Model:

    def __init__(self, sprite, coord, z_index, size):
        self.sprite = sprite
        self.coord = coord
        self.v_coord = [abs(coord[0]), abs(coord[1])]
        self.z_index = z_index
        self.size = size

    def display(self):
        BACKGROUND.display(self.coord, self.sprite)