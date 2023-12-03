STRINGED_DIGITS = {'one': 1, 'two': 2, 'three': 3, 'four': 4,
                   'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def get_digit(line: str, rng: iter) -> str:
    for i in rng:
        for word, digit in STRINGED_DIGITS.items():
            if line[i:].startswith(word):
                return str(digit)

        if line[i].isnumeric():
            return line[i]

def extract_secret_number(line: str) -> int:
    s_num = get_digit(line, range(len(line)))
    s_num += get_digit(line, range(len(line) - 1, -1, -1))

    return int(s_num)


total: int = 0

with open('calibration.txt', 'r') as fd:
    while line := fd.readline():
        if not line:
            continue
        total += extract_secret_number(line)

print(total)
