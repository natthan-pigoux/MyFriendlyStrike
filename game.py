import pygame
from player import Player
from projectile import Projectile
from map import Map

class Game:

    def __init__(self):
        self.is_playing = False
        self.player = Player(self)
        self.map = Map()
        self.projectile = Projectile(self.player, self.player.is_right)
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        self.pressed = {}
        self.key_up = {}

    def start(self):
        None

    def game_over(self):
        self.is_playing = False

    def update(self, screen):
        self.all_players.draw(screen)
        self.all_players.update(0.2)
        self.player.all_projectiles.draw(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x +self.player.rect.width< screen.get_width():
            self.player.is_right = True
            self.player.animate('is_running')
            self.player.move_right()

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x >0:
            self.player.is_right = False
            self.player.animate('is_running')
            self.player.move_left()


    def launch_projectile(self):
        self.projectile.number -=1
        if self.projectile.number > 0 :
            self.player.all_projectiles.add(Projectile(self.player,self.player.is_right))
            self.player.animate('is_shooting')

    def check_collision(self, sprite, group):

        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
