############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo


def deal_card():
    """Returns a random card from the deck"""
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(deck)


def calculate_score(hand):
    """Take a list of cards and return the score calculated from the cards"""
    score = sum(hand)
    length = len(hand)

    if score > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)

    if score == 21 and length == 2:
        return 0

    return score


def compare(players_score, computers_score):
    if players_score == computers_score:
        return "Draw"
    elif computers_score == 0:
        return "Lose, opponent has Blackjack"
    elif players_score == 0:
        return "Win with a Blackjack"
    elif players_score > 21:
        return "You went over. You lose"
    elif computers_score > 21:
        return "Opponent went over. You win"
    elif players_score > computers_score:
        return "You win"
    else:
        return "You lose"


def play_game():
    print(logo)

    is_game_over = False
    computers_hand = []
    players_hand = []

    for _ in range(2):
        computers_hand.append(deal_card())
        players_hand.append(deal_card())

    while not is_game_over:
        computers_score = calculate_score(computers_hand)
        players_score = calculate_score(players_hand)

        print(f"You current hand is {players_hand}, and score is {players_score}")
        print(f"Computers first card is {computers_hand[0]}")

        if players_score == 0 or computers_score == 0 or players_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass:")
            if user_should_deal == "y":
                players_hand.append(deal_card())
                players_score = calculate_score(players_hand)
            else:
                is_game_over = True

    while computers_score > 17 and computers_score != 0:
        computers_hand.append(deal_card())
        print(f"Computers hand: {computers_hand}")
        computers_score = calculate_score(computers_hand)

    print(f"\n\nYour final hand: {players_hand}, Final score {players_score}")
    print(f"Computers final hand {computers_hand}, final score: {computers_score}")
    print(compare(players_score=players_score, computers_score=computers_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n' ") == "y":
    play_game()
