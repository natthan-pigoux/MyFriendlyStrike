#!/usr/bin/python3.6
import pygame, sys
from game import Game
import math
pygame.init()

game = Game()

background = pygame.image.load('images/png/BG.png')
screen_width = background.get_width()
screen_height = background.get_height()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('friendly Strike')

background = pygame.image.load('images/png/BG.png')

clock = pygame.time.Clock()
running = True

while running:

    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
            quit()
    #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.animate('is_jumping')

            if event.key == pygame.K_t:
                game.launch_projectile()

            if event.key == pygame.K_LCTRL:
                game.player.animate('is_getting_down')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

    game.update(screen)
    pygame.display.flip()
    clock.tick(60)
