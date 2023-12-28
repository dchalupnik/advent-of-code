import typing as tp
from dataclasses import dataclass
from functools import reduce

from utils import read_file
import re

find_numbers_pattern = re.compile('\\d+')

@dataclass
class Race:
    time: int
    distance: int


def solution():
    races = load_races()
    combinations = []
    for race in races:
        combinations.append(count_combinations(race))

    return reduce(lambda x, y: x*y, combinations)


def load_races() -> tp.Generator[Race, None, None]:
    data = read_file(6)
    time, distance = data.split('\n')
    time = find_numbers_pattern.findall(time)
    distance = find_numbers_pattern.findall(distance)
    for i in range(len(time)):
        yield Race(
            time=int(time[i]),
            distance=int(distance[i])
        )


def count_combinations(race: Race) -> int:
    combinations_count = 0
    for i in range(1, race.time):
        if (race.time - i) * i > race.distance:
            combinations_count += 1
    return combinations_count


def solution2():
    time, distance = load_race()
    # first_time = distance / time
    # if first_time % 1 != 0:
    #     first_time = int(first_time + 1)
    #
    # return time - first_time * 2 + 1
    return count_combinations(Race(time=time, distance=distance))


def load_race() -> tp.Tuple[int, int]:
    data = read_file(6)
    time, distance = data.split('\n')
    time = find_numbers_pattern.findall(time)
    distance = find_numbers_pattern.findall(distance)
    return int(''.join(time)), int(''.join(distance))


print(solution2())