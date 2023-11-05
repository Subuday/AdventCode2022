
def part1(window_size=4):
    signal = None
    with open("input.txt", "r") as f:
        signal = list(map(lambda s: s.strip(), f.readlines()))[0]

    l = 0
    r = 0
    counter = {}

    while r < window_size:
        counter[signal[r]] = counter.get(signal[r], 0) + 1
        r += 1

    if len(counter) == window_size:
        return window_size

    while r < len(signal):
        counter[signal[l]] -= 1
        if counter[signal[l]] == 0:
            del counter[signal[l]]
        l += 1

        counter[signal[r]] = counter.get(signal[r], 0) + 1
        r += 1

        if len(counter) == window_size:
            return r

    return -1

def part2():
    return part1(window_size=14)

if __name__ == "__main__":
    print(part1())
    print(part2())