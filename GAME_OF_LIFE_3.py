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
		
		self.rect.centerx = x #needed by pygame to det position of the Square
		self.rect.centery = y #needed by pygame to det position of the Square
		
		self.onEdge = onEdge #íf on theEdge
		
		#set color based on position
		if self.onEdge == True:
			pygame.draw.rect(self.image,[0,0,0],[0,0,40,40],0)
		if self.onEdge == False:
			pygame.draw.rect(self.image,[0,255,0],[0,0,40,40],0)
			
		
	
		
		






#sets x and y start position
x = size / 2
y = size / 2
onEdge = False

#createa all the Square classes
#every Square at the egde get ignored to make the project a little easyer
#a Square on the edge is found by its x and y position

for col in range(int(screen_width / size - 1)): #the number of Squares is based on how many time the size goes up minus one
	x = size / 2
	for row in range(int(screen_height / size - 1)):
		
		if x == size / 2 or x == screen_width - size: #checks if a Square is on the edge based on position
			onEdge = True
		
		elif y == size / 2 or y == screen_height - size: #checks if a Square is on the edge based on position
			onEdge = True
		
		else:
			onEdge = False
		
		square = Square(x, y, onEdge, size) #creates the Squares
		SquareGroup.add(square)
		
		print("x", x) #print the live x position
		x = x + size #change x position for every col
	print("y", y) #print the live y position
	y = y + size #change the y position for every row
	
	
	
SquareGroup.draw(screen) #draws every Square to screen
pygame.display.flip() #updates the screen

#mainloop
while 1:
	
	for event in pygame.event.get():
     
		if event.type == pygame.QUIT:
			break 
		
				



