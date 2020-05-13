def determineCard(cardLed, hand):
    """
    Determines a card to play based on the card led and the player's hand.
    Currently determines card to play according to the rules, but somewhat randomly.
    """
    suit = cardLed[2]
    cardsOfSuit = []
    for card in hand:
        if card[2] == suit:
            cardsOfSuit.append(card)
    if len(cardsOfSuit) == 0:
        return hand[0]
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


    