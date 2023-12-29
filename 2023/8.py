import re
import typing as tp
import math

from utils import read_file

find_numbers_pattern = re.compile('[A-Z1-9]+')


def solution():
    instruction, map_ = parse_file()
    starting_keys = [it for it in map_.keys() if it.endswith('A')]
    steps_by_key = []
    for key in starting_keys:
        steps_by_key.append(count_steps(instruction, map_, key))

    return math.lcm(*steps_by_key)


def parse_file() -> tp.Tuple[str, dict]:
    instruction, raw_map = read_file(8).split('\n\n')
    map_ = {}
    for it in raw_map.split('\n'):
        key, l, r = find_numbers_pattern.findall(it)
        map_[key] = {'L': l, 'R': r}
    return instruction, map_


def count_steps(instruction: str, map_: dict, key: str):
    current_instruction = 0
    z_pos = []
    while len(z_pos) < 2:
        key = map_.get(key)[instruction[current_instruction % len(instruction)]]
        current_instruction += 1
        if key.endswith('Z'):
            z_pos.append(current_instruction)

    return z_pos[1] - z_pos[0]


print(solution())
