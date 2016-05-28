from unittest import TestCase
import cards

class TestGetSuitDescription(TestCase):
    def test_getSuitDescription(self):
        expectedResults = []
        expectedResults.append("Clubs")
        expectedResults.append("Diamonds")
        expectedResults.append("Hearts")
        expectedResults.append("Spades")

        for i in 0, len(expectedResults) - 1:
            self.assertEquals(cards.getSuitDescription(i), expectedResults[i])

