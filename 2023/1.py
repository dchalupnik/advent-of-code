from utils import next_line

TRANSLATION = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6.txt',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
R_TRANSLATION = {key[::-1]: value for key, value in TRANSLATION.items()}


def find_first_digit(n: int, line: str, translation_: dict) -> str:
    """Find first digit or word describing digit in line"""
    translation_keys = translation_.keys()
    for i in range(n):
        if line[i].isdigit():
            return line[i]
        else:
            for translation_key in translation_keys:
                if line[i:].startswith(translation_key):
                    return translation_[translation_key]


def solution() -> int:
    result = 0
    for line in next_line(1):
        n = len(line)
        left = find_first_digit(n, line, TRANSLATION)
        right = find_first_digit(n, line[::-1], R_TRANSLATION)
        result += int(left + right)

    return result


print(solution())
