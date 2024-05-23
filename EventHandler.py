import pygame

from Bullet import Bullet
from Model import Model
from SpriteManager import CANNON, BULLETS, LANCE
from config import *
from Player import Player

from random import randint


# Initialisation des variables

player = Player(
    [WIDTH//2, GROUND]
)

background = Model(
    "background",
    [0, 0],
    0,
    [1664, 1419]
)

bullet = None
bullet_timer = 0
bullet_max_time = 30

cannon_anim_y = 0
coef_cannon_y = 1

cannon_anim_x = 0
coef_cannon_x = 1

border_coord = WIDTH//2

lance = LANCE
lance_pos = 0

vie = 10

time = 0
score = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(pygame.image.load("./src/sprites/menu.png").convert(), (0, 0))
    pygame.display.flip()

    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]: break

# Boucle de jeu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    bullet_timer += 1

    # Gestion du déplacement de l'arrière plan et du joueur
    if background.coord[0] >= player.v_coord[0]:
        player.coord = [WIDTH//2 + player.v_coord[0], player.v_coord[1]]
        background.coord = [0, 0]

    elif player.v_coord[0] + WIDTH//2 >= background.size[0] - (WIDTH//2+80):
        player.coord = [(player.v_coord[0]*WIDTH)//background.size[0], player.v_coord[1]]
        background.coord = [WIDTH - (background.size[0]-80), 0]

    else:
        player.coord = [WIDTH//2, player.v_coord[1]]

        background.v_coord = [player.v_coord[0], 0]
        background.coord = [-background.v_coord[0], 0]

    background.display()

    # Gestion des touches
    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        player.jump()
    elif key[pygame.K_q]:
        if player.coord[0] >= 0: player.walk(-1)
        else: player.stay()
    elif key[pygame.K_d]:
        if player.coord[0] <= WIDTH-50: player.walk(1)
        else: player.stay()
    else: player.stay()

    # Gestion des animations
    cannon_anim_y += coef_cannon_y
    if (cannon_anim_y >= 30 or cannon_anim_y <= 0): coef_cannon_y = -coef_cannon_y

    cannon_anim_x += coef_cannon_x
    if (cannon_anim_x >= WIDTH//6 or cannon_anim_x <= 0): coef_cannon_x = -coef_cannon_x

    lance_pos += 20
    lance.display((lance_pos, HEIGHT - 50), "default")
    if lance_pos >= WIDTH+2000: lance_pos = - lance.sprites["default"][2]

    CANNON.display((WIDTH // 2 - (BULLETS.sprites["bullet"][2]+350) + 2*cannon_anim_x, HEIGHT // 2 - 150 + cannon_anim_y), "default")

    if bullet_timer == bullet_max_time:
        bullet_timer = 0
        if bullet_max_time < 2: bullet_max_time -= 2

        bullet = Bullet(
            (WIDTH // 2 - 60000, HEIGHT // 2 + 120 - cannon_anim_y),
            15 + (cannon_anim_x/5),
            15//2,
            "bullet" if randint(0, 1) == 1 else "fired_bullet",
            30
        )

    # Gestion des collisions
    if not bullet is None:
        bullet.display()

        if player.coord[0] + 50 >= bullet.coord[0] and player.coord[0] <= bullet.coord[0] + 24 and player.coord[1] + 150 >= HEIGHT - bullet.coord[1] and player.coord[1] <= HEIGHT - bullet.coord[1] + 24:
            vie -= 1
            bullet = None

    if player.coord[0] + 50 >= lance_pos and player.coord[0] <= lance_pos + 64 and player.coord[1] + 150 >= HEIGHT -20 and player.coord[1] <= HEIGHT - 20 + 20:
        vie -= 1
        lance_pos += 100


    # Gestion de l'affichage
    screen.blit(font.render(f"Vie : {vie}", True, (255, 255, 255)), (WIDTH-120, 0))
    screen.blit(font.render(f"Score : {score}", True, (255, 255, 255)), (10, 0))

    time += 1
    if time % 100 == 0: score += 1

    if vie == 0: break

    pygame.display.flip()


# Gestion de la fin de partie
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(pygame.image.load("./src/sprites/death.png").convert(), (0, 0))
    screen.blit(font.render(f"Score : {score}", True, (255, 255, 255)), (10, 0))
    pygame.display.flip()

    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]: break

# Quitter Pygame
pygame.quit()