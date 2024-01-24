import typing as tp

from utils import next_line
from itertools import combinations


def solution():
    total_valid_arragements = 0
    for line in next_line(12):
        code, instruction = line.split(' ')
        instruction = [int(it) for it in instruction.split(',')]
        total_valid_arragements += count_arrangements(code, instruction)
    return total_valid_arragements


def count_arrangements(code: str, instruction: tp.List[int]):
    combinations = generate_combinations(code, instruction)
    return count_valid_arrangements(combinations, instruction)


def generate_combinations(code: str, instruction: tp.List[int]) -> tp.Generator[tp.List[bool], None, None]:
    max_combinations = sum(instruction)
    wildcard_to_change = max_combinations - code.count('#')
    wildcard_positions = [i for i, it in enumerate(code) if it == '?']
    for combination in list(combinations(wildcard_positions, wildcard_to_change)):
        yield [True if it == "#" or i in combination else False for i, it in enumerate(code)]


def count_valid_arrangements(combinations: tp.Generator[tp.List[bool], None, None], instruction: tp.List[int]):
    valid_count = 0
    for combination in combinations:
        parsed_combination = []
        current_number = 0
        for it in combination:
            if it:
                current_number += 1
            elif current_number:
                parsed_combination.append(current_number)
                current_number = 0

        if current_number:
            parsed_combination.append(current_number)

        if parsed_combination == instruction:
            valid_count += 1

    return valid_count


print(solution())