import pygame  # using methods provided by the pygame module to achieve
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -20)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 20)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-20, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(20, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 0


# some constant defined
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# SURF_WIDTH = 50
# SURF_HEIGHT = 50

# initialize
pygame.init()

# first, set the screen
# pygame.display.set_mode((width,height))
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# second,set the caption of the screen
pygame.display.set_caption("RidingRoad EXCLUSIVE Music Player")

# create a surface with pygame.Surface() and pass in a tuple with its width and  height
# surf = pygame.Surface((SURF_WIDTH, SURF_HEIGHT))
# give the surface a color to differentiate from the background
# surf.fill((255, 255, 255))
# using the get_rect() to get the area of the rectangular surface and the x,y coordinates
# rect = surf.get_rect()  # <rect(0, 0, 50, 50)>
# this line says "draws the surf on the coordinates :center of the screen"
# blit:transfer something from one location to another
# screen.blit(surf, (SCREEN_WIDTH // 2 - SURF_WIDTH // 2,
#                    SCREEN_HEIGHT // 2 - SURF_HEIGHT // 2))
# pygame.display.flip()  # to refresh display


# create a Player object
player = Player()

# variable to keep our loop running
running = True

# main loop
while running:
    # for loop through the pygame.event.get()
    for event in pygame.event.get():
        # check for keydown event,KEYDOWN is a constant defined in pygame.locals
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    pressed_keys = pygame.key.get_pressed()
    player.update(pressed_keys)

    # draw the player on the screen
    screen.blit(player.surf, (500, 100))
    # screen.blit(player.surf, player.rect)
    # refresh the display
    pygame.display.flip()
