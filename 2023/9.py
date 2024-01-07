from utils import next_line


def solution(reversed_=False):
    result = 0
    for line in next_line(9):
        numbers = parse_line(line, reversed_)
        result += numbers[-1]
        while sum(i != 0 for i in numbers) != 0:
            new_numbers = []
            for i in range(len(numbers)-1):
                new_numbers.append(numbers[i+1] - numbers[i])
            result += new_numbers[-1]
            numbers = new_numbers

    return result


def parse_line(line, reversed_=False):
    numbers = [int(it) for it in line.split(' ')]
    if reversed_:
        return numbers[::-1]
    return numbers


print(solution())
print(solution(reversed_=True))
