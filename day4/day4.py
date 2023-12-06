import os
import re


def part1():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    s = 0

    with open(filename) as f:
        for r in f:
            _, numbers = r.strip().split(': ')
            winning_numbers, user_numbers = numbers.split(' | ')
            winning_numbers = re.findall(r'\d+', winning_numbers)
            user_numbers = re.findall(r'\d+', user_numbers)
            user_winning_numbers_count = sum(
                [n in winning_numbers for n in user_numbers])
            if user_winning_numbers_count > 0:
                s += 1 << (user_winning_numbers_count - 1)

    return s


def part2():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')

    cards_winnings = []

    with open(filename) as f:
        for r in f:
            _, numbers = r.strip().split(': ')
            winning_numbers, user_numbers = numbers.split(' | ')
            winning_numbers = re.findall(r'\d+', winning_numbers)
            user_numbers = re.findall(r'\d+', user_numbers)
            user_winning_numbers_count = sum(
                [n in winning_numbers for n in user_numbers])
            cards_winnings.append(user_winning_numbers_count)

    memo: list[int | None] = [None]*len(cards_winnings)

    # def total_cards(card_index: int) -> int:
    #     if memo[card_index] is not None:
    #         return memo[card_index]
    #     memo[card_index] = 1 + sum([total_cards(card_index + c)
    #                                 for c in range(cards_winnings[card_index])])
    #     return memo[card_index]
    for card_index in range(len(cards_winnings) - 1, -1, -1):
        memo[card_index] = 1 + sum([memo[card_index + 1 + i]
                                    for i in range(cards_winnings[card_index])])

    return sum(memo)


if __name__ == '__main__':
    print(part1())
    print(part2())
