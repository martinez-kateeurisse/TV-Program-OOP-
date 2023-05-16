#Kate Eurisse L. Martinez_BSCPE 1-5_Test Driver program

#Import class file
from Television import TV

#call methods for tv1
tv1 = TV()
#Turning tv1 on
tv1.tv_on()
#Setting channel for tv1
tv1.set_channel(30)
#Settng volume for tv1
tv1.set_volume(3)

#Print output for tv 1
tv1 = print("tv1's channel is " + tv1.get_channel(), "and volume level is " +  tv1.get_volume())

#Call methods for tv2
tv2 = TV()
#Turing tv2 on
tv2.tv_on()
#Setting channel for tv2
tv2.set_channel(3)
#Setting volume for tv2
tv2.set_volume(2)

#Print output for tv 2
tv2 = print("tv2's channel is " + tv2.get_channel(), "and volume level is " +  tv2.get_volume())

#Displaying output through pygame
#Import modules 
import pygame
import sys

#Initialize variables
pygame.init
#Initialize window display format(dimension)
window_width = 550
window_height = 350
display = pygame.display.set_mode((window_width,window_height))

#Set text formats(font and color), position and background
output_font = pygame.font.Font("Gameshow.otf", 30)
output_text = output_font.render(tv1, tv2, True, (250,250,250))
text_rect = output_text.get_rect()
text_rect.center = (window_width//2, window_height//2)
background = pygame.image.load("background.jpg")

#Run the program in pygame
#Use a loop to run the program
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    display.fill((0,0,0))
    display.blit(background, (0,0))
    display.blit(output_text, text_rect)
    pygame.display.update()


#The output of the program will be displayed in the pygame window