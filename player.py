import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.velocity = 5
        self.jump = 15

        self.attack = 20

        self.down_right_sprites = []
        self.down_right_sprites.append(pygame.image.load('images/soldier_down_right/soldier_1.png'))
        self.down_right_sprites.append(pygame.image.load('images/soldier_down_right/soldier_4.png'))
        
        self.jump_right_sprites = [] 
        self.jump_right_sprites.append(pygame.image.load('images/soldier_down_right/soldier_1.png'))
        self.jump_right_sprites.append(pygame.image.load('images/soldier_jump_right/soldier_1.png'))
        self.jump_right_sprites.append(pygame.image.load('images/soldier_jump_right/soldier_2.png'))
        self.jump_right_sprites.append(pygame.image.load('images/soldier_jump_right/soldier_3.png'))

        self.run_right_sprites = [] 
        self.run_right_sprites.append(pygame.image.load('images/soldier_down_right/soldier_1.png'))
        self.run_right_sprites.append(pygame.image.load('images/soldier_run_right/soldier_1.png'))
        self.run_right_sprites.append(pygame.image.load('images/soldier_run_right/soldier_2.png'))
        self.run_right_sprites.append(pygame.image.load('images/soldier_run_right/soldier_3.png'))
        self.run_right_sprites.append(pygame.image.load('images/soldier_run_right/soldier_4.png'))
        self.run_right_sprites.append(pygame.image.load('images/soldier_run_right/soldier_5.png'))
        self.run_right_sprites.append(pygame.image.load('images/soldier_run_right/soldier_6.png'))

        self.shoot_right_sprites = []
        self.shoot_right_sprites.append(pygame.image.load('images/soldier_down_right/soldier_1.png'))
        self.shoot_right_sprites.append(pygame.image.load('images/soldier_shoot_right/soldier_1.png'))

        self.die_right_sprites = []

        self.down_left_sprites = []
        self.down_left_sprites.append(pygame.image.load('images/soldier_down_left/soldier_1.png'))
        self.down_left_sprites.append(pygame.image.load('images/soldier_down_left/soldier_4.png'))

        self.jump_left_sprites = []
        self.jump_left_sprites.append(pygame.image.load('images/soldier_down_left/soldier_1.png'))
        self.jump_left_sprites.append(pygame.image.load('images/soldier_down_left/soldier_1.png'))
        self.jump_left_sprites.append(pygame.image.load('images/soldier_jump_left/soldier_1.png'))
        self.jump_left_sprites.append(pygame.image.load('images/soldier_jump_left/soldier_2.png'))
        self.jump_left_sprites.append(pygame.image.load('images/soldier_jump_left/soldier_3.png'))

        self.run_left_sprites = []
        self.run_left_sprites.append(pygame.image.load('images/soldier_down_left/soldier_1.png'))
        self.run_left_sprites.append(pygame.image.load('images/soldier_run_left/soldier_1.png'))
        self.run_left_sprites.append(pygame.image.load('images/soldier_run_left/soldier_2.png'))
        self.run_left_sprites.append(pygame.image.load('images/soldier_run_left/soldier_3.png'))
        self.run_left_sprites.append(pygame.image.load('images/soldier_run_left/soldier_4.png'))
        self.run_left_sprites.append(pygame.image.load('images/soldier_run_left/soldier_5.png'))
        self.run_left_sprites.append(pygame.image.load('images/soldier_run_left/soldier_6.png'))

        self.shoot_left_sprites = []
        self.shoot_left_sprites.append(pygame.image.load('images/soldier_down_left/soldier_1.png'))
        self.shoot_left_sprites.append(pygame.image.load('images/soldier_shoot_left/soldier_1.png'))

        self.die_left_sprites = []

        self.current_sprite = 0
        self.image = self.down_right_sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image,(75,75))
        self.rect = self.image.get_rect()
        self.current_y = 200
        self.current_x = 100
        self.rect.x = self.current_x 
        self.rect.y = self.current_y

        self.is_jumping_right = False
        self.is_jumping_left = False
        self.is_getting_down_right = False
        self.is_getting_down_left = False
        self.is_shooting_right = False
        self.is_shooting_left = False
        self.is_dying = False
        self.is_running_right = False
        self.is_running_left = False

        self.is_right = True


        self.all_projectiles = pygame.sprite.Group()

    def animate(self, index):
        if index =='is_getting_down':
            if self.is_right == True:
                self.is_getting_down_right = True
            else:
                self.is_getting_down_left = True

        elif index =='is_jumping' :
            if self.is_right == True:
                self.is_jumping_right = True
            else:
                self.is_jumping_left =True

        elif index == 'is_shooting':
            if self.is_right == True :
                self.is_shooting_right = True
            else:
                self.is_shooting_left = True

        elif index == 'is_running':
            if self.is_right == True:
                self.is_running_right = True
            else:
                self.is_running_left = True

    def update(self, speed):
        #down_right :
        if self.is_getting_down_right == True:
            self.current_sprite +=speed
            if self.current_sprite >= len(self.down_right_sprites):
                self.current_sprite = 0
                self.is_getting_down_right = False

            self.image = self.down_right_sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image,(75,75))
            self.rect.x = self.current_x  
            self.rect.y = self.current_y

        #down_left :
        if self.is_getting_down_left == True:
            self.current_sprite +=speed
            if self.current_sprite >= len(self.down_left_sprites):
                self.current_sprite = 0
                self.is_getting_down_left = False

            self.image = self.down_left_sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image,(75,75))
            self.rect.x = self.current_x  
            self.rect.y = self.current_y

        #jump right :
        elif self.is_jumping_right == True:
            self.current_sprite +=speed
            if self.current_sprite >= len(self.jump_right_sprites):
                self.current_sprite = 0 
                self.is_jumping_right = False
                self.rect.y = self.current_y

            self.image = self.jump_right_sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image,(75,75)) 
            self.rect.x = self.current_x  
            self.rect.y -= self.velocity

        #jump left :
        elif self.is_jumping_left == True:
            self.current_sprite +=speed
            if self.current_sprite >= len(self.jump_left_sprites):
                self.current_sprite = 0 
                self.is_jumping_left = False
                self.rect.y = self.current_y

            self.image = self.jump_left_sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image,(75,75))
            self.rect.x = self.current_x  
            self.rect.y -= self.velocity

        #run right :
        elif self.is_running_right == True:
            self.current_sprite += speed+0.4
            if self.current_sprite >= len(self.run_right_sprites):
                self.current_sprite = 0
                self.is_running_right = False

            self.image = self.run_right_sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image,(75,75))
            self.rect.x = self.current_x  
            self.rect.y = self.current_y

        #run left :
        elif self.is_running_left == True:
            self.current_sprite += speed+0.4
            if self.current_sprite >= len(self.run_left_sprites):
                self.current_sprite = 0
                self.is_running_left = False

            self.image = self.run_left_sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image,(75,75))
            self.rect = self.image.get_rect()
            self.rect.x= self.current_x 
            self.rect.y = self.current_y

        #shoot right :
        elif self.is_shooting_right == True:
            self.current_sprite += speed
            if self.current_sprite >= len(self.shoot_right_sprites):
                self.current_sprite = 0
                self.is_shooting_right = False

            self.image = self.shoot_right_sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image,(75,75))
            self.rect = self.image.get_rect()
            self.rect.y = self.current_y
            self.rect.x= self.current_x 
            for projectile in self.all_projectiles:
                projectile.move_right()

        #shoot left :
        elif self.is_shooting_left == True:
            self.current_sprite += speed
            if self.current_sprite >= len(self.shoot_left_sprites):
                self.current_sprite = 0
                self.is_shooting_left = False

            self.image = self.shoot_left_sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image,(75,75))
            self.rect = self.image.get_rect()
            self.rect.x= self.current_x 
            self.rect.y = self.current_y

            for projectile in self.all_projectiles:
                projectile.move_left()

    def move_right(self):
        self.current_x  += self.velocity

    def move_left(self):
        self.current_x  -= self.velocity