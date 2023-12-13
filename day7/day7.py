import os


def score_aux(hand, cards):
    s = 0
    for c in hand:
        s *= 100
        s += cards.index(c)
    return s


def part1():
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    def score(hand):
        uniq_cards = set(hand)
        card_counts = sorted([hand.count(c) for c in uniq_cards], reverse=True)
        match card_counts:
            case [5]:
                return 60000000000 + score_aux(hand, cards)
            case [4, 1]:
                return 50000000000 + score_aux(hand, cards)
            case [3, 2]:
                return 40000000000 + score_aux(hand, cards)
            case [3, 1, 1]:
                return 30000000000 + score_aux(hand, cards)
            case [2, 2, 1]:
                return 20000000000 + score_aux(hand, cards)
            case [2, 1, 1, 1]:
                return 10000000000 + score_aux(hand, cards)
            case _:
                return score_aux(hand, cards)

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')
    game = []

    with open(filename) as f:
        for r in f:
            hand, bid = r.strip().split()
            game.append(([*hand], int(bid)))

    game.sort(key=lambda x: score(x[0]))

    return sum([bid*(i + 1) for i, (_, bid) in enumerate(game)])


def part2():
    cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

    def score(hand):
        jokers = hand.count('J')
        uniq_cards = set(hand) - set(['J'])
        max_count = max([cards.count(c) for c in uniq_cards] or [0])
        card_counts = sorted([hand.count(c) for c in uniq_cards], reverse=True)
        if len(card_counts) == 0:
            card_counts = [jokers]
        else:
            card_counts[0] += jokers

        match card_counts:
            case [5]:
                return 60000000000 + score_aux(hand, cards)
            case [4, 1]:
                return 50000000000 + score_aux(hand, cards)
            case [3, 2]:
                return 40000000000 + score_aux(hand, cards)
            case [3, 1, 1]:
                return 30000000000 + score_aux(hand, cards)
            case [2, 2, 1]:
                return 20000000000 + score_aux(hand, cards)
            case [2, 1, 1, 1]:
                return 10000000000 + score_aux(hand, cards)
            case _:
                return score_aux(hand, cards)

    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'input.txt')
    game = []

    with open(filename) as f:
        for r in f:
            hand, bid = r.strip().split()
            game.append(([*hand], int(bid)))

    game.sort(key=lambda x: score(x[0]))

    return sum([bid*(i + 1) for i, (_, bid) in enumerate(game)])


if __name__ == '__main__':
    print(part1())
    print(part2())
