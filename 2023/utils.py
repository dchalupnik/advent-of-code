import typing as tp


def next_line(number: int) -> tp.Generator[str, None, None]:
    with open(f'2023/input/{number}.txt') as file_:
        for line in file_:
            yield line.replace('\n', '')