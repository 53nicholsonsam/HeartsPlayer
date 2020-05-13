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