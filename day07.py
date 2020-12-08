import adventofcode
import re

test_rules = [
    'light red bags contain 1 bright white bag, 2 muted yellow bags.',
    'dark orange bags contain 3 bright white bags, 4 muted yellow bags.',
    'bright white bags contain 1 shiny gold bag.',
    'muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.',
    'shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.',
    'dark olive bags contain 3 faded blue bags, 4 dotted black bags.',
    'vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.',
    'faded blue bags contain no other bags.',
    'dotted black bags contain no other bags.'
]

class Bag:
    def __init__(self, name, bags):
        self.name = name
        self.bags = bags

def bag_color_count(rules):
    """
    >>> bag_color_count(test_rules)
    4
    """
    count = 0
    bag_list = parse_bags(rules)
    for bag in bag_list:
        if has_shiny(bag, bag_list):
            count += 1
    return count

def shiny_gold_count(rules):
    """
    >>> shiny_gold_count(test_rules2)
    32
    """
    count = 0
    bag_list = parse_bags(rules)
    gold = next((x for x in bag_list if x.name == 'shiny gold'), None)
    for bag in gold.bags:
        count += (bag[0] + (bag[0] * count_bags(bag, bag_list)))
    return count

def count_bags(bag, bag_list):
    count = 0
    a = next((x for x in bag_list if x.name == bag[1]), None)
    if len(a.bags) == 0:
        return 0
    for b in a.bags:
        count += (b[0] + b[0] * count_bags(b, bag_list))
    return count

def has_shiny(bag, bag_list):
    result = False
    if len(bag.bags) == 0:
        return False
    for b in bag.bags:
        if b[1] == 'shiny gold':
            return True
        a = next((x for x in bag_list if x.name == b[1]), None)
        result |= has_shiny(a, bag_list)
    return result

def parse_bags(rules):
    bag_list = []
    for line in rules:
        line = re.sub(r' bags?', '', line[:-1])
        info = re.split(r' contain |, ', line)
        if info[1] == 'no other':
            bag_list.append(Bag(info[0], []))
        else:
            sub_list = []
            for i in range(len(info)-1):
                s = info[i+1].split(' ', 1)
                sub_list.append((int(s[0]), s[1]))
            bag_list.append(Bag(info[0], sub_list))     
    return bag_list

def main():
    puzzle_input = adventofcode.read_input(7)
    adventofcode.answer(1, 272, bag_color_count(puzzle_input))
    adventofcode.answer(2, 172246, shiny_gold_count(puzzle_input))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
