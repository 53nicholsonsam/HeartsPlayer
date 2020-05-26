import tkinter as tk
from PIL import Image, ImageTk

def determineCard(playedCards, currentTrick, cardLed, hand):
    """
    Determines a card to play based on the card led and the player's hand.
    Currently determines card to play according to the rules with some strategy.
    """
    suit = cardLed[2]
    cardsOfSuit = []
    # flags for if player has queen of spades or hearts. In the event that the player doesn't
    # have the suit led, it will be useful to know this information
    hasQueen = False
    hasHearts = False
    maxHeart = 0
    for card in hand:
        if card[2] == suit:
            cardsOfSuit.append(card)
        if card == "11s":
            hasQueen = True
        if card[2] == "h":
            hasHearts = True
            if int((card[0] + card[1])) > maxHeart:
                maxHeart = int((card[0] + card[1]))

    # player has no cards of the suit that was led
    if len(cardsOfSuit) == 0:
        # dump the queen if you have it!
        if hasQueen and cardLed != "01c":
            return "11s"
        # otherwise play highest heart in hand
        if hasHearts and cardLed != "01c":
            if maxHeart < 10:
                return "0" + str(maxHeart) + "h"
            else:
                return str(maxHeart) + "h"
        # if no hearts or queen, play highest remaining card
        maxCard = 0
        suit = ""
        for card in hand:
            if int((card[0] + card[1])) > maxCard:
                maxCard = int((card[0] + card[1]))
                suit = card[2]
        if maxCard < 10:
            return "0" + str(maxCard) + suit
        else:
            return str(maxCard) + suit
    else:
        # special case of spades led and someone else played ace or king
        if ("12s" in currentTrick or "13s" in currentTrick) and cardLed[2] == "s" and "11s" in hand:
            return "11s"
        wantToWin = True # should player try to win the trick or no?
        # if hearts or the queen have been played, don't try to win
        for card in currentTrick:
            if card[0] == "11s" or card[0][2] == "h":
                wantToWin = False
        # if queen is still out there, do not want to win in spades!
        if "11c" not in playedCards and cardLed[2] == "s":
            wantToWin = False
        # if you have the queen in spades, don't try to win!
        if "11c" in hand:
            wantToWin = False
        playedOfSuit = 0
        for card in playedCards:
            if card[2] == suit:
                playedOfSuit += 1
        # if someone didn't have the suit previously, or a lot have been played, don't want to win
        if ((playedOfSuit % 4) != 0 and playedOfSuit > 4) or playedOfSuit > 7:
            wantToWin = False
    
        # find max and min cards of suit
        maxCard = 0
        minCard = 15
        for card in cardsOfSuit:
            if int((card[0] + card[1])) > maxCard:
                maxCard = int((card[0] + card[1]))
            if int((card[0] + card[1])) < minCard:
                minCard = int((card[0] + card[1]))

        # play max card of suit if want to win, otherwise play the lowest
        if wantToWin:
            if maxCard < 10:
                return "0" + str(maxCard) + suit
            else:
                return str(maxCard) + suit
        else:
            if minCard < 10:
                return "0" + str(minCard) + suit
            else:
                return str(minCard) + suit

