import typing as tp
from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations

from utils import next_line

@dataclass
class Point:
    x: int
    y: int


EXPANSE_VALUE = 1000000 - 1


def solution():
    points = list(get_points())
    all_pairs = list(combinations(list(range(len(points))), 2))
    return count_distance(points, all_pairs)


def get_points() -> tp.Generator[Point, None, None]:
    y = 0
    points = defaultdict(list)
    empty_count = defaultdict(int)
    for line in next_line(11):
        no_x = True
        for x, it in enumerate(line):
            if it == '#':
                points[x].append(Point(x=x, y=y))
                no_x = False
            else:
                empty_count[x] += 1

        if no_x:
            y += EXPANSE_VALUE
        y += 1

    line_len = len(line)
    for x, count in empty_count.items():
        if count == line_len:
            for i in range(x+1, line_len):
                for point in points[i]:
                    point.x += EXPANSE_VALUE

    for points in points.values():
        for point in points:
            yield point


def count_distance(points: tp.List[Point], pairs: tp.List[tp.Tuple[int, int]]):
    total_distance = 0
    for a, b in pairs:
        distance = abs(points[a].x - points[b].x) + abs(points[a].y - points[b].y)
        total_distance += distance
    return total_distance


print(solution())