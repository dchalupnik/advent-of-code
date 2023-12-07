import typing as tp
from dataclasses import dataclass
from collections import defaultdict

from utils import next_line


@dataclass
class Card:
    id_: int
    numbers: tp.Set[int]
    winning_numbers: tp.Set[int]


def solution() -> int:
    total_cards = 0
    multiplied_cards = defaultdict(int)
    for line in next_line(4):
        card = generate_card(line)
        total_win = count_win(card)
        addition = multiplied_cards.get(card.id_, 0) + 1
        for i in range(total_win):
            multiplied_cards[card.id_ + 1 + i] += addition

        total_cards += addition

    return total_cards


def generate_card(line: str) -> Card:
    card_id, numbers = line.split(': ')
    winning, actual = numbers.split(' | ')
    _, card_id = card_id.rsplit(' ', 1)
    return Card(
        id_=int(card_id),
        numbers={it for it in actual.split(' ') if it},
        winning_numbers={it for it in winning.split(' ') if it}
    )


def calculate_win(card: Card) -> int:
    """Part 1 solution"""
    matched_numbers = len(card.winning_numbers & card.numbers)
    if matched_numbers:
        return pow(2, matched_numbers - 1)

    return 0


def count_win(card: Card) -> int:
    """Count winning numbers"""
    return len(card.winning_numbers & card.numbers)


print(solution())