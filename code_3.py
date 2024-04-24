import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Space Invanders')

radek = 5
sloupec = 5
konec_hry = 0

bg = pygame.image.load("Ročníková_Práce/Space_invaders/img/bg.png")

def draw_bg():
	screen.blit(bg, (0, 0))
 
class HRAC(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("Ročníková_Práce/Space_invaders/img/spaceship.png")
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]