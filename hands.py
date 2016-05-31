import cards
from collections import Counter

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
    __cards = []
    __three_of_a_kind = None
    __four_of_a_kind = None
    __pairs = []
    __baby_straight = False
    __hand_type = ""
    __hand_extra_description = ""
    __hand_extra = ""

    def __init__(self, _cards):
        self.__cards = _cards
        self.parse()

    def get_type(self):
        return self.__hand_type;

    def get_extra_description(self):
        return self.__hand_extra_description;

    def get_extra(self):
        return self.__hand_extra;

    def get_pairs(self):
        return self.__pairs;

    def __build_multiples(self, ranks):

        multiple = False
        rank_keys = Counter(ranks).keys()
        rank_values = list(Counter(ranks).values())
        self.__pairs = []

        array_count = len(rank_keys)

        for i in range(0, array_count):
            if rank_values[i] > 1:
                multiple = True
                if rank_values[i] == 2:
                    self.__pairs.append(list(rank_keys)[i])
                elif rank_values[i] == 3:
                    self.__three_of_a_kind = list(rank_keys)[i]
                elif rank_values[i] == 4:
                    self.__four_of_a_kind = list(rank_keys)[i]
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
                self.__baby_straight = True

        return straight

    def parse(self):

        multiple = False
        flush = False

        self.__cards.sort()
        high_card = self.__cards[-1]
        high_card_description = cards.getSingleCardDescription(high_card) + " " + "High"

        suits = []
        ranks = []

        for card in self.__cards:
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
                self.__hand_type = STRAIGHT_FLUSH

                if self.__baby_straight:
                    self.__hand_extra_description = "Five High"
                    self.__hand_extra = self.__cards[3]
                else:
                    self.__hand_extra_description = high_card_description
                    self.__hand_extra = high_card
            elif flush:
                self.__hand_type = FLUSH
                self.__hand_extra_description = high_card_description
                self.__hand_extra = high_card
            elif straight:
                self.__hand_type = STRAIGHT

                if self.__baby_straight:
                    self.__hand_extra_description = "Five High"
                    self.__hand_extra = self.__cards[3]
                else:
                    self.__hand_extra_description = high_card_description
                    self.__hand_extra = high_card
            else:
                self.__hand_type = HIGH_CARD
                self.__hand_extra_description = high_card_description
                self.__hand_extra = high_card

        elif self.__four_of_a_kind is not None:
            self.__hand_type = FOUR_OF_A_KIND
            self.__hand_extra_description = cards.getPluralRankDescription(self.__four_of_a_kind)
            self.__hand_extra = self.__four_of_a_kind
        elif self.__three_of_a_kind is not None and len(self.__pairs) == 1:
            self.__hand_type = FULL_HOUSE
            self.__hand_extra_description = cards.getPluralRankDescription(self.__three_of_a_kind) + " over " + \
                                                cards.getPluralRankDescription(self.__pairs[0])
            self.__hand_extra = self.__three_of_a_kind
        elif self.__three_of_a_kind is not None:
            self.__hand_type = THREE_OF_A_KIND
            self.__hand_extra_description = cards.getPluralRankDescription(self.__three_of_a_kind)
            self.__hand_extra = self.__three_of_a_kind
        elif self.__pairs is not None and len(self.__pairs) == 2:
            self.__pairs.sort()
            self.__hand_type = TWO_PAIR
            self.__hand_extra_description = cards.getPluralRankDescription(self.__pairs[1]) + " over " + \
                                                cards.getPluralRankDescription(self.__pairs[0])
            self.__hand_extra = str(self.__pairs[1]) + " " + str(self.__pairs[0])
        elif self.__pairs is not None:
            self.__hand_type = PAIR
            self.__hand_extra_description = cards.getPluralRankDescription(self.__pairs[0])
            self.__hand_extra = self.__pairs[0]
        else:
            self.__hand_type = HIGH_CARD
            self.__hand_extra_description = high_card_description
            self.__hand_extra = high_card

    def get_description(self):

        hand_type = self.get_type()
        extra_description = self.get_extra_description()

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

    def get_ranks(self):

        ranks = []

        for i in range(0, 5):
            ranks.append(cards.getRank(self.__cards[i]))

        return ranks

    def display(self):

        return_display = ""

        for i in range(0, 5):
            return_display += cards.getCardDescription(self.__cards[i]) + "\n"

        return return_display


    '''
    def compare(self, __other_hand):

        comparison_result = 0;

        Hands other_hand = __other_hand

        if (self.type) > other_hand
    '''

    def __compare_hands_by_individual_values(self, other):

        self_ranks = self.get_ranks()
        other_ranks = other.get_ranks()

        self_ranks.sort()
        other_ranks.sort()

        for i in range(0, len(self_ranks)):
            if self_ranks[i] > other_ranks[i]:
                return 1
            elif self_ranks[i] < other_ranks[i]:
                return -1

        return 0

    def __compare_two_pair_hands(self, other):

        if self.get_pairs()[0] > other.get_pairs()[0]:
            return 1
        elif self.get_pairs()[0] < other.get_pairs()[0]:
            return -1
        elif self.get_pairs()[1] > other.get_pairs()[1]:
            return 1
        elif self.get_pairs()[1] < other.get_pairs()[1]:
            return -1
        else:
            return self.__compare_hands_by_individual_values(other)

    def __compare_one_pair_hands(self, other):
        if self.get_pairs()[0] > other.get_pairs()[0]:
            return 1
        elif self.get_pairs()[0] < other.get_pairs()[0]:
            return -1
        else:
            return self.__compare_hands_by_individual_values(other)

    '''
       Compares two hands.  If the hand passed in is better than this hand, -1 is retured.  If the opposite 1 is returned.
       If hands are equal then 0 is returned
       '''
    def compare(self, other):

        if self.get_type() > other.get_type():
            compare_results = 1
        elif self.get_type() < other.get_type():
            compare_results = -1
        else:
            hand_type = self.get_type()
            if hand_type in [STRAIGHT_FLUSH, FLUSH, STRAIGHT, HIGH_CARD]:
                compare_results = self.__compare_hands_by_individual_values(other)
            elif hand_type in [FOUR_OF_A_KIND, FULL_HOUSE, THREE_OF_A_KIND]:
                compare_results = False
            elif hand_type == TWO_PAIR:
                compare_results = self.__compare_two_pair_hands(other)
            elif hand_type == PAIR:
                compare_results = self.__compare_one_pair_hands(other)

        return compare_results
