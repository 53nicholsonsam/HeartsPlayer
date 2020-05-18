### Creating a script that plays hearts with itself with the hopes of further expansion
import random
from determineCard import determineCard, determineLead, determineValidity, determineLeadValidity, mapCardToImagePath
import tkinter as tk
from tkinter.ttk import *
from PIL import Image, ImageTk
from functools import partial

valid = False
tempCard = ""

def on_click(cardLed, playedCards, card, hand):
  global valid
  global tempCard
  # when player has the lead
  if cardLed == "":
    valid = determineLeadValidity(playedCards, card, hand)
    tempCard = card
  # for non-leads
  else:
    valid = determineValidity(cardLed, card, hand)
    tempCard = card

def start_game():
  global valid
  global tempCard
  # user is player 1
  player1points = 0
  player2points = 0
  player3points = 0
  player4points = 0
  handCount = 0

  for child in root.winfo_children():
    child.destroy()

  frame = Frame(root)
  frame.grid(row = 1)

  globalFrame = Frame(root)
  globalFrame.grid(row = 0)

  while player1points < 100 and player2points < 100 and player3points < 100 and player4points < 100:
    myPointsLabel = Label(globalFrame, text = "Your points: " + str(player1points))
    myPointsLabel.grid(row = 0, columnspan = 5)
    player2pointsLabel = Label(globalFrame, text = "Player 2 points: " + str(player2points))
    player2pointsLabel.grid(row = 1, columnspan = 5)
    player3pointsLabel = Label(globalFrame, text = "Player 3 points: " + str(player3points))
    player3pointsLabel.grid(row = 2, columnspan = 5)
    player4pointsLabel = Label(globalFrame, text = "Player 4 points: " + str(player4points))
    player4pointsLabel.grid(row = 3, columnspan = 5)
    root.update()

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

    # sort player1's hand
    hearts = []
    spades = []
    diamonds = []
    clubs = []
    for card in player1hand:
      if card[2] == "h":
        hearts.append(card)
      elif card[2] == "s":
        spades.append(card)
      elif card[2] == "d":
        diamonds.append(card)
      else:
        clubs.append(card)
    hearts.sort()
    spades.sort()
    diamonds.sort()
    clubs.sort()
    sortedHand = []
    for card in hearts:
      sortedHand.append(card)
    for card in spades:
      sortedHand.append(card)
    for card in diamonds:
      sortedHand.append(card)
    for card in clubs:
      sortedHand.append(card)
    player1hand = sortedHand

    # cards that each player has won
    player1tricks=[]
    player2tricks=[]
    player3tricks=[]
    player4tricks=[]

    # all cards that have been played so far
    playedCards = []
    # cards played in current trick
    currentTrick = []

    # determine who should lead first trick
    for card in player1hand:
      if card == "01c":
        lead = 1
    for card in player2hand:
      if card == "01c":
        lead = 2
    for card in player3hand:
      if card == "01c":
        lead = 3
    for card in player4hand:
      if card == "01c":
        lead = 4

    items = []

    # while loop for current hand
    while len(playedCards) < 52:
      if lead == 1:
        playMessage = Label(frame, text = "You have the lead! Click on the card you'd like to play: ")
        playMessage.grid(row = 1, columnspan = 5)
        items.append(playMessage)
        root.update()

        while valid == False:
          num = 0
          imageList = []
          for card in player1hand:
            path = mapCardToImagePath(card)
            imageList.append(ImageTk.PhotoImage(Image.open(path).resize((80, 120))))

          for img in imageList:
            btn = Button(frame, image = img, command = partial(on_click, "", playedCards, player1hand[num], player1hand))
            btn.image = img
            btn.grid(row = 2, column = num)
            items.append(btn)

            num += 1
          root.update()

        currentTrick.append([tempCard, 1])
        playedCards.append(tempCard)
        player1hand.remove(tempCard)
        leadCard = tempCard
        tempCard = ""
        valid = False

        card2 = determineCard(playedCards, currentTrick, leadCard, player2hand)
        currentTrick.append([card2, 2])
        playedCards.append(card2)
        player2hand.remove(card2)
        card3 = determineCard(playedCards, currentTrick, leadCard, player3hand)
        currentTrick.append([card3, 3])
        playedCards.append(card3)
        player3hand.remove(card3)
        card4 = determineCard(playedCards, currentTrick, leadCard, player4hand)
        currentTrick.append([card4, 4])
        playedCards.append(card4)
        player4hand.remove(card4)
      elif lead == 2:
        leadCard = determineLead(playedCards, player2hand)
        currentTrick.append([leadCard, 2])
        playedCards.append(leadCard)
        player2hand.remove(leadCard)
        card3 = determineCard(playedCards, currentTrick, leadCard, player3hand)
        currentTrick.append([card3, 3])
        playedCards.append(card3)
        player3hand.remove(card3)
        card4 = determineCard(playedCards, currentTrick, leadCard, player4hand)
        currentTrick.append([card4, 4])
        playedCards.append(card4)
        player4hand.remove(card4)

        trickMessage = Label(frame, text = "Here are the cards that have been played so far this trick: ")
        trickMessage.grid(row = 1, columnspan = 5)
        items.append(trickMessage)

        imageList = []
        for card in currentTrick:
          path = mapCardToImagePath(card[0])
          imageList.append(ImageTk.PhotoImage(Image.open(path).resize((80, 120))))

        num = 0
        for img in imageList:
          btn = Button(frame, image = img)
          btn.image = img
          btn.grid(row = 2, column = num)
          items.append(btn)
          num += 1

        playMessage = Label(frame, text = "Here is your hand. Click on the card you'd like to play: ")
        playMessage.grid(row = 3, columnspan = 5)
        items.append(playMessage)
        root.update()

        while valid == False:
          num = 0
          imageList = []
          for card in player1hand:
            path = mapCardToImagePath(card)
            imageList.append(ImageTk.PhotoImage(Image.open(path).resize((80, 120))))

          for img in imageList:
            btn = Button(frame, image = img, command = partial(on_click, leadCard, "", player1hand[num], player1hand))
            btn.image = img
            btn.grid(row = 4, column = num)
            items.append(btn)

            num += 1
          root.update()

        currentTrick.append([tempCard, 1])
        playedCards.append(tempCard)
        player1hand.remove(tempCard)
        tempCard = ""
        valid = False

      elif lead == 3:
        leadCard = determineLead(playedCards, player3hand)
        currentTrick.append([leadCard, 3])
        playedCards.append(leadCard)
        player3hand.remove(leadCard)
        card4 = determineCard(playedCards, currentTrick, leadCard, player4hand)
        currentTrick.append([card4, 4])
        playedCards.append(card4)
        player4hand.remove(card4)

        trickMessage = Label(frame, text = "Here are the cards that have been played so far this trick: ")
        trickMessage.grid(row = 1, columnspan = 5)
        items.append(trickMessage)

        imageList = []
        for card in currentTrick:
          path = mapCardToImagePath(card[0])
          imageList.append(ImageTk.PhotoImage(Image.open(path).resize((80, 120))))

        num = 0
        for img in imageList:
          btn = Button(frame, image = img)
          btn.image = img
          btn.grid(row = 2, column = num)
          items.append(btn)
          num += 1

        playMessage = Label(frame, text = "Here is your hand. Click on the card you'd like to play: ")
        playMessage.grid(row = 3, columnspan = 5)
        items.append(playMessage)
        root.update()

        while valid == False:
          num = 0
          imageList = []
          for card in player1hand:
            path = mapCardToImagePath(card)
            imageList.append(ImageTk.PhotoImage(Image.open(path).resize((80, 120))))

          for img in imageList:
            btn = Button(frame, image = img, command = partial(on_click, leadCard, "", player1hand[num], player1hand))
            btn.image = img
            btn.grid(row = 4, column = num)
            items.append(btn)

            num += 1
          root.update()

        currentTrick.append([tempCard, 1])
        playedCards.append(tempCard)
        player1hand.remove(tempCard)
        tempCard = ""
        valid = False

        card2 = determineCard(playedCards, currentTrick, leadCard, player2hand)
        currentTrick.append([card2, 2])
        playedCards.append(card2)
        player2hand.remove(card2)
      else:
        leadCard = determineLead(playedCards, player4hand)
        currentTrick.append([leadCard, 4])
        playedCards.append(leadCard)
        player4hand.remove(leadCard)

        trickMessage = Label(frame, text = "Here are the cards that have been played so far this trick: ")
        trickMessage.grid(row = 1, columnspan = 5)
        items.append(trickMessage)

        imageList = []
        for card in currentTrick:
          path = mapCardToImagePath(card[0])
          imageList.append(ImageTk.PhotoImage(Image.open(path).resize((80, 120))))

        num = 0
        for img in imageList:
          btn = Button(frame, image = img)
          btn.image = img
          btn.grid(row = 2, column = num)
          items.append(btn)
          num += 1

        playMessage = Label(frame, text = "Here is your hand. Click on the card you'd like to play: ")
        playMessage.grid(row = 3, columnspan = 5)
        items.append(playMessage)
        root.update()

        while valid == False:
          num = 0
          imageList = []
          for card in player1hand:
            path = mapCardToImagePath(card)
            imageList.append(ImageTk.PhotoImage(Image.open(path).resize((80, 120))))

          for img in imageList:
            btn = Button(frame, image = img, command = partial(on_click, leadCard, "", player1hand[num], player1hand))
            btn.image = img
            btn.grid(row = 4, column = num)
            items.append(btn)

            num += 1
            root.update()

        currentTrick.append([tempCard, 1])
        playedCards.append(tempCard)
        player1hand.remove(tempCard)
        tempCard = ""
        valid = False

        card2 = determineCard(playedCards, currentTrick, leadCard, player2hand)
        currentTrick.append([card2, 2])
        playedCards.append(card2)
        player2hand.remove(card2)
        card3 = determineCard(playedCards, currentTrick, leadCard, player3hand)
        currentTrick.append([card3, 3])
        playedCards.append(card3)
        player3hand.remove(card3)

      suit = leadCard[2]
      highest = int((leadCard[0] + leadCard[1]))
      points = 0
      for card in currentTrick:
        c = card[0]
        p = card[1]
        if c[2] == suit:
          if int((c[0] + c[1])) > highest:
            lead = p
            highest = int((c[0] + c[1]))
        if c == "11s":
          points += 13
        if c[2] == "h":
          points += 1
      
      if lead == 1:
        for card in currentTrick:
          player1tricks.append(card[0])
        print("You won the trick! " + str(points) + " points added. " )
        pointsUpdate = Label(globalFrame, text = "You won the trick! " + str(points) + " points added. " )
        pointsUpdate.grid(row = 4, columnspan = 5)
      elif lead == 2:
        for card in currentTrick:
          player2tricks.append(card[0])
        print("Player 2 won the trick! " + str(points) + " points added. " )
        pointsUpdate = Label(globalFrame, text = "Player 2 won the trick! " + str(points) + " points added. " )
        pointsUpdate.grid(row = 4, columnspan = 5)
      elif lead == 3:
        for card in currentTrick:
          player3tricks.append(card[0])
        print("Player 3 won the trick! " + str(points) + " points added. " )
        pointsUpdate = Label(globalFrame, text = "Player 3 won the trick! " + str(points) + " points added. " )
        pointsUpdate.grid(row = 4, columnspan = 5)
      else:
        for card in currentTrick:
          player4tricks.append(card[0])
        print("Player 4 won the trick! " + str(points) + " points added. " )
        pointsUpdate = Label(globalFrame, text = "Player 4 won the trick! " + str(points) + " points added. " )
        pointsUpdate.grid(row = 4, columnspan = 5)

      currentTrick = []
      frame.destroy()
      frame = Frame(root)
      frame.grid()
      root.update()

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

root = tk.Tk()
root.geometry("1200x600")

title = Label(root, text = "Welcome to the Hearts simulator!")
title.grid(row = 0, columnspan = 3, sticky='W')
start = Button(root, text = "start!", command = start_game)
start.grid(row = 1, columnspan = 2)

root.mainloop()
