import argparse
import csv

import utils


def team_games_in_week(st_date, end_date):
  """ Find out how many teams every team plays over a given time period """
  d_range = set(utils.date_range(st_date, end_date))

  with open('resources/2017_2018.csv', 'rU') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')

    team_counts = {}
    for row in reader:
      if row[0] in d_range:
        if row[1] not in team_counts:
          team_counts[row[1]] = 0
        team_counts[row[1]] += 1
        if row[2] not in team_counts:
          team_counts[row[2]] = 0
        team_counts[row[2]] += 1

    sorted_counts = sorted(team_counts.items(), key=lambda x: x[1], reverse=True)

    for team in sorted_counts:
      print '{}: {}'.format(team[0], team[1])


parser = argparse.ArgumentParser(description='Run some useful commands')
parser.add_argument('-s', '--start', help='The start date to count games for', required=True)
parser.add_argument('-e', '--end', help='The end date to count games for', required=True)
args = parser.parse_args()

try:
  team_games_in_week(args.start, args.end)
except ValueError:
  print '> ERROR: Invalid date format. Required format: "YYYY-MM-DD"'

