import pygame



class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):

        super().__init__()
        self.player = player
        self.velocity = 25
        self.number = 30
        self.image = pygame.image.load('images/bullet.png')
        self.image = pygame.transform.scale(self.image,(10,10)) 
        self.rect = self.image.get_rect()
        self.rect.x = self.player.rect.x + 20
        self.rect.y = self.player.rect.y + 20


    def remove(self):
        self.player.all_projectiles.remove(self)

    def move_left(self):
        self.image = pygame.transform.rotate(self.image,270)
        self.rect.x -= self.velocity
        if self.rect.x < -10:
            self.remove()

    def move_right(self):
        self.image = pygame.transform.rotate(self.image,90)
        self.rect.x += self.velocity

        if self.rect.x > 450:
            self.remove()
            