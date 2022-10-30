import enviroment_info
import requests
import pandas
import csv
import time
team_id_list = []
with open("assets/flatFiles/team_id.txt", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        team_id_list.extend(row)
team_id = ""
team_dataframe = pandas.DataFrame(columns=['id','name','alias','conference','conference_alias','division','division_alias','player_id_list'])

for team in team_id_list:
    team_id = team
    url = f"https://api.sportradar.us/nhl/trial/v7/en/teams/{team_id}/profile.json?api_key={enviroment_info.api_key}"
    nhlTeamRequest = requests.get(url)
    nhlTeam = nhlTeamRequest.json()
    row = []
    row.extend([nhlTeam['id'],
                nhlTeam['name'],
                nhlTeam['alias'],
                nhlTeam['conference']['name'],
                nhlTeam['conference']['alias'],
                nhlTeam['division']['name'],
                nhlTeam['division']['alias']])
    player_list = []
    for players in nhlTeam['players']:
        player_list.append(players['id'])
    row.append(player_list)
    team_dataframe.loc[len(team_dataframe.index)] = row
    time.sleep(2)
team_dataframe.to_csv('team.txt', index=False)

# # create list of all player_ids pulled from team api call
# player_id_list = []
# for id_list in team_dataframe['player_id_list']:
#     for ids in id_list:
#         player_id_list.append(ids)
# # list of player info from first object in JSON
# player_info = ['id','full_name','status','height','weight','handedness','position','primary_position','jersey_number']
# # data frame that will fill out with every player -- last column is a list of regular season stats
# player_dataframe = pandas.DataFrame(columns=['id','full_name','status','height','weight','handedness','position','primary_position','jersey_number','seasons_teams'])
# # loop through each player and pull from API -- API monthly calls max at 1,000 and there are 808 players in the NHL -- dont run code unless on new API key
# for player in player_id_list:
#     player_full_info_list = []
#     player_id_url = player
#     url = f"https://api.sportradar.us/nhl/trial/v7/en/players/{player_id_url}/profile.json?api_key={enviroment_info.api_key}"
#     nhlPlayerRequest = requests.get(url)
#     nhlPlayer = nhlPlayerRequest.json()
#     for info_item in player_info:
#         player_full_info_list.append(nhlPlayer[info_item])
#     player_team_dict = {}
#     # some players dont have seasons listed in their JSON so this gets around that
#     try:
#         for season in nhlPlayer['seasons']:
#             teams_list = []
#             if season['type'] == 'REG':
#                 year = season['year']
#                 for teams in season['teams']:
#                     teams_list.append(teams)
#                 player_team_dict[year] = teams_list 
#         player_full_info_list.append([player_team_dict])
#     except:
#         player_full_info_list.append("no season data")
#     player_dataframe.loc[len(player_dataframe.index)] = player_full_info_list
#     # API only allows one call per second
#     time.sleep(1)
# # Write to csv so anyone can load after inital pull
# player_dataframe.to_csv('player.txt', index=False)

# uncomment two import statements and can run below for decomp of file from above without needing to run above
# import pandas
# import csv
player_list_all = []
with open("assets/flatFiles/player.txt", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        player_list_all.extend(row)

# long player dataframe to write out and make into table in SQL
stat_info_list = ['games_played', 'goals', 'assists', 'penalties', 'penalty_minutes', 'shots', 'blocked_att', 'missed_shots', 'hits', 'giveaways', 'takeaways',
                                                    'blocked_shots', 'faceoffs_won', 'faceoffs_lost', 'faceoff_win_pct']
player_seasonal_stats = pandas.DataFrame(columns=['id','full_name','status','height','weight','handedness','position','primary_position','jersey_number','year',
                                                     'alias', 'games_played', 'goals', 'assists', 'penalties', 'penalty_minutes', 'shots', 'blocked_att', 'missed_shots', 'hits', 'giveaways', 'takeaways',
                                                    'blocked_shots', 'faceoffs_won', 'faceoffs_lost', 'faceoff_win_pct'])
j = 0
i = range(10, 8090, 10)
for val in i:
    try:
        dict_play = eval(player_list_all[val - 1 : val][0])
        fill_info = player_list_all[j : val - 1]
        for player_season in dict_play[0].keys():
            fill_info = fill_info[0:9]
            fill_info.append(player_season)
            fill_info.append(dict_play[0][player_season][0]['alias'])
            for item in stat_info_list:
                fill_info.append(dict_play[0][player_season][0]['statistics']['total'][item])
            player_seasonal_stats.loc[len(player_seasonal_stats.index)] = fill_info
        j += 10 
    except:
        j += 10
# write out to csv when all info in dataframe
player_seasonal_stats.to_csv('player.csv', index=False)