def determineLead(playedCards, hand):
    """
    Player won the previous trick, this function determines which card they 
    lead next. 
    Currently determined with a fair bit of strategy.
    """
    # if has the two of clubs, it's the first trick, so must lead it
    if "01c" in hand:
        return "01c"
    # have hearts been broken?
    broken = False
    # played cards from each suit so far
    playedH = []
    playedS = []
    playedC = []
    playedD = []
    for card in playedCards:
        if card[2] == "h":
            broken = True
            playedH.append(int((card[0] + card[1])))
        elif card[2] == "s":
            playedS.append(int((card[0] + card[1])))
        elif card[2] == "c":
            playedC.append(int((card[0] + card[1])))
        else:
            playedD.append(int((card[0] + card[1])))

    # player's highest and lowest cards of each suit
    highestH = 0
    lowestH = 15
    numberH = 0
    highestS = 0
    lowestS = 15
    numberS = 0
    highestC = 0
    lowestC = 15
    numberC = 0
    highestD = 0
    lowestD = 15
    numberD = 0
    for card in hand:
        if card[2] == "h":
            numberH += 1
            if int((card[0] + card[1])) > highestH:
                highestH = int((card[0] + card[1]))
            if int((card[0] + card[1])) < lowestH:
                lowestH = int((card[0] + card[1]))
        elif card[2] == "s":
            numberS += 1
            if int((card[0] + card[1])) > highestS:
                highestS = int((card[0] + card[1]))
            if int((card[0] + card[1])) < lowestS:
                lowestS = int((card[0] + card[1]))
        elif card[2] == "c":
            numberC += 1
            if int((card[0] + card[1])) > highestC:
                highestC = int((card[0] + card[1]))
            if int((card[0] + card[1])) < lowestC:
                lowestC = int((card[0] + card[1]))
        else:
            numberD += 1
            if int((card[0] + card[1])) > highestD:
                highestD = int((card[0] + card[1]))
            if int((card[0] + card[1])) < lowestD:
                lowestD = int((card[0] + card[1]))

    # hearts have been broken, lead one if a good low one is present
    if broken and numberH > 0:
        # calculate how many lower hearts remain
        lowerHearts = lowestH - 1
        for h in playedH:
            if h < lowestH:
                lowerHearts -= 1
        # if only 0 or 1 lower, always lead the heart
        if lowerHearts < 2:
            if lowestH < 10:
                return "0" + str(lowestH) + "h"
            else:
                return str(lowestH) + "h"
        # if 2 lower exist, only lead if only a few hearts have been played
        elif lowerHearts < 3 and len(playedH) < 5:
            if lowestH < 10:
                return "0" + str(lowestH) + "h"
            else:
                return str(lowestH) + "h"
    # next, try to lead a spade, if you don't have high ones!
    if numberS > 0 and highestS < 11:
        if highestS == 10:
            return str(highestS) + "s"
        else:
            return "0" + str(highestS) + "s"
    # next, try to lead either clubs or diamonds, depending on which you have less of
    elif numberC > 0 and (numberC < numberD or numberD == 0):
        # only lead highest one if exactly one full trick of them have been played
        if len(playedC) == 4:
            if(highestC > 9):
                return str(highestC) + "c"
            else:
                return "0" + str(highestC) + "c"
        else:
            if(lowestC > 9):
                return str(lowestC) + "c"
            else:
                return "0" + str(lowestC) + "c"
    elif numberD != 0:
        # only try to win if just a few have been played
        if len(playedD) < 5:
            if(highestD > 9): 
                return str(highestD) + "d"
            else:
                return "0" + str(highestD) + "d"
        else: 
            if(lowestD > 9):
                return str(lowestD) + "d"
            else:
                return "0" + str(lowestD) + "d"
    # play lowest heart if nothing else is left
    elif numberC == 0 and numberD == 0 and numberS == 0:
        if(lowestH > 9):
            return str(lowestH) + "h"
        else:
            return "0" + str(lowestH) + "h"
    # last scenario: must play highest spade
    else:
        if(highestS > 9):
            return str(highestS) + "s"
        else:
            return "0" + str(highestS) + "s"

def determineValidity(cardLed, card, hand):
    """
    Determine if the card the player tried to play is valid.
    """
    # ensure card is actually in hand
    inHand = False
    for c in hand:
        if card == c:
            inHand = True
    if inHand == False:
        return [False, "Card selected must be in hand. Please try again."]
    if cardLed == "01c" and (card[2] == "h" or card == "11s"):
        return [False, "Cannot play Queen of spades or a heart on the first trick."]
    if card[2] == cardLed[2]:
        return [True, ""]
    else: 
        for c in hand:
            if c[2] == cardLed[2]:
                return [False, "If you have a card of the suit led, you must play it."]
        return [True, ""]
    
