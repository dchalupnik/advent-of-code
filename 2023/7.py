import typing as tp
from collections import Counter
from dataclasses import dataclass

from utils import next_line


VALUES = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}

@dataclass
class Hand:
    cards: Counter
    bid: int
    value: int


def solution():
    hands = []
    for line in next_line(7):
        hands.append(parse_hand(line))

    total_value = 0
    sorted_hand = sorted(hands, key=lambda it: it.value)
    for i, it in enumerate(sorted(hands, key=lambda it: it.value)):
        total_value += it.bid * (i+1)
    return total_value


def parse_hand(line):
    cards, bid = line.split(' ')
    cards = Counter(cards)
    value = count_value(cards)
    return Hand(value=value, bid=int(bid), cards=cards)


def count_value(cards: Counter):
    if value := count_fives(cards):
        return value * pow(100, 6)

    if value := count_fours(cards):
        return value * pow(100, 5)

    if value := count_three(cards):
        return value * pow(100, 3)

    if value := count_two(cards):
        return value * pow(100, 1)

    return count_ones(cards)


def count_fives(cards: Counter):
    most_common, *_ = cards.most_common(1)
    if most_common[1] == 5:
        return VALUES[most_common[0]]

    return 0


def count_fours(cards: Counter):
    most_common, second_most_common = cards.most_common(2)
    if most_common[1] == 4:
        return VALUES[most_common[0]] * 2 + VALUES[second_most_common[0]]

    return 0


def count_three(cards: Counter):
    most_common = cards.most_common(3)
    if most_common[0][1] == 3:
        value = VALUES[most_common[0][0]] * 100
        if most_common[1][1] == 2:
            value += VALUES[most_common[1][0]] * 50 + sum([VALUES[it[0]] for it in most_common[2:]])
        else:
            value += sum([VALUES[it[0]] for it in most_common[1:]])
        return value

    return 0


def count_two(cards: Counter):
    most_common = cards.most_common()
    if most_common[0][1] == 2:
        value = VALUES[most_common[0][0]] * 100
        if most_common[1][1] == 2:
            value += VALUES[most_common[1][0]] * 50 + VALUES[most_common[2][0]]
        else:
            value += sum([VALUES[it[0]] for it in most_common[1:]])
        return value

    return 0


def count_ones(cards: Counter):
    return max(cards.keys())



print(solution())