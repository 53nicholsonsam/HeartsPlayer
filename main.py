### Creating a script that plays hearts with itself with the hopes of further expansion
import random

### Dealing ###
SUITS = ["h","d","s","c"]
# To make life a little easier, I am setting ace high to value of 13 and down from there, so a 2 is actually a 1 in this system
NUMBERS = list(range(1,14))
deck=[]
for item in SUITS:
  for num in NUMBERS:
    deck.append(str(num).zfill(2)+item) # Creating the cards here

indexDeck = list(range(1,53)) # Need to index the deck so that we can deal it
tempToDict=[] 
for i in range(0,len(indexDeck)): #Sew up the index and the card so that we can deal
  tempList=[]
  tempList.append(indexDeck[i])
  tempList.append(deck[i])
  tempToDict.append(tempList)
deckWithIndex=dict(tempToDict) #this is our indexed deck

shuffleIndex=list(range(1,53)) #creating our shuffling index
random.shuffle(shuffleIndex)

handSize=int(len(shuffleIndex)/4) #dividing up our shuffle so we can deal the cards
handSize2=int(handSize*2)
handSize3=int(handSize*3)
handSize4=int(handSize*4)
Player1deal=shuffleIndex[:handSize]
Player2deal=shuffleIndex[handSize:handSize2]
Player3deal=shuffleIndex[handSize2:handSize3]
Player4deal=shuffleIndex[handSize3:handSize4]

player1hand=[]
player2hand=[]
player3hand=[]
player4hand=[]
for ii in range(0,len(Player1deal)):  #This is the actual dealing
  player1hand.append(deckWithIndex[Player1deal[ii]])
  player2hand.append(deckWithIndex[Player2deal[ii]])
  player3hand.append(deckWithIndex[Player3deal[ii]])
  player4hand.append(deckWithIndex[Player4deal[ii]])

#Players now each have a hand of 13 cards
###Sorting the hands
player1handsorted=[] #where the sorted hands will ultimately go
player1clubs=[] #getting ready to separate out the cards by suit
player1spades=[]
player1hearts=[]
player1diamonds=[]
for item in player1hand: #going through the hand
  while item[2] == "c": #separating by suit
    player1clubs.append(item)
    break
  while item[2] == "s":
    player1spades.append(item)
    break
  while item[2] == "h":
    player1hearts.append(item)
    break
  while item[2] == "d":
    player1diamonds.append(item)
    break
player1clubs.sort() #sort each suit
player1spades.sort()
player1hearts.sort()
player1diamonds.sort()
for item in player1clubs: #put the sorted suits back into the sorted hand
  player1handsorted.append(item)
for item in player1spades:
  player1handsorted.append(item)
for item in player1diamonds:
  player1handsorted.append(item)
for item in player1hearts:
  player1handsorted.append(item)
player2handsorted=[] #repeat procedure for the other players.
player2clubs=[]
player2spades=[]
player2hearts=[]
player2diamonds=[]
for item in player2hand:
  while item[2] == "c":
    player2clubs.append(item)
    break
  while item[2] == "s":
    player2spades.append(item)
    break
  while item[2] == "h":
    player2hearts.append(item)
    break
  while item[2] == "d":
    player2diamonds.append(item)
    break
player2clubs.sort()
player2spades.sort()
player2hearts.sort()
player2diamonds.sort()
for item in player2clubs:
  player2handsorted.append(item)
for item in player2spades:
  player2handsorted.append(item)
for item in player2diamonds:
  player2handsorted.append(item)
for item in player2hearts:
  player2handsorted.append(item)
player3handsorted=[]
player3clubs=[]
player3spades=[]
player3hearts=[]
player3diamonds=[]
for item in player3hand:
  while item[2] == "c":
    player3clubs.append(item)
    break
  while item[2] == "s":
    player3spades.append(item)
    break
  while item[2] == "h":
    player3hearts.append(item)
    break
  while item[2] == "d":
    player3diamonds.append(item)
    break
player3clubs.sort()
player3spades.sort()
player3hearts.sort()
player3diamonds.sort()
for item in player3clubs:
  player3handsorted.append(item)
for item in player3spades:
  player3handsorted.append(item)
for item in player3diamonds:
  player3handsorted.append(item)
for item in player3hearts:
  player3handsorted.append(item)
player4handsorted=[]
player4clubs=[]
player4spades=[]
player4hearts=[]
player4diamonds=[]
for item in player4hand:
  while item[2] == "c":
    player4clubs.append(item)
    break
  while item[2] == "s":
    player4spades.append(item)
    break
  while item[2] == "h":
    player4hearts.append(item)
    break
  while item[2] == "d":
    player4diamonds.append(item)
    break
player4clubs.sort()
player4spades.sort()
player4hearts.sort()
player4diamonds.sort()
for item in player4clubs:
  player4handsorted.append(item)
for item in player4spades:
  player4handsorted.append(item)
for item in player4diamonds:
  player4handsorted.append(item)
for item in player4hearts:
  player4handsorted.append(item)
handssorted=[player1handsorted,player2handsorted,player3handsorted,player4handsorted] #putting all the hands together to itterate through below
clubssorted=[player1clubs,player2clubs,player3clubs,player4clubs]
spadessorted=[player1spades,player2spades,player3spades,player4spades]
heartssorted=[player1hearts,player2hearts,player3hearts,player4hearts]
diamondssorted=[player1diamonds,player2diamonds,player3diamonds,player4diamonds]
print(player1handsorted)
print(player2handsorted)
print(player3handsorted)
print(player4handsorted)
###Playing the hand###
player1tricks=[]
player2tricks=[]
player3tricks=[]
player4tricks=[]
played=[]
playersplayed=[]
##First Trick##
for hand in handssorted:
  for card in hand:
    if card == "01c":
      played.append(card)
      hand.pop(hand.index(card))
      playersplayed.append(handssorted.index(hand))
for hand in clubssorted:
  if clubssorted.index(hand) != playersplayed[0]:
    played.append(hand[len(hand)-1])
    hand.pop(len(hand)-1)
print(played)







#print(player1hand)
print("Welcome to the Hearts simulator! Enter 'exit' to leave at any time")
# program while loop to play Hearts, type "exit" to exit
#while True:
#    print("Here is your hand: ")
#    print(player1hand)
#    print("Here is what was dealt: <insert card that was dealt>")
#    userInput = input('Which card would you like to play? ')
#    if userInput == "exit":
#        break
    

