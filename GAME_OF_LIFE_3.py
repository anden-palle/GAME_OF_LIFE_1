import pygame 
import random
import time

#initialize the screen
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))
screen.fill([0,0,0])
board = []
number = 0


#initialize Squaregroup
SquareGroup = pygame.sprite.LayeredUpdates() #Squaregroup is the group the Squares are in

size = 10 #size of Square

#Creates the board all the Squares refer to
#for a in range(int(screen_width / size - 1)):
	#for b in range(int(screen_height / size - 1)):
		#board[a].append(0)

#Square class
class Square(pygame.sprite.Sprite):
	
	def __init__(self, x, y, onEdge, size, number):
		
		super().__init__()
		
		self.number = number
		
		self.condition = "Alive"
		
		self.onEdge = onEdge #íf on theEdge
		
		if self.onEdge == True:
			self.condiition = 0
		
		if self.onEdge == False:
			self.condition = 1
		
		self.size = size #size of square
		
		self.image = pygame.Surface([self.size, self.size]) #surface for the square
		self.rect = self.image.get_rect() #needed by pygame
		
		self.rect.centerx = x #needed by pygame to set position of the Square
		self.rect.centery = y #needed by pygame to set position of the Square
		
		
		
		#set color based on position
		if self.condition == 1:
			pygame.draw.rect(self.image,[0,255,0],[0,0,40,40],0)
		
		if self.condition == 0:
			pygame.draw.rect(self.image,[0,0,0],[0,0,40,40],0)
			
		#def update():
			
			
		def return_dead_or_alive(number_to_answer):
			
			if number_to_answer == self.number:
				return self.condition
			
	
		
		


#sets x and y start position
x = size / 2
y = size / 2
onEdge = False

#creates all the Squares
#every Square at the egde get ignored to make the project a little easyer
#a Square on the edge is found by its x and y position

for col in range(int(screen_width / size - 1)): #the number of Squares is based on how many time the size goes up minus one
	x = size / 2
	for row in range(int(screen_height / size - 1)):
		
		
		#if Square is on the edge
		if x == size / 2 or x == screen_width - size: #checks if a Square is on the edge based on position
			onEdge = True
			print(onEdge)
		elif y == size / 2 or y == screen_height - size: #checks if a Square is on the edge based on position
			onEdge = True
			print(onEdge)
		
		else:
			onEdge = False
		
		#creates the Squares
		square = Square(x, y, onEdge, size, number) 
		SquareGroup.add(square)
		
		#updates the Square number
		number =+ 1
		
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
		
				



