COLORS = {
        'red': 12,
        'green': 13,
        'blue': 14,
        }

def parse_games(s: str) -> list:
    game_list = [game.strip().split(', ') for game in s.split('; ')]
     
    for i, rnd in enumerate(game_list):
        for j, case in enumerate(rnd):
            lst = case.split()
            game_list[i][j] = {'n': int(lst[0]), 'color': lst[1]}
            
    return game_list


def is_game_possible(game : list) -> bool:
    for rnd in game:
        for case in rnd:
            if case['n'] > COLORS[case['color']]:
                return False
    return True


total = 0

with open('games.txt', 'r') as fd:
    while line := fd.readline():
        if not line:
            continue

        header, game_str = line.split(': ')
        game_id = int(header.split()[-1])
        game = parse_games(game_str)

        if is_game_possible(game):
            total += game_id
        
print(total)
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
