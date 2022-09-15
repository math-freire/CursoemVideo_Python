player = {'name': input('Name: ')}
games = int(input('How many games did you play? '))
goals = []
[goals.append(int(input(f'Goals in the #{i+1} game: '))) for i in range(0, games)]
player['score'] = goals
player['total'] = sum(goals)
print('-='*20)

print(player)
print(f"{player['name']} played {games} games and scored {player['total']} goals.")
[print(f"    => In game {i+1}, did {player['score'][i]} goals.") for i in range(0, games)]
