import pygame
import sys 

pygame.init()

size = width, height = 1024, 768
speed = [-5,5]
 


screen = pygame.display.set_mode(size)
pygame.display.set_caption ("FishC Demo")
bg = (0,0,0)
font = pygame.font.Font(None, 30)

line_height = font.get_linesize()

yposition = 0
screen.fill(bg)

while True:
    
    for event in pygame.event.get():
         
        if event.type == pygame.QUIT:
            sys.exit()

        screen.blit(font.render(str(event), True, (0,255,0)), (0,yposition))
        yposition += line_height

        if yposition > height:
            yposition = 0
            screen.fill(bg)


    pygame.display.flip()
