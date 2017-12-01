import pygame
import serial

import slider
#import port

######	Color Definitions	######
red = 	(255,0,0)
black = (0,0,0)
grey = 	(100,100,100)
lgrey=	(150,150,150)
green = (0,120,0)
white = (255,255,255)

gap = 10
width = 80

pygame.init()
pygame.font.init()

display_size = 1200, 460

screen = pygame.display.set_mode(display_size)

screen.fill(grey)

sliders = []

atten_values = [1,1,1,1,1,1,1,1,1,1,1,1,1]

for i in range(13):
	
	sliders.append(slider.slider((gap + i * (width + gap),50), (width,300)))
	
print(atten_values)
print(sliders)

for s in sliders:
	
	s.draw(screen)

running = 1;

while(running):

	event = pygame.event.poll()

	if event.type == pygame.QUIT:

		running = 0

	#elif event.type == pygame.MOUSEMOTION:
	elif pygame.mouse.get_pressed()[0]:
		print("mouse is at %d, %d " % pygame.mouse.get_pos())

		for s in sliders:

			s.set_value(pygame.mouse.get_pos())

			s.draw(screen)

			print(1 - s.get_value())

		for i in range(13):

			if atten_values[i] != 1 - sliders[i].get_value():

				#ser_write(sliders[i].get_value()) # WRITE VALUE OVER SERIAL
				print("SERIAL WRITE")

				atten_values[i] = 1 - sliders[i].get_value()

	pygame.display.flip()
