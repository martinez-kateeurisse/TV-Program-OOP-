#Kate Eurisse L. Martinez_BSCPE 1-5_Test Driver program

#Import class file
from Television import TV

#Call methods for tv1
tv1 = TV()
#Turning tv1 on
tv1.tv_on()
#Setting channel for tv1
tv1.set_channel(30)
#Settng volume for tv1
tv1.set_volume(3)

#Call methods for tv2
tv2 = TV()
#Turing tv2 on
tv2.tv_on()
#Setting channel for tv2
tv2.set_channel(3)
#Setting volume for tv2
tv2.set_volume(2)

#Displaying output through pygame

#Import modules 
import pygame
from pygame.locals import *
import sys

#Initialize variables
pygame.init
pygame.font.init()

#Initialize window display format(dimension)
window_width = 550
window_height = 320
display = pygame.display.set_mode((window_width,window_height))

#Run the program in pygame
#Use a loop to run the program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    #Set text formats(font and color), position and background
    output_font = pygame.font.Font("awesome.ttf", 30)
    text_rect_tv1 = output_font.render("", True, (250,250,250)).get_rect()
    text_rect_tv2 = output_font.render("", True, (250,250,250)).get_rect()       
    background = pygame.image.load("background.jpg")  
      
    #Render text surfaces with the current values (text outputs)
    output_tv1 = output_font.render("tv1's channel is " + str(tv1.get_channel()) + " and volume level is " +  str(tv1.get_volume()), True, (250,250,250))
    output_tv2 = output_font.render("tv2's channel is " + str(tv2.get_channel()) + " and volume level is " +  str(tv2.get_volume()), True, (250,250,250))
    
    # Calculate centered positions
    text_rect_tv1.center = (window_width // 2, window_height // 2)
    text_rect_tv2.center = (window_width // 2, window_height // 2 + output_tv1.get_height() + 20)

    # Adjust the positions based on the width and height of the text surfaces
    text_rect_tv1.x -= output_tv1.get_width() // 2
    text_rect_tv1.y -= output_tv1.get_height() // 2
    text_rect_tv2.x -= output_tv2.get_width() // 2
    text_rect_tv2.y -= output_tv2.get_height() // 2
   
    #Update display 
    display.fill((0,0,0))
    display.blit(background, (0,0))
    display.blit(output_tv1, text_rect_tv1)
    display.blit(output_tv2, text_rect_tv2)
    pygame.display.update()

#The output of the program will be displayed in the pygame window