import pygame
import random

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("GALAGA")
player = pygame.image.load("img/ship.png")
player = pygame.transform.scale(player, (60, 60))
clock = pygame.time.Clock()
run = True
player_x = screen.get_width() // 2 - 30
player_y = screen.get_height() - 100
player_rect = pygame.Rect(player_x, player_y, 60, 60)
SPEED = 5
SCORE = 0
bullets = []

def create_bullet(x, y):
    return pygame.Rect(x, y, 5, 10)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(create_bullet(player_x + 27.5, player_y))

    screen.fill((255, 255, 255))
    
    #pohyb
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= SPEED
    if keys[pygame.K_d]:
        player_x += SPEED

    #okraje
    if player_x >= SCREEN_WIDTH - 60:
        player_x = SCREEN_WIDTH - 60
    if player_x <= 0:
        player_x = 0

    # strileni
    for bullet in bullets[:]:
        bullet.y -= 10
        if bullet.y < 0:
            bullets.remove(bullet)
    for bullet in bullets:
        pygame.draw.rect(screen, (0, 0, 0), bullet)


    screen.blit(player, (player_x, player_y))
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
