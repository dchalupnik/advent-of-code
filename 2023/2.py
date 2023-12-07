import typing as tp
from dataclasses import dataclass

from utils import next_line

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


@dataclass
class Turn:
    red: int = 0
    blue: int = 0
    green: int = 0


@dataclass
class Game:
    id: int
    turns: tp.List[Turn]


def parse_turn(turn: str) -> Turn:
    """Transform turn string into turn object."""
    cube_colors = {}
    for cube in turn.split(', '):
        count, color = cube.split(' ')
        cube_colors[color] = int(count)

    return Turn(**cube_colors)


def parse_game(line: str) -> Game:
    """Transform game string into game object."""
    game_id, turns = line.split(': ')
    _, game_id = game_id.split(' ')
    return Game(
       id=int(game_id),
       turns=[parse_turn(it) for it in turns.split('; ')]
    )


def validate_game(game: Game) -> bool:
    """Check if game is valid."""
    for turn in game.turns:
        if turn.red > MAX_RED or turn.blue > MAX_BLUE or turn.green > MAX_GREEN:
            return False

    return True


def calculate_game_power(game: Game) -> int:
    """Calculate game power witch indicate desired result"""
    max_green, max_blue, max_red = [0] * 3
    for turn in game.turns:
        if turn.red > max_red:
            max_red = turn.red
        if turn.blue > max_blue:
            max_blue = turn.blue
        if turn.green > max_green:
            max_green = turn.green

    return max_green * max_blue * max_red


def solution():
    power = 0
    for line in next_line(2):
        game = parse_game(line)
        power += calculate_game_power(game)

    return power


print(solution())