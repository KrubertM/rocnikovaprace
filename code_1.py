import pygame

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background = pygame.image.load("pozadi.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

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

level = 1

line_enemy_max = 6

level_1_enemy_count = 12
level_2_enemy_count = 18
level_3_enemy_count = 24

level_1_enemy_list = []
level_2_enemy_list = []
level_3_enemy_list = []
bullets = []

enemy = pygame.image.load("img/ufo.png")
enemy_width = enemy.get_width()
enemy_height = enemy.get_height()
enemy = pygame.transform.scale(enemy, (enemy_width/2, enemy_height/2))
enemy_width = enemy.get_width()
enemy_height = enemy.get_height()
enemy_speed = 0.5

def create_bullet(x, y):
    return pygame.Rect(x, y, 5, 10)

def create_enemy(x, y):
    return pygame.Rect(x, y, enemy_width, enemy_height)


margin_x = 40
margin_y = 20

x_pos_enemy = margin_x
y_pos_enemy = margin_y

for x in range(int(level_1_enemy_count/line_enemy_max)):

    for y in range(line_enemy_max):
        enemy_obj = create_enemy(x_pos_enemy, y_pos_enemy)
        level_1_enemy_list.append(enemy_obj)
        x_pos_enemy += 50

    y_pos_enemy += 50
    x_pos_enemy = margin_x

x_pos_enemy = margin_x
y_pos_enemy = margin_y

for x in range(int(level_2_enemy_count/line_enemy_max)):
    
    for y in range(line_enemy_max):
        enemy_obj = create_enemy(x_pos_enemy, y_pos_enemy)
        level_2_enemy_list.append(enemy_obj)
        x_pos_enemy += 50
        
    y_pos_enemy += 50
    x_pos_enemy = margin_x
    
x_pos_enemy = margin_x
y_pos_enemy = margin_y

for x in range(int(level_3_enemy_count/line_enemy_max)):
    
    for y in range(line_enemy_max):
        enemy_obj = create_enemy(x_pos_enemy, y_pos_enemy)
        level_3_enemy_list.append(enemy_obj)
        x_pos_enemy += 50

    y_pos_enemy += 50
    x_pos_enemy = margin_x


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(create_bullet(player_x + 27.5, player_y))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_x -= SPEED
    if keys[pygame.K_d]:
        player_x += SPEED
        
    screen.blit(background, (0, 0))
    
    current_enemies = []
    if level == 1:
        current_enemies = level_1_enemy_list
    elif level == 2:
        current_enemies = level_2_enemy_list
    elif level == 3:
        current_enemies = level_3_enemy_list

    for enemy_rect in current_enemies:
        enemy_rect.y += enemy_speed
        
        if enemy_rect.y + enemy_height >= player_y:
            run = False
            break

    for bullet in bullets[:]:
        bullet.y -= 10
        if bullet.y < 0:
            bullets.remove(bullet)

    for bullet in bullets[:]:
        for enemy_rect in current_enemies[:]:
            if bullet.colliderect(enemy_rect):
                current_enemies.remove(enemy_rect)
                bullets.remove(bullet)
                break 

    
    if player_x >= SCREEN_WIDTH - 60:
        player_x = SCREEN_WIDTH - 60
    if player_x <= 0:
        player_x = 0

    if current_enemies == []:
        level += 1
        enemy_speed += 0.5

    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 255), bullet)

    for enemy_obj in current_enemies: 
        screen.blit(enemy, (enemy_obj.x, enemy_obj.y))

    screen.blit(player, (player_x, player_y))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

