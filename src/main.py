### Creating a script that plays hearts with itself with the hopes of further expansion
import random
from determineCard import determineCard, determineLead, determineValidity

print("Welcome to the Hearts simulator! Enter 'exit' to leave at any time")

# user is player 1
player1points = 0
player2points = 0
player3points = 0
player4points = 0
handCount = 0

while player1points < 100 and player2points < 100 and player3points < 100 and player4points < 100:
  handCount += 1
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

  # cards that each player has won
  player1tricks=[]
  player2tricks=[]
  player3tricks=[]
  player4tricks=[]

  # all cards that have been played so far
  playedCards = []

  currentTrick = []

  # determine who should lead first trick
  for card in player1hand:
    if card == "01c":
      playedCards.append(card)
      currentTrick.append([card, 1])
      player1hand.remove(card)
      print("You were dealt the 2 of clubs. It has been automatically led for you.")
      card2 = determineCard(playedCards, currentTrick, card, player2hand)
      player2hand.remove(card2)
      playedCards.append(card2)
      currentTrick.append([card2, 2])
      card3 = determineCard(playedCards, currentTrick, card, player3hand)
      player3hand.remove(card3)
      playedCards.append(card3)
      currentTrick.append([card3, 3])
      card4 = determineCard(playedCards, currentTrick, card, player4hand)
      player4hand.remove(card4)
      playedCards.append(card4)
      currentTrick.append([card4, 4])
  for card in player2hand:
    if card == "01c":
      playedCards.append(card)
      currentTrick.append([card, 2])
      player2hand.remove(card)
      card3 = determineCard(playedCards, currentTrick, card, player3hand)
      player3hand.remove(card3)
      playedCards.append(card3)
      currentTrick.append([card3, 3])
      card4 = determineCard(playedCards, currentTrick, card, player4hand)
      player4hand.remove(card4)
      playedCards.append(card4)
      currentTrick.append([card4, 4])
      print("Here are the cards that have been played so far this trick: ")
      print(currentTrick)
      print("Here is your hand: ")
      print(player1hand)
      valid = False
      while valid == False:
        card1 = input("Which card would you like to play? Enter it like this: '04c' for 5 of clubs, '10d' for Jack of diamonds: ")
        valid = determineValidity("01c", card1, player1hand)
      player1hand.remove(card1)
      playedCards.append(card1)
      currentTrick.append([card1, 1])
  for card in player3hand:
    if card == "01c":
      playedCards.append(card)
      currentTrick.append([card, 3])
      player3hand.remove(card)
      card4 = determineCard(playedCards, currentTrick, card, player4hand)
      player4hand.remove(card4)
      playedCards.append(card4)
      currentTrick.append([card4, 4])
      print("Here are the cards that have been played so far this trick: ")
      print(currentTrick)
      print("Here is your hand: ")
      print(player1hand)
      valid = False
      while valid == False:
        card1 = input("Which card would you like to play? Enter it like this: '04c' for 5 of clubs, '10d' for Jack of diamonds: ")
        valid = determineValidity("01c", card1, player1hand)
      player1hand.remove(card1)
      playedCards.append(card1)
      currentTrick.append([card1, 1])
      card2 = determineCard(playedCards, currentTrick, card, player2hand)
      player2hand.remove(card2)
      playedCards.append(card2)
      currentTrick.append([card2, 2])
  for card in player4hand:
    if card == "01c":
      playedCards.append(card)
      currentTrick.append([card, 4])
      player4hand.remove(card)
      print("Here are the cards that have been played so far this trick: ")
      print(currentTrick)
      print("Here is your hand: ")
      print(player1hand)
      valid = False
      while valid == False:
        card1 = input("Which card would you like to play? Enter it like this: '04c' for 5 of clubs, '10d' for Jack of diamonds: ")
        valid = determineValidity("01c", card1, player1hand)
      player1hand.remove(card1)
      playedCards.append(card1)
      currentTrick.append([card1, 1])
      card2 = determineCard(playedCards, currentTrick, card, player2hand)
      player2hand.remove(card2)
      playedCards.append(card2)
      currentTrick.append([card2, 2])
      card3 = determineCard(playedCards, currentTrick, card, player3hand)
      player3hand.remove(card3)
      playedCards.append(card3)
      currentTrick.append([card3, 3])

  # determine who won the current trick
  highest = 0
  lead = 0
  for card in currentTrick:
    c = card[0]
    p = card[1]
    if c[2] == "c":
      if int((c[0] + c[1])) > highest:
        highest = int((c[0] + c[1]))
        lead = p

  if lead == 1:
    for card in currentTrick:
      player1tricks.append(card[0])
  elif lead == 2:
    for card in currentTrick:
      player2tricks.append(card[0])
  elif lead == 3:
    for card in currentTrick:
      player3tricks.append(card[0])
  else:
    for card in currentTrick:
      player4tricks.append(card[0])

  currentTrick = []

  while len(playedCards) < 52:
    if lead == 1:
      leadCard = determineLead(playedCards, player1hand)
      card2 = determineCard(playedCards, currentTrick, leadCard, player2hand)
      card3 = determineCard(playedCards, currentTrick, leadCard, player3hand)
      card4 = determineCard(playedCards, currentTrick, leadCard, player4hand)
      currentTrick.append([leadCard, 1])
      currentTrick.append([card2, 2])
      currentTrick.append([card3, 3])
      currentTrick.append([card4, 4])
      playedCards.append(leadCard)
      playedCards.append(card2)
      playedCards.append(card3)
      playedCards.append(card4)
      player1hand.remove(leadCard)
      player2hand.remove(card2)
      player3hand.remove(card3)
      player4hand.remove(card4)
    elif lead == 2:
      leadCard = determineLead(playedCards, player2hand)
      card3 = determineCard(playedCards, currentTrick, leadCard, player3hand)
      card4 = determineCard(playedCards, currentTrick, leadCard, player4hand)
      card1 = determineCard(playedCards, currentTrick, leadCard, player1hand)
      currentTrick.append([leadCard, 2])
      currentTrick.append([card3, 3])
      currentTrick.append([card4, 4])
      currentTrick.append([card1, 1])
      playedCards.append(leadCard)
      playedCards.append(card3)
      playedCards.append(card4)
      playedCards.append(card1)
      player2hand.remove(leadCard)
      player3hand.remove(card3)
      player4hand.remove(card4)
      player1hand.remove(card1)
    elif lead == 3:
      leadCard = determineLead(playedCards, player3hand)
      card4 = determineCard(playedCards, currentTrick, leadCard, player4hand)
      card1 = determineCard(playedCards, currentTrick, leadCard, player1hand)
      card2 = determineCard(playedCards, currentTrick, leadCard, player2hand)
      currentTrick.append([leadCard, 3])
      currentTrick.append([card4, 4])
      currentTrick.append([card1, 1])
      currentTrick.append([card2, 2])
      playedCards.append(leadCard)
      playedCards.append(card4)
      playedCards.append(card1)
      playedCards.append(card2)
      player3hand.remove(leadCard)
      player4hand.remove(card4)
      player1hand.remove(card1)
      player2hand.remove(card2)
    else:
      leadCard = determineLead(playedCards, player4hand)
      card1 = determineCard(playedCards, currentTrick, leadCard, player1hand)
      card2 = determineCard(playedCards, currentTrick, leadCard, player2hand)
      card3 = determineCard(playedCards, currentTrick, leadCard, player3hand)
      currentTrick.append([leadCard, 4])
      currentTrick.append([card1, 1])
      currentTrick.append([card2, 2])
      currentTrick.append([card3, 3])
      playedCards.append(leadCard)
      playedCards.append(card1)
      playedCards.append(card2)
      playedCards.append(card3)
      player4hand.remove(leadCard)
      player1hand.remove(card1)
      player2hand.remove(card2)
      player3hand.remove(card3)

    suit = leadCard[2]
    highest = int((leadCard[0] + leadCard[1]))
    for card in currentTrick:
      c = card[0]
      p = card[1]
      if c[2] == suit:
        if int((c[0] + c[1])) > highest:
          lead = p
          highest = int((c[0] + c[1]))
    
    if lead == 1:
      for card in currentTrick:
        player1tricks.append(card[0])
    elif lead == 2:
      for card in currentTrick:
        player2tricks.append(card[0])
    elif lead == 3:
      for card in currentTrick:
        player3tricks.append(card[0])
    else:
      for card in currentTrick:
        player4tricks.append(card[0])

    currentTrick = []

  for card in player1tricks:
    if card[2] == "h":
      player1points += 1
    if card == "11s":
      player1points += 13
  for card in player2tricks:
    if card[2] == "h":
      player2points += 1
    if card == "11s":
      player2points += 13
  for card in player3tricks:
    if card[2] == "h":
      player3points += 1
    if card == "11s":
      player3points += 13
  for card in player4tricks:
    if card[2] == "h":
      player4points += 1
    if card == "11s":
      player4points += 13

  print("HAND: " + str(handCount))
  print(player1points)
  print(player2points)
  print(player3points)
  print(player4points)
    

