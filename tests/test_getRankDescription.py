from unittest import TestCase
import cards

class TestGetRankDescription(TestCase):
    def test_getRankDescription(self):
       expectedResults = []
       expectedResults.append("Two")
       expectedResults.append("Three")
       expectedResults.append("Four")
       expectedResults.append("Five")
       expectedResults.append("Six")
       expectedResults.append("Seven")
       expectedResults.append("Eight")
       expectedResults.append("Nine")
       expectedResults.append("Ten")
       expectedResults.append("Jack")
       expectedResults.append("Queen")
       expectedResults.append("King")
       expectedResults.append("Ace")
       for i in 0, len(expectedResults) - 1:
           self.assertEquals(cards.getRankDescription(i), expectedResults[i])

