"""Simulate Blackjack to show odds that you will end up losing more than winning in value after 
each play

(base) macuser1@Mac week6 % python3 -i blackjack.py 
>>> gamble(basic_strat)
-628
>>> gamble(basic_strat)
-566
>>> gamble(basic_strat)
-573
>>> gamble(basic_strat)
-678
>>> gamble(basic_strat)
-583
>>> gamble(basic_strat)
-473
>>> 


"""

import random 

points = {'J': 10, 'Q': 10, 'K': 10, 'A': 1}

def hand_score(hand):
    """Total score for hand
    >>> hand_score(['A', 3, 6])
    20
    >>> hand_score(['A', 'J', 'A'])
    20
    """
    total = sum([points.get(card, card) for card in hand])
    if total <= 11 and 'A' in hand: 
        return total + 10 
    return total 

def shuffle_cards():
    deck = (['J', 'Q', 'K', 'A'] + list(range(2, 11))) * 4 
    random.shuffle(deck)
    return iter(deck)

def player_turn(up_card, cards, strategy, deck):
    while hand_score(cards) <= 21 and strategy(up_card, cards):
        cards.append(next(deck))

def dealer_turn(cards, deck):
    while hand_score(cards) < 17: 
        cards.append(next(deck))

def blackjack(strategy, announce=print):
    """Play a hand of casino blackjack"""

    deck = shuffle_cards()
    player_cards = [next(deck)]
    up_card = next(deck)
    hole_card = next(deck)

    player_turn(up_card, player_cards, strategy, deck)
    if hand_score(player_cards) > 21:
        announce('Player goes bust with', player_cards, 
                 'against a', up_card) 
        return -1
    
    dealer_cards = [up_card, hole_card]
    dealer_turn(dealer_cards, deck)
    if hand_score(dealer_cards) > 21:
        announce('Dealer busts with', dealer_cards)
        return 1 
    else:
        announce('Player has', hand_score(player_cards), 
                 'and dealer has', hand_score(dealer_cards))
        diff = hand_score(player_cards) - hand_score(dealer_cards)
        return max(-1, min(1, diff))
    
def basic_strat(up_card, cards):
    if hand_score(cards) <= 11:
        return True
    if up_card in [2, 3, 4, 5, 6]:
        return False
    return hand_score(cards) < 17 

def system(*args): 
    """Dont print or do anything"""

def gamble(strategy, hands=10000): 
    """simulating gambling 1000 times to check odds"""
    return sum([blackjack(strategy, system) for _ in range(hands)])