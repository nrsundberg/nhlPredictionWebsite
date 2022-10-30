import mysql.connector
import assets.pyFiles.enviroment_info as prt_elem
username = 'noah'
password = prt_elem.mysql_password
database = 'nhlpredictions'
server = 'nhlpredictions.mysql.database.azure.com'
certif = 'assets/certFiles/BaltimoreCyberTrustRoot.crt.pem'
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