import pytest

from tests.conftest import day_22


sample_player_1 = [9, 2, 6, 3, 1]
sample_player_2 = [5, 8, 4, 7, 10]


@pytest.mark.parametrize('player_1,expected_player_1,player_2,expected_player_2', [
    (
            [9, 2, 6, 3, 1], [2, 6, 3, 1, 9, 5],
            [5, 8, 4, 7, 10], [8, 4, 7, 10]
    ),
    (
            [2, 6, 3, 1, 9, 5], [6, 3, 1, 9, 5],
            [8, 4, 7, 10], [4, 7, 10, 8, 2]
    )
])
def test_play_round(
        player_1: day_22.Deck,
        player_2: day_22.Deck,
        expected_player_1: day_22.Deck,
        expected_player_2: day_22.Deck
):
    day_22.play_round(player_1, player_2)
    assert player_1 == expected_player_1
    assert player_2 == expected_player_2


@pytest.mark.parametrize('player_1,player_2,expected', [
    (sample_player_1, sample_player_2, 29)
])
def test_play_game(player_1: day_22.Deck, player_2: day_22.Deck, expected: int):
    assert day_22.play_game(player_1, player_2) == expected
    assert player_1 == []
    assert player_2 == [3, 2, 10, 6, 8, 5, 9, 4, 7, 1]


@pytest.mark.parametrize('deck,expected', [
    ([3, 2, 10, 6, 8, 5, 9, 4, 7, 1], 306)
])
def test_score_deck(deck: day_22.Deck, expected: int):
    assert day_22.score_deck(deck) == expected


@pytest.mark.parametrize('player_1,player_2', [
    (sample_player_1, sample_player_2)
])
def test_play_game_recursive(player_1: day_22.Deck, player_2: day_22.Deck):
    day_22.play_game_recursive(player_1, player_2)
    assert player_1 == []
    assert player_2 == [7, 5, 6, 2, 4, 1, 10, 8, 9, 3]


@pytest.mark.parametrize('player_1,player_2', [
    ([43, 19], [2, 29, 14])
])
def test_play_game_recursive_endless(player_1: day_22.Deck, player_2: day_22.Deck):
    day_22.play_game_recursive(player_1, player_2)
    assert player_1 != []
    assert player_2 == []
