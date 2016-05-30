from unittest import TestCase
import hands


class TestHands(TestCase):
    def __do_parse_test(self, cards, expected_type, expected_extra_description, expected_extra):

        hand = hands.Hands(cards)
        hand_description_tuple = hand.get_type()

        self.assertEquals(expected_type, hand_description_tuple.type)
        self.assertEquals(expected_extra_description, hand_description_tuple.extra_description)
        self.assertEquals(expected_extra, hand_description_tuple.extra)

    def __do_get_description_test(self, cards, expected_type):
        hand = hands.Hands(cards)
        self.assertEquals(expected_type, hand.get_description())

    def test_parse_high_card(self):
        self.__do_parse_test([40, 0, 18, 51, 27], hands.HIGH_CARD, "Ace High", 51)
        self.__do_parse_test([47, 0, 18, 10, 26], hands.HIGH_CARD, "King High", 47)

    def test_parse_pair(self):
        self.__do_parse_test([40, 0, 18, 51, 1], hands.PAIR, "Twos", 0)
        self.__do_parse_test([47, 0, 18, 51, 46], hands.PAIR, "Kings", 11)

    def test_parse_two_pairs(self):
        self.__do_parse_test([0, 1, 4, 5, 40], hands.TWO_PAIR, "Threes over Twos", "1 0")
        self.__do_parse_test([4, 48, 49, 5, 27], hands.TWO_PAIR, "Aces over Threes", "12 1")

    def test_parse_three_of_a_kind(self):
        self.__do_parse_test([0, 1, 2, 20, 40], hands.THREE_OF_A_KIND, "Twos", 0)
        self.__do_parse_test([4, 5, 6, 18, 30], hands.THREE_OF_A_KIND, "Threes", 1)

    def test_parse_straight(self):
        self.__do_parse_test([0, 5, 8, 12, 16], hands.STRAIGHT, "Six High", 16)
        self.__do_parse_test([16, 5, 22, 8, 12], hands.STRAIGHT, "Seven High", 22)
        self.__do_parse_test([51, 46, 42, 38, 34], hands.STRAIGHT, "Ace High", 51)
        self.__do_parse_test([51, 0, 4, 8, 12], hands.STRAIGHT, "Five High", 12)

    def test_parse_flush(self):
        self.__do_parse_test([0, 4, 8, 16, 32], hands.FLUSH, "Ten High", 32)
        self.__do_parse_test([37, 9, 17, 5, 1], hands.FLUSH, "Jack High", 37)

    def test_parse_full_house(self):
        self.__do_parse_test([0, 1, 2, 51, 50], hands.FULL_HOUSE, "Twos over Aces", 0)
        self.__do_parse_test([22, 4, 5, 6, 23], hands.FULL_HOUSE, "Threes over Sevens", 1)

    def test_parse_four_of_a_kind(self):
        self.__do_parse_test([0, 1, 2, 3, 4], hands.FOUR_OF_A_KIND, "Twos", 0)
        self.__do_parse_test([48, 49, 50, 51, 4], hands.FOUR_OF_A_KIND, "Aces", 12)

    def test_parse_straight_flush(self):
        self.__do_parse_test([0, 4, 8, 12, 16], hands.STRAIGHT_FLUSH, "Six High", 16)
        self.__do_parse_test([51, 47, 43, 39, 35], hands.STRAIGHT_FLUSH, "Ace High", 51)
        self.__do_parse_test([51, 3, 7, 11, 15], hands.STRAIGHT_FLUSH, "Five High", 15)

    def test_parse_description_high_card(self):
        self.__do_get_description_test([40, 0, 18, 51, 27], "Ace High")
        self.__do_get_description_test([47, 0, 18, 10, 26], "King High")

    def test_parse_description_pair(self):
        self.__do_get_description_test([40, 0, 18, 51, 1], "Pair of Twos")
        self.__do_get_description_test([47, 0, 18, 51, 46], "Pair of Kings")

    def test_parse_description_two_pairs(self):
        self.__do_get_description_test([0, 1, 4, 5, 40], "Two pairs Threes over Twos")
        self.__do_get_description_test([4, 48, 49, 5, 27], "Two pairs Aces over Threes")

    def test_parse_description_three_of_kind(self):
        self.__do_get_description_test([0, 1, 2, 20, 40], "Three Twos")
        self.__do_get_description_test([4, 5, 6, 18, 30], "Three Threes")

    def test_parse_description_straight(self):
        self.__do_get_description_test([0, 5, 8, 12, 16], "Six High Straight")
        self.__do_get_description_test([16, 5, 22, 8, 12], "Seven High Straight")
        self.__do_get_description_test([51, 46, 42, 38, 34], "Ace High Straight")
        self.__do_get_description_test([51, 0, 4, 8, 12], "Five High Straight")

    def test_parse_description_flush(self):
        self.__do_get_description_test([0, 4, 8, 16, 32], "Ten High Flush")
        self.__do_get_description_test([37, 9, 17, 5, 1], "Jack High Flush")

'''
    def test_getRanks(self):
        self.fail()

    def test_display(self):
        self.fail()
'''
