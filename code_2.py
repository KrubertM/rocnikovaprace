import pygame, random
from sys import exit
from lod import Ship

pygame.init()
width = 800
height = 900

screen = pygame.display.set_mode((width, height))

player = Ship()
 
sprite_groupe = pygame.sprite.Group()
sprite_groupe.add(player)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
    
    
    
    sprite_groupe.update()
    sprite_groupe.draw(screen)
    pygame.display.update()
    clock.tick(60)