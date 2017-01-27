import csv

import utils


# Find out how many teams every team plays over a given time period
def team_games_in_week(st_date, end_date):
  d_range = set(utils.date_range(st_date, end_date))

  with open('resources/nhl_schedule.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    team_counts = {}
    for row in reader:
      if row[0] in d_range:
        if row[1] not in team_counts:
          team_counts[row[1]] = 0
        team_counts[row[1]] += 1
        if row[3] not in team_counts:
          team_counts[row[3]] = 0
        team_counts[row[3]] += 1

    sorted_counts = sorted(team_counts.items(), key=lambda x: x[1], reverse=True)

    for team in sorted_counts:
      print '{}: {}'.format(team[0], team[1])

team_games_in_week('2017-01-31', '2017-02-05')
