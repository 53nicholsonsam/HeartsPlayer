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
def takesecond(elem):
  return elem[2]
player1hand.sort(key= takesecond)
player2hand.sort(key=takesecond)
player3hand.sort(key=takesecond)
player4hand.sort(key=takesecond)
#print(player1hand)
print("Welcome to the Hearts simulator! Enter 'exit' to leave at any time")
# program while loop to play Hearts, type "exit" to exit
while True:
    print("Here is your hand: ")
    print(player1hand)
    print("Here is what was dealt: <insert card that was dealt>")
    userInput = input('Which card would you like to play? ')
    if userInput == "exit":
        break
    

