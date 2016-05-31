import hands
import sys
import random
import itertools

def main():
    __credits = 500
    game_continues = True
    print("Welcome to poker")

    while game_continues:
        print("You have " + str(__credits) + " credits.")
        try:
            response = input("Place your wager (or quit to quit)")
            if (response == "quit"):
                exit()
            elif int(response) > __credits:
                print("You do not have enough credits")
            elif int(response) < 1:
                print("Bets need to be at least 1")
            else:
                result = play_game()
                if result == 1:
                    print("You win")
                    __credits += int(response)
                elif result == -1:
                    print("You lose")
                    __credits -= int(response)
                    if __credits <= 0:
                        exit()
                else:
                    print("Tie")
        except(ValueError):
            print("Need to specify integer for your wager.")

def play_game():

    deck = list(range(0, 51))
    random.shuffle(deck)
    player_cards = deck[0:5]
    dealer_cards = deck[5:10]

    player_hand = hands.Hands(player_cards)
    dealer_hand = hands.Hands(dealer_cards)

    print("Player hand " + player_hand.display())
    print(player_hand.get_description())
    print("Dealer hand " + dealer_hand.display())
    print(dealer_hand.get_description())

    return player_hand.compare(dealer_hand)

if __name__ == "__main__":
    main()

