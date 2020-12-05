import adventofcode
import re

test_docs = [
    'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd',
    'byr:1937 iyr:2017 cid:147 hgt:183cm',
    '',
    'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884',
    'hcl:#cfa07d byr:1929',
    '',
    'hcl:#ae17e1 iyr:2013',
    'eyr:2024',
    'ecl:brn pid:760753108 byr:1931',
    'hgt:179cm',
    '',
    'hcl:#cfa07d eyr:2025 pid:166559648',
    'iyr:2011 ecl:brn hgt:59in',
]

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

def valid_doc_count(input):
    """
    >>> valid_doc_count(test_docs)
    2
    """
    total = 0
    docs = parse_docs(input)
    for doc in docs:
        if is_valid_doc(doc):
            total += 1
    return total

def valid_doc_count2(input):
    total = 0
    docs = parse_docs(input)
    for doc in docs:
        if is_valid_doc2(doc):
            total += 1
    return total

def parse_docs(input):
    docs = []
    doc = {}
    for line in input:
        if line == '':
            docs.append(doc)
            doc = {}
        fields = line.split()
        for field in fields:
            kv = field.split(':')
            doc[kv[0]] = kv[1]
    return docs

def is_valid_doc(doc):
    total = 0
    for field in required_fields:
        if field in doc:
            total += 1
    return total == 7

def is_valid_doc2(doc):
    """
    >>> is_valid_doc2({'eyr': '1972', 'cid': '100', 'hcl': '#18171d', 'ecl': 'amb', 'hgt': '170', 'pid': '186cm', 'iyr': '2018', 'byr': '1926'})
    False
    >>> is_valid_doc2({'iyr': '2019', 'hcl': '#602927', 'eyr': '1967', 'hgt': '170', 'ecl': 'grn', 'pid': '012533040', 'byr': '1946'})
    False
    >>> is_valid_doc2({'hcl': 'dab227', 'iyr': '2012', 'ecl': 'brn', 'hgt': '182cm', 'pid': '021572410', 'eyr': '2020', 'byr': '1992', 'cid': '277'})
    False
    >>> is_valid_doc2({'hgt': '59cm', 'ecl': 'zzz', 'eyr': '2038', 'hcl': '74454a', 'iyr': '2023', 'pid': '3556412378', 'byr': '2007'})
    False
    >>> is_valid_doc2({'pid': '087499704', 'hgt': '74in', 'ecl': 'grn', 'iyr': '2012', 'eyr': '2030', 'byr': '1980', 'hcl': '#623a2f'})
    True
    >>> is_valid_doc2({'eyr': '2029', 'ecl': 'blu', 'cid': '129', 'byr': '1989', 'iyr': '2014', 'pid': '896056539', 'hcl': '#a97842', 'hgt': '165cm'})
    True
    >>> is_valid_doc2({'hcl': '#888785', 'hgt': '164cm', 'byr': '2001', 'iyr': '2015', 'cid': '88', 'pid': '545766238', 'ecl': 'hzl', 'eyr': '2022'})
    True
    >>> is_valid_doc2({'iyr': '2010', 'hgt': '158cm', 'hcl': '#b6652a', 'ecl': 'blu', 'byr': '1944', 'eyr': '2021', 'pid': '093154719'})
    True
    """
    if is_valid_doc(doc):
        for field in doc.items():
            if not is_valid_field(field):
                return False
        return True
    return False

def is_valid_field(kv):
    if kv[0] == 'byr':
        return re.match(r'^\d{4}$', kv[1]) and int(kv[1]) >= 1920 and int(kv[1]) <= 2002
    if kv[0] == 'iyr':
        return re.match(r'^\d{4}$', kv[1]) and int(kv[1]) >= 2010 and int(kv[1]) <= 2020
    if kv[0] == 'eyr':
        return re.match(r'^\d{4}$', kv[1]) and int(kv[1]) >= 2020 and int(kv[1]) <= 2030
    if kv[0] == 'hgt':
        return (re.match(r'^\d{3}cm$', kv[1]) and int(kv[1][:3]) >= 150 and int(kv[1][:2]) <= 193) or (re.match(r'^\d{2}in$', kv[1]) and int(kv[1][:2]) >= 59 and int(kv[1][:2]) <= 76)
    if kv[0] == 'hcl':
        return re.match(r'^#[0-9a-f]{6}$', kv[1])
    if kv[0] == 'ecl':
        return re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', kv[1])
    if kv[0] == 'pid':
        return re.match(r'^\d{9}$', kv[1])
    if kv[0] == 'cid':
        return True
    return False

def main():
    puzzle_input = adventofcode.read_input(4)
    adventofcode.answer(1, 256, valid_doc_count(puzzle_input))
    adventofcode.answer(2, 198, valid_doc_count2(puzzle_input))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
