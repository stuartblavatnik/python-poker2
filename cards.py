'''
Methods that operate on cards
'''

import math

ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
pluralRanks = ("Twos", "Threes", "Fours", "Fives", "Sixes", "Sevens", "Eights", "Nines", "Tens", "Jacks", "Queens", "Kings", "Aces")
suits = ("Clubs", "Diamonds", "Hearts", "Spades")

def getCardDescription(cardNumber):
    rankDescription = getRankDescription(getRank(cardNumber))
    suitDescription = getSuitDescription(getSuit(cardNumber))

    return rankDescription + " of " + suitDescription

def getSingleCardDescription(cardNumber):
    return getRankDescription(getRank(cardNumber))

def getRank(cardNumber):
#return intval(floor(cardNumber / NUMBER_OF_SUITS))
    return math.floor(cardNumber / 4)

def getRankDescription(cardNumber):
    return ranks[cardNumber]

def getSuitDescription(cardNumber):
    return suits[cardNumber]

def getPluralRankDescription(cardNumber):
    return pluralRanks[cardNumber]

def getSuit(cardNumber):
    return cardNumber % 4


