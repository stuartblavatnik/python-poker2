# python-poker2

Conversion of php poker game into Python as a learning experience.

The game consists of a player making a bet and being delt 5 cards.  The house also gets 5 cards.  There is no drawing of extra cards.  
Each hand is parsed and compared to the other and the player either receives or loses units of bet based on the outcome.  This is a text 
only version of the game.

The application is currently made up of 3 main modules:

1) poker.py -- main entry point to the game.  It provides a command line interface allowing for the user to place bets then the deck is shuffled
and the cards are dealt.  The outcome is determined and bet is added or subtracted from the players' credits.  When the credits reach 0 or the
user enters 'quit' the game ends.

2) cards.py -- some inline functions that are used for determining a card's suit and rank.  The deck of cards is represented as an array of values from 0 - 51 where each rank is card index div 4 (2 through ace) and each suit is
the card index modulo 4

3) hands.py -- a class that represents a hand of cards (assumption is currently a 5 card hand) including parsing, displaying (as text) and
comparing against other hands.

How to run:  python poker.py

unit tests are in the tests directory

