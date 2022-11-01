import mysql.connector
import assets.pyFiles.enviroment_info as private
username = 'noah'
password = private.mysql_password
database = 'nhlpredictions'
server = 'nhlpredictions.mysql.database.azure.com'
certif = 'assets\certFiles\DigiCertGlobalRootCA.crt.pem'
# Connecting to mysql database
cnx = mysql.connector.connect(user=username,
 password=password, 
 host=server, 
 port=3306, database=database, 
 ssl_ca=certif)
print(cnx)
cursor = cnx.cursor()

sql_command = "SELECT * FROM player_statistics WHERE full_name = 'Brock Nelson'"
sql_command = "SELECT * FROM player_statistics"
cursor.execute(sql_command)
myresult = cursor.fetchall()
for x in myresult:
  print(x)

# Run before closing file
cnx.close()


import assets.pyFiles.enviroment_info as private
import requests
# get list of game id's -- most likely query from schedule db
game_id = '06fc4032-ebb9-4618-890c-dff93c80212a'
url = f"https://api.sportradar.us/nhl/trial/v7/en/games/{game_id}/summary.json?api_key={private.api_key}"
nhlGameRequest = requests.get(url)
nhlGame = nhlGameRequest.json()
# Create game pull to get each game from yesterday and parse it down to files that can update current files

nhlGame.keys()

for key in nhlGame.keys():
  print(key)
  try:
    for keys in nhlGame[key].keys():
      print(keys)
  except:
    next
nhlGame['home'].keys()
home_info = ['name', 'points','scoring']
# need to get each value from keys
nhlGame['home']['statistics'].keys()
statistics_info = ['total', 'powerplay', 'shorthanded', 'evenstrength', 'penalty']
for key in statistics_info:
  print(key)
  print(nhlGame['home']['statistics'][key].keys())
# need to get each value from keys
nhlGame['home']['goaltending'].keys()
# value 0 is a loop for each element in list of players
nhlGame['home']['players'][0].keys()
#  no sub keys for period -- rest have subs and are terminal
nhlGame['home']['players'][0]['statistics'].keys()
# no sub keys -- terminal key
nhlGame['home']['players'][0]['time_on_ice'].keys()
