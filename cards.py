'''
Methods that operate on cards.  The deck is made up of values from 0-51 with the individual index of the card used to
describe it's rank and suit.

Rank is defined as index / 4

Examples:

    cardIndex = 3
    3/4 = 0
    ranks[0]  =    "Two"

    cardIndex = 50
    50/4 = 12
    ranks[12]  =   "Ace"

Suit is defined as index % 4   -- The arbitrary order of suits is Clubs, Diamonds, Hearts and Spades

'''
import math

'''
Descriptions of the cards.
'''
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")

'''
Plural descriptions of the cards.
'''
pluralRanks = (
"Twos", "Threes", "Fours", "Fives", "Sixes", "Sevens", "Eights", "Nines", "Tens", "Jacks", "Queens", "Kings", "Aces")

'''
Description of suits
'''
suits = ("Clubs", "Diamonds", "Hearts", "Spades")


def getCardDescription(cardNumber):
    rankDescription = getRankDescription(getRank(cardNumber))
    suitDescription = getSuitDescription(getSuit(cardNumber))

    return rankDescription + " of " + suitDescription


def getSingleCardDescription(cardNumber):
    return getRankDescription(getRank(cardNumber))


def getRank(cardNumber):
    return math.floor(cardNumber / 4)


def getRankDescription(cardNumber):
    return ranks[cardNumber]


def getSuitDescription(cardNumber):
    return suits[cardNumber]


def getPluralRankDescription(cardNumber):
    return pluralRanks[cardNumber]


def getSuit(cardNumber):
    return cardNumber % 4
