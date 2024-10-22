team_1 = 'Мастера кода'
team_2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

print('В команде %s участников: %s! \n'
      'В команде %s участников: %s! \n'
      'Итого сегодня в командах участников: %s и %s!'
      % (team_1, team1_num, team_2, team2_num, team1_num, team2_num))

print('Команда {team_1} решила задач: {score_1}! \n'
      '{team_1} решили задачи за {team1_time} с! \n'
      'Команда {team_2} решила задач: {score_2}! \n'
      '{team_2} решили задачи за {team2_time} с!'.
      format(team_1 = 'Мастера кода', team_2 = 'Волшебники данных',
             score_1 = 40, score_2 = 42,
             team1_time = 1552.512, team2_time = 2153.31451))

print(f'Команды решили {score_1} и {score_2} задач')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = f"Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = f"Победа команды Волшебники Данных!"
else:
    result = f"Ничья!"
challenge_result = result

print(challenge_result)