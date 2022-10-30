import enviroment_info
import requests
import pandas
import csv
import time
team_id_list = []
with open("flatFiles/team_id.txt", 'r') as file:
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
    time.sleep(2)mlk 'uitg ;iutg;kiug'lkjbasfwcasvfq
team_dataframe.to_csv('team.txt', index=False)

# # create list of all player_ids pulled from team api call
# player_id_list = []
# for id_list in team_dataframe['player_id_list']:  
# # list of player info from first object in JSON
# player_info = ['id','full_name','status','height','weight','handedness','position','primary_position','jersey_number']
# # data frame that will fill out with every player -- last column is a list of regular season  211211212121
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
import pandas
import csv
player_list_all = []
with open("flatFiles/player.txt", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        player_list_all.extend(row)
# long player dataframe to write out and make into table in SQL\
# need to change columns when identified which items are being saved
full_player_dataframe = pandas.DataFrame(columns=['id','full_name','status','height','weight','handedness','position','primary_position','jersey_number','year'])
# player elements to repeat for every season are 0:9
player_list_all[0:9]
# player element to decompose 9:10
# make dictionary from string object
dict_play = eval(player_list_all[9:10][0])
# for each key
dict_play[0].keys()
player_seasonal_stats = pandas.DataFrame(columns=['year', 'alias', 'games_played', 'goals', 'assists', 'penalties', 'penalty_minutes', 'shots', 'blocked_att', 'missed_shots', 'hits', 'giveaways', 'takeaways',
                                                    'blocked_shots', 'faceoffs_won', 'faceoffs_lost', 'faceoff_win_pct'])
# need to figure out which element we want for each season
for player_season in dict_pla


   son]
    player_seasonal_stats.append(player_season)
# write out to csv when all info in dataframe
full_player_dataframe.to_csv('player.txt', index=False)

dict_play[0][2015]



