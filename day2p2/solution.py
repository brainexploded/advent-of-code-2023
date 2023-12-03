def parse_games(s: str) -> list:
    game_list = [game.strip().split(', ') for game in s.split('; ')]
     
    for i, rnd in enumerate(game_list):
        for j, case in enumerate(rnd):
            lst = case.split()
            game_list[i][j] = {'n': int(lst[0]), 'color': lst[1]}
            
    return game_list


def get_cubes_power(game : list) -> int:
    maxes = {
            'red': -1,
            'green': -1,
            'blue': -1,
            }
    for rnd in game:
        for case in rnd:
            if case['n'] > maxes[case['color']]:
                maxes[case['color']] = case['n']
    return maxes['red'] * maxes['green'] * maxes['blue']


total = 0

with open('games.txt', 'r') as fd:
    while line := fd.readline():
        if not line:
            continue

        header, game_str = line.split(': ')
        game_id = int(header.split()[-1])
        game = parse_games(game_str)

        total += get_cubes_power(game)
        
print(total)
# Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
