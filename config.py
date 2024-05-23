import random

import pygame
from math import sqrt, cos, sin

# CONSTANT
GRAVITY = 9.8
PLAYER_WEIGHT = 70

WIDTH = 800
HEIGHT = 530

DIVIDE_FACTOR = 100

GROUND = HEIGHT-(120+50) + 2

# Equations physiques
speed = lambda h: sqrt(2 * GRAVITY * h)
bullet_path = lambda x, y, t, vx, vy, angle: (vx*cos(angle)*t*t, -1/2 * GRAVITY * t**1.5 + vy*(random.uniform(0.1, 1)) * sin(angle)*t + y )

# Initialisation de Pygame
pygame.init()

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Bullet Master")
pygame.display.set_icon(pygame.image.load('src/icon.png'))

font = pygame.font.SysFont('Comic Sans MS', 30)
