import pygame


# Colors ###################
red = 	(255,0,0)
black = (0,0,0)
grey = 	(100,100,100)
lgrey=	(150,150,150)
green = (0,120,0)
white = (255,255,255)

slider_width = 60

#pygame.font.init()

#print(pygame.font.get_fonts())


class slider:
	
	point = (0,0)

	size = 	(0,0)

	value = 0

	font = 0

	def __init__(self, point, size):
	
#		pygame.init()

		self.point = point

		self.size =  size

		self.value = 0

		self.font = pygame.font.SysFont('arial', 30)

	def set_value(self, point):

		ypoint = point[1]
		xpoint = point[0]

		if xpoint < self.point[0] or xpoint > self.point[0] + self.size[0]:
			
			return -1

		top = self.point[1] + 50

		bottom = self.point[1] - 50 + self.size[1]

		bottom = bottom - top

		ypoint = ypoint - top

		value = float(ypoint) / float(bottom)

		if (value > 1):

			self.value = 1

			return 0

		elif (value < 0):
			
			self.value = 0

			return 0

		self.value = value

		return 0

	def get_value(self):

		return self.value

	def draw(self, screen):

		pygame.draw.rect(screen, lgrey, (self.point[0],self.point[1],self.size[0],self.size[1]))

		line_center = self.point[0] + (self.size[0] / 2)

		pygame.draw.line(screen, black, (line_center, self.point[1] + 50), (line_center, self.point[1] - 50 + self.size[1]), 5)

#		pygame.draw.line(screen, black, (self.point[0], self.point[1] + 50), (self.point[0]+self.size[0], self.point[1] + 50), 1)

#		pygame.draw.line(screen, black, (self.point[0], self.point[1] - 50 + self.size[1]), (self.point[0]+self.size[0], self.point[1] - 50 + self.size[1]), 1)
		
		pygame.draw.rect(screen, grey, (line_center - slider_width/2, self.point[1] + 50 + (self.size[1]-100) * self.value - 25 , slider_width, 50))

		text = self.font.render("{0:.3f}".format(1-self.value), False, black)

		pygame.draw.rect(screen, white, (self.point[0], self.point[1] + 60 + self.size[1], self.size[0], 30))

		screen.blit(text, (self.point[0], self.point[1] + 60 + self.size[1]))




