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
game_id = ''
url = f"https://api.sportradar.us/nhl/trial/v7/en/games/{game_id}/summary.json?api_key={private.api_key}"
nhlGameRequest = requests.get(url)
nhlGame = nhlGameRequest.json()
# Create game pull to get each game from yesterday and parse it down to files that can update current files