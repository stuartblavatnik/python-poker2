import cards
from collections import Counter
from collections import namedtuple

HIGH_CARD = 0
PAIR = 1
TWO_PAIR = 2
THREE_OF_A_KIND = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
FOUR_OF_A_KIND = 7
STRAIGHT_FLUSH = 8

HIGH_CARD_DESC = ""
PAIR_DESC = "Pair of "
TWO_PAIR_DESC = "Two pairs "
THREE_OF_A_KIND_DESC = "Three "
STRIGHT_DESC = " Straight"
FLUSH_DESC = " Flush"
FULL_HOUSE_DESC = "Full house "
FOUR_OF_A_KIND_DESC = "Four "
STRAIGHT_FLUSH_DESC = " Straight flush"


class Hands:

    cards = []
    type = ""
    threeOfAKind = None
    fourOfAKind = None
    pairs = []



    def __init__(self, cards):
        self.cards = cards
        self.type = self.parse()

#    def compare(self, other):

    def __buildMultiples(self, ranks):

        multiple = False
        rankKeys = Counter(ranks).keys()
        rankValues = list(Counter(ranks).values())
        self.pairs = []

        arrayCount = len(rankKeys)

        for i in range(0, arrayCount):
            if (rankValues[i] > 1):
                multiple = True
                if (rankValues[i] == 2):
                    self.pairs.append(list(rankKeys)[i])
                elif (rankValues[i] == 3):
                    self.threeOfAKind = list(rankKeys)[i]
                elif (rankValues[i] == 4):
                    self.fourOfAKind = list(rankKeys)[i]
        return multiple

    def parse(self):

        HandDescription = namedtuple('HandDescription', 'description extraDescription extra')

        multiple = False

        self.cards.sort()
        highCard = self.cards[-1]
        highCardDescription = cards.getSingleCardDescription(highCard) + " " + "High"

        #Build arrays to hold suits and ranks
        suits = []
        ranks = []

        for card in self.cards:
            suits.append(cards.getSuit(card))
            ranks.append(cards.getRank(card))

        if len(suits) == 1:
            flush = True
            flushType = suits[0]
        else :
            multiple = self.__buildMultiples(ranks)

        if not multiple :
            '''
            Check for Straight -- Since the hand is sorted and we know that there
                                are no duplicates then the difference of the low
                                to the high card would be 4 -- for the case of 5
                                card hands
            '''

            if cards[4] - cards[0] == 4:
                straight = True

            if straight == True and flush == True:
                HandDescription.description = STRAIGHT_FLUSH
                HandDescription.extraDescription = highCardDescription
                HandDescription.extra = highCard
            elif flush is not None:
                HandDescription.description = FLUSH
                HandDescription.extraDescription = highCardDescription
                HandDescription.extra = highCard
            elif straight == True:
                HandDescription.description = STRAIGHT
                HandDescription.extraDescription = highCardDescription
                HandDescription.extra = highCard
            else:
                HandDescription.description = HIGH_CARD
                HandDescription.extraDescription = highCardDescription
                HandDescription.extra = highCard

        elif self.fourOfAKind is not None:
            HandDescription.description = FOUR_OF_A_KIND
            HandDescription.extraDescription = cards.getPluralRankDescription(self.fourOfAKind)
            HandDescription.extra = self.fourOfAKind
        elif self.threeOfAKind is not None and len(self.pairs) == 1:
            HandDescription.description = FULL_HOUSE
            HandDescription.extraDescription = cards.getPluralRankDescription(self.threeOfAKind) + " over " + \
                                               cards.getPluralRankDescription(self.pairs[0])
            HandDescription.extra = self.threeOfAKind
        elif self.threeOfAKind is not None:
            HandDescription.description = THREE_OF_A_KIND
            HandDescription.extraDescription = cards.getPluralRankDescription(self.threeOfAKind)
            HandDescription.extra = self.threeOfAKind
        elif self.pairs is not None and len(self.pairs) == 2:
            self.pairs.sort()
            HandDescription.description = TWO_PAIR
            HandDescription.extraDescription = cards.getPluralRankDescription(self.pairs[1]) + " over " + \
                cards.getPluralRankDescription(self.pairs[0])
            HandDescription.extra = self.pairs[1] + " " + self.pairs[0]
        elif self.pairs is not None:
            HandDescription.description = PAIR
            HandDescription.extraDescription = cards.getPluralRankDescription(self.pairs[0])
            HandDescription.extra = self.pairs[0]

        return HandDescription

    def getdescription(self, handType, extra):

        if handType == STRAIGHT_FLUSH:
            description = extra + STRAIGHT_FLUSH_DESC
        elif handType == FOUR_OF_A_KIND:
            description = FOUR_OF_A_KIND_DESC + extra
        elif handType == FULL_HOUSE:
            description = FULL_HOUSE_DESC + extra
        elif handType == FLUSH:
            description = extra + FLUSH_DESC
        elif handType == STRAIGHT:
            description = extra + STRIGHT_DESC
        elif handType == THREE_OF_A_KIND:
            description = THREE_OF_A_KIND_DESC + extra
        elif handType == TWO_PAIR:
            description = TWO_PAIR_DESC + extra
        elif handType == PAIR:
            description = PAIR_DESC + extra
        elif handType == HIGH_CARD:
            description = extra

        return description

    def getRanks(self):

        ranks = []

        for i in 0,5:
            ranks.append(self.cards[i])

        return ranks

    def display(self):

        for i in 0,5:
            print(cards.getCardDescription(self.cards[i]) + "\n")


















