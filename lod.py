import pygame

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.image = pygame.image.load("Ročníková_Práce/img/ship.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.x = 350
        self.y = 700
        self.speed = 5
        
        
    def update(self):
        self.rect.x += self.x
        self.rect.y += self.y
