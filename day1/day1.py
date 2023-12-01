import os


def part1():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    with open(filename) as file:
        sum = 0
        for row in file:
            digits = [char for char in row if char.isdigit()]
            sum += int(f'{digits[0]}{digits[-1]}')

    return sum


def part2():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    with open(filename) as file:
        sum = 0
        numbers = [
            'one',
            'two',
            'three',
            'four',
            'five',
            'six',
            'seven',
            'eight',
            'nine',
        ]

        for row in file:
            # First digit
            i = 0
            found = False
            match_count = {n: 0 for n in numbers}
            while i < len(row) and not found:
                c = row[i]
                if c.isdigit():
                    sum += 10*int(c)
                    found = True
                    break

                for val, n in enumerate(numbers, 1):
                    if c == n[match_count[n]]:
                        match_count[n] += 1
                        if match_count[n] == len(n):
                            sum += 10*val
                            found = True
                            break
                    elif c == n[0]:
                        match_count[n] = 1
                    else:
                        match_count[n] = 0
                i += 1

            # Second digit
            found = False
            match_count = {n: 0 for n in numbers}
            i = len(row) - 1
            while i >= 0 and not found:
                c = row[i]
                if c.isdigit():
                    sum += int(c)
                    found = True
                    break

                for val, n in enumerate(numbers, 1):
                    if c == n[len(n) - match_count[n] - 1]:
                        match_count[n] += 1
                        if match_count[n] == len(n):
                            sum += val
                            found = True
                            break
                    elif c == n[-1]:
                        match_count[n] = 1
                    else:
                        match_count[n] = 0
                i -= 1

        return sum


if __name__ == '__main__':
    print(part1())
    print(part2())
