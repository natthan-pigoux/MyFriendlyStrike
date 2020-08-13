import pygame
from player import Player
from projectile import Projectile


class Game:

    def __init__(self,map_sprite, ladder_sprite, screen_width, screen_height):
        self.map_sprite = map_sprite
        self.ladder_sprite = ladder_sprite
        self.screen_height = screen_height
        self.screen_width = screen_width

        self.is_playing = False
        self.player = Player(self)
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

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x +self.player.rect.width< screen.get_width() and self.player.is_falling == False:
            self.player.is_right = True
            self.player.animate('is_running')
            self.player.move_right()

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x >0 and self.player.is_falling == False:
            self.player.is_right = False
            self.player.animate('is_running')
            self.player.move_left()

        elif self.pressed.get(pygame.K_UP):
            self.player.move_up()

        elif self.pressed.get(pygame.K_DOWN):
            self.player.move_down()

        self.all_players.update()
        self.all_players.draw(screen)
        self.player.all_projectiles.draw(screen)

    def launch_projectile(self):
        self.projectile.number -=1
        if self.projectile.number > 0 :
            self.player.all_projectiles.add(Projectile(self.player,self.player.is_right))
            self.player.animate('is_shooting')

    def check_collision(self, sprite, group):

        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
