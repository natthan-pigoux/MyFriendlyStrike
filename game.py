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
        self.player_1 = Player(self)
        self.player_2 = Player(self)
        self.player_2.rect.x = screen_width -200
        self.player_2.rect.y = screen_height -200

        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player_1)
        self.all_players.add(self.player_2)

        self.pressed = {}
        self.key_up = {}

    def start(self):
        None

    def game_over(self):
        self.is_playing = False

    def update(self, screen):
        self.manage_key()
        self.all_players.update()
        self.all_players.draw(screen)

        for player in self.all_players:
            player.all_projectiles.draw(screen)
            player.update_health_bar(screen)
            for projectile in player.all_projectiles:
                projectile.move()

    def manage_key(self):

        if self.pressed.get(pygame.K_RIGHT) and self.player_1.rect.x +self.player_1.rect.width< self.screen_width \
        and self.player_1.is_falling == False:
            self.player_1.is_right = True
            self.player_1.animate('is_running')
            self.player_1.move_right()

        elif self.pressed.get(pygame.K_LEFT) and self.player_1.rect.x >0 and self.player_1.is_falling == False:
            self.player_1.is_right = False
            self.player_1.animate('is_running')
            self.player_1.move_left()

        elif self.pressed.get(pygame.K_UP):
            self.player_1.move_up()

        elif self.pressed.get(pygame.K_DOWN):
            self.player_1.move_down()

        if self.pressed.get(pygame.K_z):
            self.player_2.move_up()

        elif self.pressed.get(pygame.K_s):
            self.player_2.move_down()

        elif self.pressed.get(pygame.K_q) and self.player_2.rect.x >0 and self.player_2.is_falling == False:
            self.player_2.is_right = False
            self.player_2.animate('is_running')
            self.player_2.move_left()

        elif self.pressed.get(pygame.K_d) and self.player_2.rect.x +self.player_2.rect.width< self.screen_width \
        and self.player_2.is_falling == False:
            self.player_2.is_right = True
            self.player_2.animate('is_running')
            self.player_2.move_right()

    def check_collision_group(self, sprite, group):

        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def check_collision_sprite(self, sprite1, sprite2):

        return pygame.sprite.collide_mask(sprite1, sprite2)