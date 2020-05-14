def determineCard(cardLed, hand):
    """
    Determines a card to play based on the card led and the player's hand.
    Currently determines card to play according to the rules, but somewhat randomly.
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
        return cardsOfSuit[0]
    

def determineLead(hand):
    """
    Player won the previous trick, this function determines which card they 
    lead next. 
    Currently determined somewhat randomly.
    """
    nonHearts = []
    for card in hand:
        if card[2] != "h":
            nonHearts.append(card)
    if len(nonHearts) == 0:
        return hand[0]
    else:
        return nonHearts[0]


    