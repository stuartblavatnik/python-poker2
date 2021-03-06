from unittest import TestCase
import cards


class TestGetCardDescription(TestCase):
    def test_getCardDescription(self):

        expectedResults = []
        expectedResults.append("Two of Clubs")
        expectedResults.append("Two of Diamonds")
        expectedResults.append("Two of Hearts")
        expectedResults.append("Two of Spades")
        expectedResults.append("Three of Clubs")
        expectedResults.append("Three of Diamonds")
        expectedResults.append("Three of Hearts")
        expectedResults.append("Three of Spades")
        expectedResults.append("Four of Clubs")
        expectedResults.append("Four of Diamonds")
        expectedResults.append("Four of Hearts")
        expectedResults.append("Four of Spades")
        expectedResults.append("Five of Clubs")
        expectedResults.append("Five of Diamonds")
        expectedResults.append("Five of Hearts")
        expectedResults.append("Five of Spades")
        expectedResults.append("Six of Clubs")
        expectedResults.append("Six of Diamonds")
        expectedResults.append("Six of Hearts")
        expectedResults.append("Six of Spades")
        expectedResults.append("Seven of Clubs")
        expectedResults.append("Seven of Diamonds")
        expectedResults.append("Seven of Hearts")
        expectedResults.append("Seven of Spades")
        expectedResults.append("Eight of Clubs")
        expectedResults.append("Eight of Diamonds")
        expectedResults.append("Eight of Hearts")
        expectedResults.append("Eight of Spades")
        expectedResults.append("Nine of Clubs")
        expectedResults.append("Nine of Diamonds")
        expectedResults.append("Nine of Hearts")
        expectedResults.append("Nine of Spades")
        expectedResults.append("Ten of Clubs")
        expectedResults.append("Ten of Diamonds")
        expectedResults.append("Ten of Hearts")
        expectedResults.append("Ten of Spades")
        expectedResults.append("Jack of Clubs")
        expectedResults.append("Jack of Diamonds")
        expectedResults.append("Jack of Hearts")
        expectedResults.append("Jack of Spades")
        expectedResults.append("Queen of Clubs")
        expectedResults.append("Queen of Diamonds")
        expectedResults.append("Queen of Hearts")
        expectedResults.append("Queen of Spades")
        expectedResults.append("King of Clubs")
        expectedResults.append("King of Diamonds")
        expectedResults.append("King of Hearts")
        expectedResults.append("King of Spades")
        expectedResults.append("Ace of Clubs")
        expectedResults.append("Ace of Diamonds")
        expectedResults.append("Ace of Hearts")
        expectedResults.append("Ace of Spades")

        for i in 0,len(expectedResults)-1:
            self.assertEquals(cards.getCardDescription(i),expectedResults[i])
        

