import pygame 
import random
import time

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill([0,0,0])
SquareGroup = pygame.sprite.LayeredUpdates()
size = 40

class Square(pygame.sprite.Sprite):
	
	def __init__(self, x, y, onEdge, size):
		
		super().__init__()
		
		self.size = size #size of square
		
		self.image = pygame.Surface([self.size, self.size]) #surface for the square
		self.rect = self.image.get_rect() #needed by pygame
		
		self.rect.centerx = x
		self.rect.centery = y
		
		self.onEdge = onEdge
		
		if self.onEdge == True:
			pygame.draw.rect(self.image,[0,0,0],[0,0,40,40],0)
		if self.onEdge == False:
			pygame.draw.rect(self.image,[0,255,0],[0,0,40,40],0)
			
		
	
		
		







x = size / 2
y = size / 2
onEdge = False

for col in range(int(screen_width / size - 1)):
	x = size / 2
	for row in range(int(screen_height / size - 1)):
		
		if x == size / 2 or x == screen_width - size:
			onEdge = True
		
		elif y == size / 2 or y == screen_height - size:
			onEdge = True
		
		else:
			onEdge = False
		
		square = Square(x, y, onEdge, size)
		SquareGroup.add(square)
		
		print("x", x)
		x = x + size
	print("y", y)
	y = y + size
	
	
	
SquareGroup.draw(screen)
pygame.display.flip()

while 1:
	for event in pygame.event.get():
     
		if event.type == pygame.QUIT:
			break 
		
				

screen = pygame.display.set_mode((screen_width,screen_height))

