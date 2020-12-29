from typing import List, Dict


Cup = int
Cups = Dict[Cup, Cup]


def get_cups_to_move(cups: Cups, current_cup: Cup) -> List[Cup]:
    cups_to_move = []
    next_cup = cups[current_cup]
    for i in range(3):
        cups_to_move.append(next_cup)
        next_cup = cups[next_cup]
    return cups_to_move


def get_destination_cup(current_cup: Cup, cups_to_move: List[Cup], max_cup: Cup) -> Cup:
    if current_cup > 1:
        destination_cup = current_cup - 1
    else:
        destination_cup = max_cup
    while destination_cup in cups_to_move:
        if destination_cup > 1:
            destination_cup -= 1
        else:
            destination_cup = max_cup
    return destination_cup


def move_cups(cups: Cups, cups_to_move: List[Cup], current_cup: Cup, destination_cup: Cup):
    cups.update({
        current_cup: cups[cups_to_move[-1]],
        destination_cup: cups_to_move[0],
        cups_to_move[-1]: cups[destination_cup],
    })


def play_move(cups: Cups, current_cup: Cup) -> Cup:
    max_cup = len(cups)

    cups_to_move = get_cups_to_move(cups, current_cup)
    destination_cup = get_destination_cup(current_cup, cups_to_move, max_cup)
    move_cups(cups, cups_to_move, current_cup, destination_cup)
    next_cup = cups[current_cup]

    return next_cup


def create_cups_dict(cup_labels: List[Cup], fill: int = None) -> Cups:
    cups = {left: right for left, right in zip(cup_labels[:-1], cup_labels[1:])}
    if fill:
        fill_min = max(cups.keys()) + 1
        cups[cup_labels[-1]] = fill_min
        cups.update({cup: cup + 1 for cup in range(fill_min, fill)})
        cups[fill] = cup_labels[0]
    else:
        cups[cup_labels[-1]] = cup_labels[0]
    return cups


def get_string_starting_at_one(cups: Cups) -> str:
    cup_string = ''
    cup = cups[1]
    while cup != 1:
        cup_string += str(cup)
        cup = cups[cup]
    return cup_string


def main():
    cup_labels = [int(cup) for cup in '157623984']

    cups = create_cups_dict(cup_labels)
    current_cup = cup_labels[0]
    for cup in range(100):
        current_cup = play_move(cups, current_cup)
    print(f'the final sequence is {get_string_starting_at_one(cups)}')

    cups = create_cups_dict(cup_labels, 1_000_000)
    current_cup = cup_labels[0]
    for i in range(10_000_000):
        current_cup = play_move(cups, current_cup)
    answer = cups[1] * cups[cups[1]]
    print(f'the gold star cups multiply to {answer}')


if __name__ == '__main__':
    main()
