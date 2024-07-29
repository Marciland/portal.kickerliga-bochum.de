import csv
from io import TextIOWrapper
from models import TeamModel


def dump_team_to_file(team: TeamModel, file: TextIOWrapper):
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['Number', 'Name', 'Positions', 'Teams',
                    'Leagues', 'Seasons', 'Nationality'])
    for index, player in enumerate(team.get_full_team()):
        writer.writerow([index, player, '', team.name,
                         '', '', ''])
