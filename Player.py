from SpriteManager import *
from config import *
from math import *
class Player:
    import config
    def __init__(self, coord):
        self.coord = coord
        self.v_coord = [(coord[0]), abs(coord[1])]

        self.animation_state = 0

        self.jump_state = 0
        self.can_jump = True


    def gravity(self):
        height = GROUND - self.v_coord[1]
        if self.v_coord[1] < GROUND:
            self.v_coord[1] += speed(height)/2
            self.v_coord[1] = ceil(self.v_coord[1])
        else :
            self.v_coord[1] = GROUND


    def is_player_on_ground(self):
        if self.v_coord[1] == GROUND:
            self.can_jump = True


    def walk(self, direction):
        reverse = False if direction > 0 else True
        self.gravity()
        self.v_coord[0] += direction*8
        self.animation_state = self.animation_state+1 if self.animation_state < 3 else 0
        if self.animation_state == 2:
            self.animation_type = "walk2" if self.animation_type == "walk1" else "walk1"
        self.display(reverse)
        self.is_player_on_ground()


    def jump(self):
        if self.can_jump==True and self.jump_state < 5:
            self.jump_state += 1
            self.v_coord[1] -= 25-self.jump_state
            self.animation_type = "jump"

        else :
            self.jump_state = 0
            self.gravity()
            self.can_jump = False

        self.display()

    def stay(self):
        self.gravity()
        self.animation_type = "stay"
        self.display()
        self.is_player_on_ground()



    def display(self, is_reversed:bool=False):
        PLAYER.display(self.coord, self.animation_type, is_reversed)