import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.velocity = 10
        self.jump_height = 50

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
        self.size = 120
        self.image = self.down_right_sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image,(self.size, self.size))
        self.rect = self.image.get_rect()
        self.current_x = self.game.screen_width*0 + 50
        self.current_y = self.game.screen_height*0.5 - 200
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
        self.is_falling = False

        self.is_right = True

        #corriger les projectiles
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

    def update(self):
        speed = 0.3
        self.get_down(speed)

        self.jump(speed)

        self.shoot(speed)

        self.fall(speed)
        
        self.run(speed)

    def fall(self, speed):
        if not self.game.check_collision(self, self.game.map_sprite) and self.is_jumping_left == False and self.is_jumping_right == False:
            if self.current_y < self.game.screen_height -100:
                self.is_falling = True
                self.current_y +=speed*20
                self.image = self.down_right_sprites[0]
                self.image = pygame.transform.scale(self.image,(self.size,self.size))
                self.rect = self.image.get_rect()
                self.rect.y = self.current_y
                self.rect.x= self.current_x 
            else:
                self.is_falling = False
        else:
            self.is_falling = False

    def shoot(self,speed):
        #shoot right :
        if self.is_shooting_right == True:
            self.current_sprite += speed
            if self.current_sprite >= len(self.shoot_right_sprites):
                self.current_sprite = 0
                self.is_shooting_right = False

            self.image = self.shoot_right_sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image,(self.size,self.size))
            self.rect = self.image.get_rect()
            self.rect.y = self.current_y
            self.rect.x= self.current_x 

        #shoot left :
        elif self.is_shooting_left == True:
            self.current_sprite += speed
            if self.current_sprite >= len(self.shoot_left_sprites):
                self.current_sprite = 0
                self.is_shooting_left = False

            self.image = self.shoot_left_sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image,(self.size,self.size))
            self.rect = self.image.get_rect()
            self.rect.x= self.current_x 
            self.rect.y = self.current_y

        for projectile in self.all_projectiles:
            projectile.move()

    def get_down(self,speed):
        #down_right : 
        if self.is_getting_down_right == True:
            self.current_sprite +=speed
            if self.current_sprite >= len(self.down_right_sprites):
                self.current_sprite = 0
                self.is_getting_down_right = False

            self.image = self.down_right_sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image,(self.size,self.size))
            self.rect.x = self.current_x  
            self.rect.y = self.current_y

        #down_left :
        elif self.is_getting_down_left == True:
            self.current_sprite +=speed
            if self.current_sprite >= len(self.down_left_sprites):
                self.current_sprite = 0
                self.is_getting_down_left = False

            self.image = self.down_left_sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image,(self.size,self.size))
            self.rect.x = self.current_x  
            self.rect.y = self.current_y

    def jump(self,speed):

        #jump right :
        if self.is_jumping_right == True:
            self.current_sprite +=speed
            if self.current_sprite >= len(self.jump_right_sprites):
                self.current_sprite = 0 
                self.is_jumping_right = False
                self.rect.y = self.current_y

            self.image = self.jump_right_sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image,(self.size,self.size)) 
            self.current_x += self.velocity 
            self.rect.x = self.current_x 
            self.rect.y -= self.jump_height/3

        #jump left :
        elif self.is_jumping_left == True:
            self.current_sprite +=speed
            if self.current_sprite >= len(self.jump_left_sprites):
                self.current_sprite = 0 
                self.is_jumping_left = False
                self.rect.y = self.current_y

            self.image = self.jump_left_sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image,(self.size,self.size))
            self.current_x -= self.velocity 
            self.rect.x = self.current_x  
            self.rect.y -= self.jump_height/3

    def run(self,speed):
            #run right :
        if self.is_running_right == True:
            self.current_sprite += speed+0.4
            if self.current_sprite >= len(self.run_right_sprites):
                self.current_sprite = 0
                self.is_running_right = False

            self.image = self.run_right_sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image,(self.size,self.size))
            self.rect.x = self.current_x  
            self.rect.y = self.current_y

        #run left :
        elif self.is_running_left == True:
            self.current_sprite += speed+0.4
            if self.current_sprite >= len(self.run_left_sprites):
                self.current_sprite = 0
                self.is_running_left = False

            self.image = self.run_left_sprites[int(self.current_sprite)]
            self.image = pygame.transform.scale(self.image,(self.size,self.size))
            self.rect = self.image.get_rect()
            self.rect.x= self.current_x 
            self.rect.y = self.current_y


    def move_right(self):
        self.current_x  += self.velocity

    def move_left(self):
        self.current_x  -= self.velocity
