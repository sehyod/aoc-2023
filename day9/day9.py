import os
import re


def derivative(seq):
    return [e2 - e1 for e1, e2 in zip(seq, seq[1:])]


def part1():
    sequences: list[list[int]] = []

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    with open(filename) as f:
        for r in f:
            sequences.append([int(n) for n in re.findall(r'-?\d+', r)])

    def predict_next(seq):
        if all(e == seq[0] for e in seq):
            return seq[0]
        else:
            return seq[-1] + predict_next(derivative(seq))

    return sum([predict_next(seq) for seq in sequences])


def part2():
    sequences: list[list[int]] = []

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    with open(filename) as f:
        for r in f:
            sequences.append([int(n) for n in re.findall(r'-?\d+', r)])

    def predict_previous(seq):
        if all(e == seq[0] for e in seq):
            return seq[0]
        else:
            return seq[0] - predict_previous(derivative(seq))

    return sum([predict_previous(seq) for seq in sequences])


if __name__ == '__main__':
    print(part1())
    print(part2())
