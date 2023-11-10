
class Monkey:
    def __init__(self, items, op, test, divider=None, rcvs=None):
        if rcvs is None:
            rcvs = []
        self.items = items
        self.op = op
        self.test = test
        self.insp = 0
        self.divider = divider
        self.rcvs = rcvs

    def __str__(self):
        return self.insp.__str__()

    def send(self, item, monkeys_dict):
        if self.test(item):
            monkeys_dict[self.rcvs[0]].items.append(item)
        else:
            monkeys_dict[self.rcvs[1]].items.append(item)
        self.insp += 1

def print_monkeys(monkeys_dict):
    print("====================================")
    for m in monkeys_dict.values():
        print(m)

def part1(monkeys_dict):
    for i in range(1, 21):
        for m in monkeys_dict.values():
            while m.items:
                item = m.items.pop(0)
                new_item = m.op(item)
                new_item = new_item // 3
                m.send(new_item, monkeys_dict)

    monkeys = list(monkeys_dict.values())
    monkeys.sort(key = lambda m: m.insp, reverse=True)

    return monkeys[0].insp * monkeys[1].insp

def part2(monkeys_dict):
    divider = 1
    for m in monkeys_dict.values():
        divider *= m.divider

    for i in range(1, 10_000 + 1):
        for m in monkeys_dict.values():
            while m.items:
                item = m.items.pop(0)
                new_item = m.op(item)
                new_item = new_item % divider
                m.send(new_item, monkeys_dict)

    monkeys = list(monkeys_dict.values())
    monkeys.sort(key = lambda m: m.insp, reverse=True)

    return monkeys[0].insp * monkeys[1].insp

if __name__ == "__main__":
    monkeys_dict_1 = {
        0: Monkey(items = [98, 89, 52], op = lambda old: old * 2, test = lambda new: new % 5 == 0, rcvs = [6, 1]),
        1: Monkey(items = [57, 95, 80, 92, 57, 78], op = lambda old: old * 13, test = lambda new: new % 2 == 0, rcvs = [2, 6]),
        2: Monkey(items = [82, 74, 97, 75, 51, 92, 83], op = lambda old: old + 5, test = lambda new: new % 19 == 0, rcvs = [7, 5]),
        3: Monkey(items = [97, 88, 51, 68, 76], op = lambda old: old + 6, test = lambda new: new % 7 == 0, rcvs = [0, 4]),
        4: Monkey(items = [63], op = lambda old: old + 1, test = lambda new: new % 17 == 0, rcvs = [0, 1]),
        5: Monkey(items = [94, 91, 51, 63], op = lambda old: old +  4, test = lambda new: new % 13 == 0, rcvs = [4, 3]),
        6: Monkey(items = [61, 54, 94, 71, 74, 68, 98, 83], op = lambda old: old + 2, test = lambda new: new % 3 == 0, rcvs = [2, 7]),
        7: Monkey(items = [90, 56], op = lambda old: old * old, test = lambda new: new % 11 == 0, rcvs = [3, 5])
    }
    print(part1(monkeys_dict_1))

    monkeys_dict_2 = {
        0: Monkey(items = [98, 89, 52], op = lambda old: old * 2, test = lambda new: new % 5 == 0, divider=5, rcvs = [6, 1]),
        1: Monkey(items = [57, 95, 80, 92, 57, 78], op = lambda old: old * 13, test = lambda new: new % 2 == 0, divider=2, rcvs = [2, 6]),
        2: Monkey(items = [82, 74, 97, 75, 51, 92, 83], op = lambda old: old + 5, test = lambda new: new % 19 == 0, divider=19, rcvs = [7, 5]),
        3: Monkey(items = [97, 88, 51, 68, 76], op = lambda old: old + 6, test = lambda new: new % 7 == 0, divider=7, rcvs = [0, 4]),
        4: Monkey(items = [63], op = lambda old: old + 1, test = lambda new: new % 17 == 0, divider=17, rcvs = [0, 1]),
        5: Monkey(items = [94, 91, 51, 63], op = lambda old: old +  4, test = lambda new: new % 13 == 0, divider=13, rcvs = [4, 3]),
        6: Monkey(items = [61, 54, 94, 71, 74, 68, 98, 83], op = lambda old: old + 2, test = lambda new: new % 3 == 0, divider=3, rcvs = [2, 7]),
        7: Monkey(items = [90, 56], op = lambda old: old * old, test = lambda new: new % 11 == 0, divider=11, rcvs = [3, 5])
    }
    print(part2(monkeys_dict_2))