def determineLeadValidity(playedCards, card, hand):
    """
    Given the cards that have been played so far, as well as the player's hand,
    determine whether the card they have attempted to lead is valid.
    """
    # must lead 2C if have it for first trick
    if "01c" in hand and card != "01c":
        return [False, "You must lead the 2 of clubs for the first trick."]
    # ensure card is actually in hand
    inHand = False
    for c in hand:
        if card == c:
            inHand = True
    if inHand == False:
        return [False, "Card selected must be in hand. Please try again."]
    # always okay to lead a non-Heart
    if card[2] != "h":
        return [True, ""]
    # otherwise, it must have either been broken, or the player has all hearts left
    else:
        for c in playedCards:
            if c[2] == "h":
                return [True, ""]
        for c in hand:
            if c[2] != "h":
                return [False, "Hearts have not yet been broken. Please lead a non-Heart."]
        return [True, ""]

def mapCardToImagePath(card):
    """
    Given a card, return the relative path to its image
    """
    if card == "01c":
        return 'src/imgs/2C.png'
    if card == "02c":
        return 'src/imgs/3C.png'
    if card == "03c":
        return 'src/imgs/4C.png'
    if card == "04c":
        return 'src/imgs/5C.png'
    if card == "05c":
        return 'src/imgs/6C.png'
    if card == "06c":
        return 'src/imgs/7C.png'
    if card == "07c":
        return 'src/imgs/8C.png'
    if card == "08c":
        return 'src/imgs/9C.png'
    if card == "09c":
        return 'src/imgs/10C.png'
    if card == "10c":
        return 'src/imgs/JC.png'
    if card == "11c":
        return 'src/imgs/QC.png'
    if card == "12c":
        return 'src/imgs/KC.png'
    if card == "13c":
        return 'src/imgs/AC.png'
    
    if card == "01d":
        return 'src/imgs/2D.png'
    if card == "02d":
        return 'src/imgs/3D.png'
    if card == "03d":
        return 'src/imgs/4D.png'
    if card == "04d":
        return 'src/imgs/5D.png'
    if card == "05d":
        return 'src/imgs/6D.png'
    if card == "06d":
        return 'src/imgs/7D.png'
    if card == "07d":
        return 'src/imgs/8D.png'
    if card == "08d":
        return 'src/imgs/9D.png'
    if card == "09d":
        return 'src/imgs/10D.png'
    if card == "10d":
        return 'src/imgs/JD.png'
    if card == "11d":
        return 'src/imgs/QD.png'
    if card == "12d":
        return 'src/imgs/KD.png'
    if card == "13d":
        return 'src/imgs/AD.png'

    if card == "01s":
        return 'src/imgs/2S.png'
    if card == "02s":
        return 'src/imgs/3S.png'
    if card == "03s":
        return 'src/imgs/4S.png'
    if card == "04s":
        return 'src/imgs/5S.png'
    if card == "05s":
        return 'src/imgs/6S.png'
    if card == "06s":
        return 'src/imgs/7S.png'
    if card == "07s":
        return 'src/imgs/8S.png'
    if card == "08s":
        return 'src/imgs/9S.png'
    if card == "09s":
        return 'src/imgs/10S.png'
    if card == "10s":
        return 'src/imgs/JS.png'
    if card == "11s":
        return 'src/imgs/QS.png'
    if card == "12s":
        return 'src/imgs/KS.png'
    if card == "13s":
        return 'src/imgs/AS.png'

    if card == "01h":
        return 'src/imgs/2H.png'
    if card == "02h":
        return 'src/imgs/3H.png'
    if card == "03h":
        return 'src/imgs/4H.png'
    if card == "04h":
        return 'src/imgs/5H.png'
    if card == "05h":
        return 'src/imgs/6H.png'
    if card == "06h":
        return 'src/imgs/7H.png'
    if card == "07h":
        return 'src/imgs/8H.png'
    if card == "08h":
        return 'src/imgs/9H.png'
    if card == "09h":
        return 'src/imgs/10H.png'
    if card == "10h":
        return 'src/imgs/JH.png'
    if card == "11h":
        return 'src/imgs/QH.png'
    if card == "12h":
        return 'src/imgs/KH.png'
    if card == "13h":
        return 'src/imgs/AH.png'
    else:
        return 'INVALID CARD'