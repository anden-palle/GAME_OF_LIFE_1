import pygame 
import random
import time

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill([0,0,0])
SquareGroup = pygame.sprite.LayeredUpdates()

class Square(pygame.sprite.Sprite):
	
	def __init__(self, x, y, onEdge):
		
		super().__init__()
		
		self.size = 40 #size of square
		
		self.image = pygame.Surface([self.size, self.size]) #surface for the square
		self.rect = self.image.get_rect() #needed by pygame
		
		self.rect.centerx = x
		self.rect.centery = y
		
		self.onEdge = onEdge
		
		if self.onEdge == True:
			pygame.draw.rect(self.image,[0,0,0],[0,0,40,40],0)
		if self.onEdge == False:
			pygame.draw.rect(self.image,[0,255,0],[0,0,40,40],0)
			
		
	
		
		







x = 20
y = 20
onEdge = False

for col in range(10):
	x = 20
	for row in range(10):
		
		if x == 20 or x == 380:
			onEdge = True
		
		elif y == 20 or y == 380:
			onEdge = True
		
		else:
			onEdge = False
		
		square = Square(x, y, onEdge)
		SquareGroup.add(square)
		
		print("x", x)
		x = x + 40
	print("y", y)
	y = y + 40
	
	
	
SquareGroup.draw(screen)
pygame.display.flip()

while 1:
	for event in pygame.event.get():
     
		if event.type == pygame.QUIT:
			break 
		
				

screen = pygame.display.set_mode((screen_width,screen_height))

