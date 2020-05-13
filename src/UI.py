#Creating a UI with pygame.
import pygame
cardidentifier={}
SUITS = ["h","d","s","c"]
SUITSCAPS=["H","D","S","C"]
CARDNum=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
# To make life a little easier, I am setting ace high to value of 13 and down from there, so a 2 is actually a 1 in this system
NUMBERS = list(range(1,14))
deck=[]
deckforimg=[]
for item in SUITS:
    for num in NUMBERS:
      deck.append(str(num).zfill(2)+item) # Creating the cards here
for item in SUITSCAPS:
    for num in CARDNum:
        deckforimg.append(num+item)
for i in range(0,len(deck)):
    cardidentifier[deck[i]]=deckforimg[i]
print(cardidentifier)
pygame.init()

# define the RGB value 
# for white colour 
white = (255, 255, 255) 
  
# assigning values to X and Y variable 
X = 50
Y = 50
  
# create the display surface object 
# of specific dimension..e(X, Y). 
display_surface = pygame.display.set_mode((X, Y )) 
display_width = 800
display_height = 600
# set the pygame window name 
pygame.display.set_caption('Image')
image = pygame.image.load('src/imgs/2C.png').convert()
image=pygame.transform.rotozoom(image, 0, .5)
x = 20 # x coordnate of image
y = 30 # y coordinate of image

 
running = True
while (running): # loop listening for end of game
    screen = pygame.display.set_mode((display_width, display_height ))
    screen.blit(image, ( x,y)) # paint to screen
    pygame.display.flip() # paint screen one time
    pygame.time.wait(3000)
    running=False
#loop over, quit pygame
pygame.quit()