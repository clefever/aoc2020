import adventofcode

test_answers = [
    'abc',
    '',
    'a',
    'b',
    'c',
    '',
    'ab',
    'ac',
    '',
    'a',
    'a',
    'a',
    'a',
    '',
    'b',
]

def answer_sum(answers):
    """
    >>> answer_sum(test_answers)
    11
    """
    ans = parse_answers(answers)
    return sum(len(a) for a in ans)

def answer_sum2(answers):
    """
    >>> answer_sum2(test_answers)
    6
    """
    ans = parse_answers2(answers)
    count = 0
    for a in ans:
        for d in a[0].values():
            if d == a[1]:
                count += 1
    return count


def parse_answers(input):
    docs = []
    doc = set()
    for line in input:
        if line == '':
            docs.append(doc)
            doc = set()
        for ans in line:
            doc.add(ans)
    docs.append(doc)
    return docs

def parse_answers2(input):
    docs = []
    num = 0
    doc = {}
    for line in input:
        if line == '':
            docs.append((doc, num))
            num = 0
            doc = {}
        else:
            num += 1
        for ans in line:
            if ans not in doc.keys():
                doc[ans] = 1
            else:
                doc[ans] += 1
    docs.append((doc, num))
    return docs

def main():
    puzzle_input = adventofcode.read_input(6)
    adventofcode.answer(1, 7110, answer_sum(puzzle_input))
    adventofcode.answer(2, 3628, answer_sum2(puzzle_input))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
