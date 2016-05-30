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
    __type = ""
    threeOfAKind = None
    fourOfAKind = None
    pairs = []
    baby_straight = False

    def __init__(self, _cards):
        self.cards = _cards
        self.__type = self.parse()

    def get_type(self):
        return self.__type;

    #    def compare(self, other):

    def __build_multiples(self, ranks):

        multiple = False
        rank_keys = Counter(ranks).keys()
        rank_values = list(Counter(ranks).values())
        self.pairs = []

        array_count = len(rank_keys)

        for i in range(0, array_count):
            if rank_values[i] > 1:
                multiple = True
                if rank_values[i] == 2:
                    self.pairs.append(list(rank_keys)[i])
                elif rank_values[i] == 3:
                    self.threeOfAKind = list(rank_keys)[i]
                elif rank_values[i] == 4:
                    self.fourOfAKind = list(rank_keys)[i]
        return multiple

    def __is_straight(self, ranks):

        straight = False

        rank_keys = Counter(ranks).keys()

        if len(rank_keys) == 5:
            if list(rank_keys)[4] - list(rank_keys)[0] == 4:
                straight = True
            elif list(rank_keys)[0] == 0 and list(rank_keys)[1] == 1 and list(rank_keys)[2] == 2 and \
                list(rank_keys)[3] == 3 and list(rank_keys)[4] == 12:
                straight = True
                self.baby_straight = True

        return straight

    def parse(self):

        hand_description = namedtuple('HandDescription', 'type extra_description extra')

        multiple = False
        flush = False

        self.cards.sort()
        high_card = self.cards[-1]
        high_card_description = cards.getSingleCardDescription(high_card) + " " + "High"

        suits = []
        ranks = []

        for card in self.cards:
            suits.append(cards.getSuit(card))
            ranks.append(cards.getRank(card))

        # Normalize suits to get the count of different suits in the hand
        suits = list(set(suits))

        if len(suits) == 1:
            flush = True
            flushType = suits[0]
        else:
            multiple = self.__build_multiples(ranks)

        if not multiple:

            straight = self.__is_straight(ranks)

            if straight and flush:
                hand_description.type = STRAIGHT_FLUSH

                if self.baby_straight:
                    hand_description.extra_description = "Five High"
                    hand_description.extra = self.cards[3]
                else:
                    hand_description.extra_description = high_card_description
                    hand_description.extra = high_card
            elif flush:
                hand_description.type = FLUSH
                hand_description.extra_description = high_card_description
                hand_description.extra = high_card
            elif straight:
                hand_description.type = STRAIGHT

                if self.baby_straight:
                    hand_description.extra_description = "Five High"
                    hand_description.extra = self.cards[3]
                else:
                    hand_description.extra_description = high_card_description
                    hand_description.extra = high_card
            else:
                hand_description.type = HIGH_CARD
                hand_description.extra_description = high_card_description
                hand_description.extra = high_card

        elif self.fourOfAKind is not None:
            hand_description.type = FOUR_OF_A_KIND
            hand_description.extra_description = cards.getPluralRankDescription(self.fourOfAKind)
            hand_description.extra = self.fourOfAKind
        elif self.threeOfAKind is not None and len(self.pairs) == 1:
            hand_description.type = FULL_HOUSE
            hand_description.extra_description = cards.getPluralRankDescription(self.threeOfAKind) + " over " + \
                                                cards.getPluralRankDescription(self.pairs[0])
            hand_description.extra = self.threeOfAKind
        elif self.threeOfAKind is not None:
            hand_description.type = THREE_OF_A_KIND
            hand_description.extra_description = cards.getPluralRankDescription(self.threeOfAKind)
            hand_description.extra = self.threeOfAKind
        elif self.pairs is not None and len(self.pairs) == 2:
            self.pairs.sort()
            hand_description.type = TWO_PAIR
            hand_description.extra_description = cards.getPluralRankDescription(self.pairs[1]) + " over " + \
                                                cards.getPluralRankDescription(self.pairs[0])
            hand_description.extra = str(self.pairs[1]) + " " + str(self.pairs[0])
        elif self.pairs is not None:
            hand_description.type = PAIR
            hand_description.extra_description = cards.getPluralRankDescription(self.pairs[0])
            hand_description.extra = self.pairs[0]
        else:
            hand_description.type = HIGH_CARD
            hand_description.extra_description = high_card_description
            hand_description.extra = high_card

        return hand_description

    def get_description(self):

        hand_type = self.__type.type
        extra_description = self.__type.extra_description

        if hand_type == STRAIGHT_FLUSH:
            description = extra_description + STRAIGHT_FLUSH_DESC
        elif hand_type == FOUR_OF_A_KIND:
            description = FOUR_OF_A_KIND_DESC + extra_description
        elif hand_type == FULL_HOUSE:
            description = FULL_HOUSE_DESC + extra_description
        elif hand_type == FLUSH:
            description = extra_description + FLUSH_DESC
        elif hand_type == STRAIGHT:
            description = extra_description + STRIGHT_DESC
        elif hand_type == THREE_OF_A_KIND:
            description = THREE_OF_A_KIND_DESC + extra_description
        elif hand_type == TWO_PAIR:
            description = TWO_PAIR_DESC + extra_description
        elif hand_type == PAIR:
            description = PAIR_DESC + extra_description
        elif hand_type == HIGH_CARD:
            description = extra_description

        return description

    def getRanks(self):

        ranks = []

        for i in 0, 5:
            ranks.append(self.cards[i])

        return ranks

    def display(self):

        for i in 0, 5:
            print(cards.getCardDescription(self.cards[i]) + "\n")
