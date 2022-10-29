import enviroment_info
import requests
import pandas
nhlStandingsRequest = requests.get(f"https://api.sportradar.us/nhl/trial/v7/en/seasons/2022/REG/standings.json?api_key={enviroment_info.api_key}")
nhlStandings = nhlStandingsRequest.json()
conference = nhlStandings['conferences']
western_conference_teams = conference[0]['divisions']
pacific_western_conference_teams = western_conference_teams[0]['teams'] 
central_western_conference_teams = western_conference_teams[1]['teams'] 
eastern_conference_teams = conference[1]['divisions']
metropolitan_eastern_conference_teams = eastern_conference_teams[0]['teams']
atlantic_eastern_conference_teams = eastern_conference_teams[1]['teams']
teams = pacific_western_conference_teams + central_western_conference_teams + metropolitan_eastern_conference_teams + atlantic_eastern_conference_teams
standings = {}
for item in teams:
    for record_type in item['records']:
        if record_type['record_type'] == 'home':
            home = record_type  
            home_list = [home['wins'],
                        home['losses'],
                        home['win_pct'],
                        home['points'],
                        home['goals_for'],
                        home['goals_against']]
    for record_type in item['records']:
        if record_type['record_type'] == 'road':
            road = record_type  
            road_list = [road['wins'],
                        road['losses'],
                        road['win_pct'],
                        road['points'],
                        road['goals_for'],
                        road['goals_against']]
    info_dict = []
    info_dict.append(item['id'])
    info_dict.append(item['games_played'])
    info_dict.append(item['wins'])
    info_dict.append(item['losses'])
    info_dict.append(item['win_pct'])
    info_dict.append(item['points'])
    info_dict.append(item['goals_for'])
    info_dict.append(item['goals_against'])
    info_dict.extend(home_list)
    info_dict.extend(road_list)
    info_dict.append(item['rank']['division'])
    info_dict.append(item['rank']['conference'])
    standings[item['name']] = info_dict
df = pandas.DataFrame(columns=['team_name','id','games_played','wins','losses','win_pct','points','goals_for','goals_against',
                                'home_wins','home_losses','home_win_pct','home_points','home_goals_for','home_goals_against',
                                'road_wins','road_losses','road_win_pct','road_points','road_goals_for','road_goals_against',
                                'division_rank','conference_rank'])
for key in standings.keys():
    row = []
    row.append(key)
    row.extend(standings[key])
    df.loc[len(df.index)] = row

df.to_csv('standings.txt', index = False)

df['id'].to_csv('team_id.txt', index = False)