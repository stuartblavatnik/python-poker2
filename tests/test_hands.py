from unittest import TestCase

import hands

import cards

class TestHands(TestCase):

    def doParseTest(self, cards, expected_description, expected_extra_description, expected_extra):
        cardsinhand = cards
        hand = hands.Hands(cardsinhand)

        hand_description_tuple = hand.parse()

        self.assertEquals(expected_description, hand_description_tuple.description)
        self.assertEquals(expected_extra_description, hand_description_tuple.extraDescription)
        self.assertEquals(expected_extra, hand_description_tuple.extra)

    def test_parse_four_of_a_kind(self):

        self.doParseTest([0,1,2,3,4], hands.FOUR_OF_A_KIND, "Twos", 0)
        self.doParseTest([48, 49, 50, 51, 4], hands.FOUR_OF_A_KIND, "Aces", 12)

    def test_parse_three_of_a_kind(self):

        self.doParseTest([0, 1, 2, 20, 40], hands.THREE_OF_A_KIND, "Twos", 0)
        self.doParseTest([4, 5, 6, 18, 30], hands.THREE_OF_A_KIND, "Threes", 1)

    def test_parse_two_pairs(self):

        self.doParseTest([0, 1, 4, 5, 40], hands.TWO_PAIR, "Threes over Twos", "1 0")
        self.doParseTest([4, 48, 49, 5, 27], hands.TWO_PAIR, "Aces over Threes", "12 1")


    def test_parse_pair(self):
        self.doParseTest([40, 0, 18, 51, 1], hands.PAIR, "Twos", 0)



'''
    def test_getdescription(self):
        self.fail()

    def test_getRanks(self):
        self.fail()

    def test_display(self):
        self.fail()
'''