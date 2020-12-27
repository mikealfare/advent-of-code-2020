from typing import List


Deck = List[int]


def play_round(player_1: Deck, player_2: Deck):
    card_1 = player_1.pop(0)
    card_2 = player_2.pop(0)
    if card_1 > card_2:
        player_1.append(card_1)
        player_1.append(card_2)
    elif card_2 > card_1:
        player_2.append(card_2)
        player_2.append(card_1)


def play_game(player_1: Deck, player_2: Deck) -> int:
    turns = 0
    while len(player_1) > 0 and len(player_2) > 0:
        play_round(player_1, player_2)
        turns += 1
    return turns


def play_round_recursive(player_1: Deck, player_2: Deck):
    card_1 = player_1.pop(0)
    card_2 = player_2.pop(0)
    if len(player_1) >= card_1 and len(player_2) >= card_2:
        sub_game_1 = player_1.copy()[:card_1]
        sub_game_2 = player_2.copy()[:card_2]
        play_game_recursive(sub_game_1, sub_game_2)
        if len(sub_game_1) == 0:
            player_2.append(card_2)
            player_2.append(card_1)
        elif len(sub_game_2) == 0:
            player_1.append(card_1)
            player_1.append(card_2)
        else:
            raise ValueError(f'ERROR - unexpected scenario: player 1: {player_1}, player_2: {player_2}')
    else:
        if card_1 > card_2:
            player_1.append(card_1)
            player_1.append(card_2)
        elif card_2 > card_1:
            player_2.append(card_2)
            player_2.append(card_1)


def play_game_recursive(player_1: Deck, player_2: Deck):
    positions = []
    while len(player_1) > 0 and len(player_2) > 0:
        if (player_1, player_2) not in positions:
            positions.append((player_1.copy(), player_2.copy()))
            play_round_recursive(player_1, player_2)
        else:
            player_2.clear()


def score_deck(deck: Deck) -> int:
    score = 0
    for i in range(len(deck)):
        score += deck[i] * (len(deck) - i)
    return score


def main():
    player_1 = [47, 19, 22, 31, 24, 6, 10, 5, 1, 48, 46, 27, 8, 45, 16, 28, 33, 41, 42, 36, 50, 39, 30, 11, 17]
    player_2 = [4, 18, 21, 37, 34, 15, 35, 38, 20, 23, 9, 25, 32, 13, 26, 2, 12, 44, 14, 49, 3, 40, 7, 43, 29]
    play_game(player_1, player_2)
    winning_deck = player_1
    if player_2:
        winning_deck = player_2
    score = score_deck(winning_deck)
    print(f'the winning deck has a score of {score}')
    player_1 = [47, 19, 22, 31, 24, 6, 10, 5, 1, 48, 46, 27, 8, 45, 16, 28, 33, 41, 42, 36, 50, 39, 30, 11, 17]
    player_2 = [4, 18, 21, 37, 34, 15, 35, 38, 20, 23, 9, 25, 32, 13, 26, 2, 12, 44, 14, 49, 3, 40, 7, 43, 29]
    play_game_recursive(player_1, player_2)
    winning_deck = player_1
    if player_2:
        winning_deck = player_2
    score = score_deck(winning_deck)
    print(f'the winning deck in the recursive version has a score of {score}')



if __name__ == '__main__':
    main()