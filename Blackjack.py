import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

def draw_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(player_score, dealer_score):
    if player_score > 21 and dealer_score  > 21:
        return "You busted, you lose."
    elif player_score == dealer_score:
        return "Draw!"
    elif dealer_score == 0:
        return "Dealer blackjack, you lose."
    elif player_score == 0:
        return "Blackjack, you win!"
    elif player_score > 21:
        return "You busted, you lose."
    elif dealer_score > 21:
        return "Dealer busted, you win!"
    elif player_score > dealer_score:
        return "You win!"
    else:
        return "You lose."

def play_game():
    print (logo)
    game_over = False
    player_cards = []
    dealer_cards = []

    for i in range(2):
        player_cards.append(draw_card())
        dealer_cards.append(draw_card())

    while not game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print (f"Your cards: {player_cards}, current score: {player_score}")
        print (f"Dealer's first card: {dealer_cards[0]}")
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            player_hit = input("Would you like to hit? Type 'y' for yes or 'n' for no: ")
            if player_hit == 'y':
                player_cards.append(draw_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(draw_card())
        dealer_score = calculate_score(dealer_cards)

    print (f"Your final hand: {player_cards}, final score: {player_score}")
    print (f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}")
    print (compare(player_score, dealer_score))

while input("Would you like to play a game of Blackjack? Type 'y' for yes or 'n' for no: ").lower() == 'y':
    play_game()

print ("Thanks for playing!")
