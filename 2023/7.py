import typing as tp
from collections import Counter
from dataclasses import dataclass

from utils import next_line


VALUES = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 1,
    'Q': 11,
    'K': 12,
    'A': 13,
}

@dataclass
class Hand:
    cards: str
    bid: int
    value: float


def solution():
    hands = []
    for line in next_line(7):
        hands.append(parse_hand(line))

    total_value = 0
    i = 0
    prev_value = 0
    for it in sorted(hands, key=lambda it: it.value):
        if it.value > prev_value:
            i += 1
            prev_value = it.value

        total_value += it.bid * i
    return total_value


def parse_hand(line: str) -> Hand:
    cards, bid = line.split(' ')
    cards_counter = Counter(cards)
    value = count_value(cards_counter, cards)
    return Hand(value=value, bid=int(bid), cards=cards)


def count_value(cards_counter: Counter, cards: str) -> int:
    most_common_values_no_j = [it[1] for it in Counter(cards.replace('J', '')).most_common()]
    j_count = cards_counter.get('J', 0)

    if j_count == 5 or most_common_values_no_j[0] + j_count == 5:
        multiplayer = 6
    elif most_common_values_no_j[0] + j_count == 4:
        multiplayer = 5
    elif most_common_values_no_j[0] + j_count == 3 and most_common_values_no_j[1] == 2:
        multiplayer = 4
    elif most_common_values_no_j[0] + j_count == 3 and most_common_values_no_j[1] == 1:
        multiplayer = 3
    elif most_common_values_no_j[0] == 2 and most_common_values_no_j[1] == 2:
        multiplayer = 2
    elif most_common_values_no_j[0] + j_count == 2:
        multiplayer = 1
    else:
        multiplayer = 0

    return count_ones(cards) * pow(100, multiplayer)


def count_ones(cards: str):
    return sum([VALUES[it] / pow(100, i) for i, it in enumerate(cards)])


print(solution())
