from unittest import TestCase
import cards

class TestGetRank(TestCase):
    def test_getRank(self):
        expectedResults = []
        expectedResults.append(0)
        expectedResults.append(0)
        expectedResults.append(0)
        expectedResults.append(0)
        expectedResults.append(1)
        expectedResults.append(1)
        expectedResults.append(1)
        expectedResults.append(1)
        expectedResults.append(2)
        expectedResults.append(2)
        expectedResults.append(2)
        expectedResults.append(2)
        expectedResults.append(3)
        expectedResults.append(3)
        expectedResults.append(3)
        expectedResults.append(3)
        expectedResults.append(4)
        expectedResults.append(4)
        expectedResults.append(4)
        expectedResults.append(4)
        expectedResults.append(5)
        expectedResults.append(5)
        expectedResults.append(5)
        expectedResults.append(5)
        expectedResults.append(6)
        expectedResults.append(6)
        expectedResults.append(6)
        expectedResults.append(6)
        expectedResults.append(7)
        expectedResults.append(7)
        expectedResults.append(7)
        expectedResults.append(7)
        expectedResults.append(8)
        expectedResults.append(8)
        expectedResults.append(8)
        expectedResults.append(8)
        expectedResults.append(9)
        expectedResults.append(9)
        expectedResults.append(9)
        expectedResults.append(9)
        expectedResults.append(10)
        expectedResults.append(10)
        expectedResults.append(10)
        expectedResults.append(10)
        expectedResults.append(11)
        expectedResults.append(11)
        expectedResults.append(11)
        expectedResults.append(11)
        expectedResults.append(12)
        expectedResults.append(12)
        expectedResults.append(12)
        expectedResults.append(12)

        for i in 0, len(expectedResults) - 1:
            self.assertEquals(cards.getRank(i), expectedResults[i])
