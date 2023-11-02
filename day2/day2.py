def part1():
    game = None
    with open("input.txt", "r") as f:
        game = f.readlines()

    wins = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    }
    draws = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }
    shape_score = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    res = 0
    for play in game:
        b1 = play[0]
        b2 = play[2]

        if wins[b1] == b2:
            res += 6 # win
        elif draws[b1] == b2:
            res += 3 # draw
        res += shape_score[b2]

    return res


def part2():
    game = None
    with open("input.txt", "r") as f:
        game = f.readlines()

    wins = {
        'A': 'Y',
        'B': 'Z',
        'C': 'X'
    }
    draws = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }
    loses = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    }
    output = {'X': loses, 'Y': draws, 'Z': wins }
    output_score = {'X': 0, 'Y': 3, 'Z': 6 }
    shape_score = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }

    res = 0
    for play in game:
        b1 = play[0]
        otp = play[2]

        res += output_score[otp]
        res += shape_score[output[otp][b1]]

    return res



if __name__ == "__main__":
    print(part1())
    print(part2())
