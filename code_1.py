import pygame, random
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800,900))
pygame.display.set_caption("STARSHIP")
clock = pygame.time.Clock()
start_font = pygame.font.Font(None,50)

pozadi_hvezdy = pygame.image.load('Ročníková_Práce/img/vesmir-hvezdy.jpg')
start_text = start_font.render('STARSHIP',False,'Blue')

hrac = pygame.image.load('Ročníková_Práce/img/lod.gif')
ship_x_pos = 375
ship_y_pos = 300


#Životy
HP = 3
HP1 = pygame.image.load('Ročníková_Práce/img/lod.gif')
HP2 = pygame.image.load('Ročníková_Práce/img/lod.gif')
HP3 = pygame.image.load('Ročníková_Práce/img/lod.gif')


enemyship = pygame.image.load('Ročníková_Práce/img/ufo.png')
enemyship_x_pos = random.randint(25, 775)
enemyship_y_pos = -50
enemyship2 = pygame.image.load('Ročníková_Práce/img/ufo.png')
enemyship_x_pos2 = enemyship_x_pos + 100
enemyship_y_pos2 = -50
enemyship3 = pygame.image.load('Ročníková_Práce/img/ufo.png')
enemyship_x_pos3 = enemyship_x_pos2 + 100
enemyship_y_pos3 = -50



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
            
    enemyship_y_pos += 1
    enemyship_y_pos2 += 1
    enemyship_y_pos3 += 1

    screen.blit(pozadi_hvezdy,(0,0))    
    screen.blit(start_text,(300,50))
    screen.blit(hrac,(ship_x_pos,ship_y_pos))
    screen.blit(enemyship,(enemyship_x_pos,enemyship_y_pos))
    screen.blit(enemyship2,(enemyship_x_pos2,enemyship_y_pos2))
    screen.blit(enemyship3,(enemyship_x_pos3,enemyship_y_pos3))
    screen.blit(HP1,(10,700))
    screen.blit(HP2,(50,700))
    screen.blit(HP3,(90,700))
    
    #Rychlost lodi
   
        
        
    #Strany pozice    
    if ship_x_pos <= -50:
        ship_x_pos = 800
    if ship_x_pos >= 850:
        ship_x_pos = 0
    if ship_y_pos <= -80:
        ship_y_pos = 400
    if ship_y_pos >= 480:
        ship_y_pos = -25
        
    #Enemy pozice
    if enemyship_y_pos == 400:
        enemyship_y_pos = -50
        enemyship_x_pos = random.randint(25,775)
        enemyship_y_pos2 = -50
        enemyship_x_pos2 = enemyship_x_pos + 100
        enemyship_y_pos3 = -50
        enemyship_x_pos3 = enemyship_x_pos2 + 100

    #Kolize 
    #if(ship_x_pos < (enemyship_x_pos + 80 ) or ship_x_pos > (enemyship_x_pos + 80)):
    #    text_konec = 
    #if(ship_y_pos < (enemyship_y_pos + 40) or ship_y_pos > (enemyship_y_pos + 40)):

    
    
    pygame.display.update()
    clock.tick(60)
