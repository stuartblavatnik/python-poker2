'''
Methods that operate on cards
'''

ranksTuple = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

def getCardDescription(cardNumber):
    rankDescription = getRankDescription(getRank(cardNumber))
    suitDescription = getSuitDescription(getSuit(cardNumber))

    return rankDescription + " of " + suitDescription

def getSingleCardDescription(cardNumber):
    return getRankDescription(getRank(cardNumber))

def getRank(cardNumber):
    return ranksTuple[cardNumber]

