import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load("Ročníková_Práce/img/ufo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.speed = 5
        
        
    def update(self):
        self.rect.x += self.x
        self.rect.y += self.y