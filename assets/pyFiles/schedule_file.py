import enviroment_info
import requests
import pandas
nhlScheduleRequest = requests.get(f"https://api.sportradar.us/nhl/trial/v7/en/games/2022/REG/schedule.json?api_key={enviroment_info.api_key}")
nhlSchedule = nhlScheduleRequest.json()

schedule = pandas.DataFrame(columns = ['game_id','home_team_alias','home_team','away_team_alias','away_team','date', 'time_zone'])

for game in nhlSchedule['games']:
    row = []
    row.extend([game['id'], game['home']['alias'],game['home']['name'], game['away']['alias'], game['away']['name'], game['scheduled'], game['venue']['time_zone']])
    schedule.loc[len(schedule.index)] = row

schedule.to_csv('schedule.txt', index=False)