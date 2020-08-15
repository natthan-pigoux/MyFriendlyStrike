#!/usr/bin/python3.6
import pygame, sys
from game import Game
from map import Map
import math
pygame.init()



background = pygame.image.load('images/png/BG.png')
screen_width = background.get_width()
screen_height = background.get_height()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('friendly Strike')

background = pygame.image.load('images/png/BG.png')


this_map = Map(screen_width, screen_height) 

map_sprite = this_map.map_sprite
ladder_sprite = this_map.ladder_sprite
game = Game(map_sprite, ladder_sprite, screen_width, screen_height)

clock = pygame.time.Clock()
running = True

def key_manager():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
            quit()
    #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_RCTRL:
                game.player_1.animate('is_jumping')

            if event.key == pygame.K_RETURN:
                game.player_1.launch_projectile()

            if event.key == pygame.K_RSHIFT:
                game.player_1.animate('is_getting_down')

            if event.key == pygame.K_SPACE:
                game.player_2.animate('is_jumping')

            if event.key == pygame.K_t:
                game.player_2.launch_projectile()

            if event.key == pygame.K_LCTRL:
                game.player_2.animate('is_getting_down')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

while running:

    screen.blit(background, (0, 0))
    key_manager()

    map_sprite.draw(screen)
    ladder_sprite.draw(screen)
    game.update(screen)
    pygame.display.flip()
    clock.tick(60)
