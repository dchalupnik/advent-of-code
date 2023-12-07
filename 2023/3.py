import typing as tp
from dataclasses import dataclass

from utils import next_line


@dataclass
class Matrix:
    matrix: tp.List[str]
    length: int
    size: int


@dataclass
class Number:
    value: str
    length: int
    end_i: int
    end_j: int


def solution() -> int:
    matrix = create_matrix()
    return sum(number for number in find_numbers(matrix))


def create_matrix() -> Matrix:
    """Build Matrix object from file data"""
    matrix = []
    for line in next_line(3):
        matrix.append(line)

    return Matrix(matrix=matrix, length=len(matrix[0]), size=len(matrix))


def find_numbers(matrix: Matrix) -> tp.Generator[str, None, None]:
    """Find all numbers that have allowed sign neighbour"""
    for j, row in enumerate(matrix.matrix):
        number = ''
        for i in range(matrix.length):
            if row[i].isdigit():
                number += row[i]
            else:
                if number and is_valid_number(matrix, Number(value=number, length=len(number), end_j=j, end_i=i-1)):
                    yield int(number)
                number = ''


def is_valid_number(matrix: Matrix, number: Number) -> bool:
    """Check if number has any neighbour"""
    # check front:
    position = number.end_i - number.length
    if position > 0:
        if _is_valid_sign(matrix.matrix[number.end_j][position]):
            return True

    # check back:
    position = number.end_i + 1
    if position < matrix.size:
        if _is_valid_sign(matrix.matrix[number.end_j][position]):
            return True

    # check top
    position = number.end_j - 1
    if position > 0:
        if check_different_row(matrix, number, position):
            return True

    # check bottom
    position = number.end_j + 1
    if position < matrix.length:
        if check_different_row(matrix, number, position):
            return True

    return False


def check_different_row(matrix: Matrix, number: Number, i: int) -> bool:
    """Check different row to find out sign"""
    for j in range(number.end_i - number.length, number.end_i + 2):
        if j > -1 and j < matrix.length:
            if _is_valid_sign(matrix.matrix[i][j]):
                return True

    return False


def _is_valid_sign(char: str):
    """Check if char is allowed sign"""
    return not char.isdigit() and char != '.'


print(solution())
