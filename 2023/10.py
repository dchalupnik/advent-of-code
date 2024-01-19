import typing as tp
from collections import defaultdict
from dataclasses import dataclass

from utils import read_file


@dataclass
class Position:
    x: int
    y: int


MOVES = {
    '|': lambda pos, prev_pos: Position(x=pos.x, y=pos.y + (1 if pos.y > prev_pos.y else -1)),
    '-': lambda pos, prev_pos: Position(x=pos.x + (1 if pos.x > prev_pos.x else -1), y=pos.y),
    'F': lambda pos, prev_pos: Position(x=pos.x, y=pos.y+1) if pos.x != prev_pos.x else Position(x=pos.x+1, y=pos.y),
    'L': lambda pos, prev_pos: Position(x=pos.x, y=pos.y-1) if pos.x != prev_pos.x else Position(x=pos.x+1, y=pos.y),
    'J': lambda pos, prev_pos: Position(x=pos.x, y=pos.y-1) if pos.x != prev_pos.x else Position(x=pos.x-1, y=pos.y),
    '7': lambda pos, prev_pos: Position(x=pos.x, y=pos.y+1) if pos.x != prev_pos.x else Position(x=pos.x-1, y=pos.y),
}


def solution():
    raw_map = read_file(10)
    map_ = raw_map.split('\n')
    start_position = find_start(map_)
    position = find_first_step(map_, start_position)
    distance_value, point_y_map = next_step(map_, position, start_position)
    inside_points = calculate_inside_points(map_, point_y_map)
    return int(distance_value / 2), inside_points


def find_start(map_: tp.List[str]) -> Position:
    for y, it in enumerate(map_):
        for x in range(len(it)):
            if it[x] == 'S':
                return Position(x=x, y=y)


def find_first_step(map_: tp.List[str], start_position: Position) -> Position:
    if start_position.y > 0 and map_[start_position.y - 1][start_position.x] in '|F7':
        return Position(y=start_position.y - 1, x=start_position.x)
    if start_position.x > 0 and map_[start_position.y][start_position.x - 1] in '-FL':
        return Position(y=start_position.y, x=start_position.x - 1)
    if start_position.x < len(map_[0]) - 1 and map_[start_position.y][start_position.x + 1] in '-7J':
        return Position(y=start_position.y, x=start_position.x + 1)
    if start_position.y > len(map_) - 1 and map_[start_position.y + 1][start_position.x] in '|LJ':
        return Position(y=start_position.y + 1, x=start_position.x)

    raise Exception('No connection from start!')


def next_step(map_: tp.List[str], position: Position, prev_position: Position) -> (int, dict):
    value = 1
    point_x_map = defaultdict(list)
    point_y_map = defaultdict(list)
    symbol = map_[position.y][position.x]
    point_y_map[prev_position.y].append(prev_position.x)
    while symbol != 'S':
        point_x_map[position.x].append(position.y)
        point_y_map[position.y].append(position.x)
        next_position = MOVES[symbol](position, prev_position)
        prev_position, position = position, next_position
        symbol = map_[position.y][position.x]
        value += 1

    return value, point_y_map


def calculate_inside_points(map_: tp.List[str], point_y_map: dict):
    value = 0
    map_y_size = len(map_)
    map_x_size = len(map_[0])
    for y in range(1, map_y_size-1):
        for x in range(1, map_x_size-1):
            if x in point_y_map[y]:
                continue

            lesser_x = [it for it in point_y_map[y] if x > it]
            bigger_x = [it for it in point_y_map[y] if x < it]
            if len(lesser_x) % 2 == 1 and len(bigger_x) % 2 == 1:
                value += 1
                print(x, y)
    return value



print(solution())