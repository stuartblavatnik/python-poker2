from unittest import TestCase
import cards

class TestGetPluralRankDescription(TestCase):
    def test_getPluralRankDescription(self):
        expectedResults = []
        expectedResults.append("Twos")
        expectedResults.append("Threes")
        expectedResults.append("Fours")
        expectedResults.append("Fives")
        expectedResults.append("Sixes")
        expectedResults.append("Sevens")
        expectedResults.append("Eights")
        expectedResults.append("Nines")
        expectedResults.append("Tens")
        expectedResults.append("Jacks")
        expectedResults.append("Queens")
        expectedResults.append("Kings")
        expectedResults.append("Aces")
        for i in 0, len(expectedResults) - 1:
            self.assertEquals(cards.getPluralRankDescription(i), expectedResults[i])
