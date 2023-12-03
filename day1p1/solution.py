def find_first_digit(s: str) -> str:
    for symbol in s:
        if symbol.isnumeric():
            return symbol


def extract_secret_number(line: str) -> int:
    return int(find_first_digit(line) + find_first_digit(reversed(line)))

total: int = 0

with open('calibration.txt', 'r') as fd:
    while line := fd.readline():
        total += extract_secret_number(line)

print(total)
