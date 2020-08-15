import pygame



class Cactus(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load('images/png/Objects/Cactus_1.png')
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def set_image(self, object):
        self.image = pygame.image.load('images/png/Objects/Cactus_1.png')

class Stone(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load('images/png/Objects/StoneBlock.png')
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Ladder(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load('images/ladders/ladder2.png')
        self.image = pygame.transform.scale(self.image, (100,450))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Map():

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.decor = []
        for i in range(0,self.screen_width,100):
            self.decor.append(Stone(i,self.screen_height-100))

        self.decor.append(Cactus(self.screen_width*0.62, self.screen_height-200))
        self.decor.append(Stone(self.screen_width*0, self.screen_height*0.5))
        self.decor.append(Stone(self.screen_width*0 + 100, self.screen_height*0.5))
        self.decor.append(Stone(self.screen_width*0.5, self.screen_height-100))
        self.map_sprite = pygame.sprite.Group()
        self.ladder_sprite = pygame.sprite.Group()
        self.ladder_sprite.add(Ladder(100, self.screen_height*0.5+ 50))
        self.create_map()

    def create_map(self):
        for i in self.decor:
            self.map_sprite.add(i)





