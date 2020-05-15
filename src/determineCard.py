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
        if hasQueen:
            return "11s"
        # otherwise play highest heart in hand
        elif hasHearts:
            if maxHeart < 10:
                return "0" + str(maxHeart) + "h"
            else:
                return str(maxHeart) + "h"
        # if no hearts or queen, play highest remaining card
        else:
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
        wantToWin = True # should player try to win the trick or no?
        # if hearts or the queen have been played, don't try to win
        for card in currentTrick:
            if card[0] == "11s" or card[0][2] == "h":
                wantToWin = False
        playedOfSuit = 0
        for card in playedCards:
            if card[2] == suit:
                playedOfSuit += 1
        # if someone didn't have the suit previously, or a lot have been played, don't want to win
        if (playedOfSuit % 4) != 0 or playedOfSuit > 7:
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
    # have hearts been broken?
    broken = False
    # number of played cards from each suit so far
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

