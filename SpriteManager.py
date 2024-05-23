import config
import pygame

class SpritesManager:
    def __init__(self, src: str, sprites: dict):
        self.src = "./src/sprites/" + src
        self.sprites = sprites

    def display(self, coord: tuple, sprite: str, reverse: bool = False):
        img = pygame.image.load(self.src).convert()
        img.set_colorkey((255,0,0))

        if not reverse:
            config.screen.blit(img, coord, self.sprites[sprite])
        else:
            decalage = 78 if sprite in ["stay","walk1", "walk2"] else 102
            config.screen.blit(pygame.transform.flip(img, True, False), coord, (img.get_size()[0]-self.sprites[sprite][0]- decalage, self.sprites[sprite][1], self.sprites[sprite][2], self.sprites[sprite][3]))


#factor = 4
PLAYER = SpritesManager(
    "player/player.png",
    {
        "stay":  (0,            0,  78, 150),
        "walk1": (78+1,         0,  78, 150),
        "walk2": (78 * 2 + 1,   0,  78, 150),
        "jump":  ((78 * 3 + 1), 0,  102, 150)
    }
)

BACKGROUND = SpritesManager(
    "scenes/background.png",
    {
        "background": (0, 0, 1664, 1419)
    }
)

BULLETS = SpritesManager(
    "objects/bullets.png",
    {
        "bullet":       (0,    0,      24, 24),
        "fired_bullet": (24+1, 0,      24, 24)
    }
)

CANNON = SpritesManager(
    "objects/cannon.png",
    {
        "default": (0, 0, 192, 192)
    }
)

LANCE = SpritesManager(
    "objects/lance.png",
    {
        "default": (0, 0, 64, 20)
    }
)