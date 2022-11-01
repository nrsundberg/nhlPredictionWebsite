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
# Create cursor in db
cursor = cnx.cursor()
# sql command to execute
sql_command = "SELECT * FROM player_statistics WHERE full_name = 'Brock Nelson'"
# actuall execution
cursor.execute(sql_command)
# fetch results of execution
myresult = cursor.fetchall()
# print coumns and rows of call
cursor.column_names
for rows in myresult:
  print(rows)
# close connection
cnx.close()

# # example query for info users
# import mysql.connector
# username = 'info'
# password = 'Islanders1!'
# database = 'nhlpredictions'
# server = 'nhlpredictions.mysql.database.azure.com'
# certif = 'assets\certFiles\DigiCertGlobalRootCA.crt.pem'
# # Connecting to mysql database
# cnx = mysql.connector.connect(user=username,
#  password=password, 
#  host=server, 
#  port=3306, database=database, 
#  ssl_ca=certif)
# print(cnx)
# # Create cursor in db
# cursor = cnx.cursor()
# # sql command to execute
# sql_command = "SELECT * FROM player_statistics WHERE full_name = 'Brock Nelson'"
# # actuall execution
# cursor.execute(sql_command)
# # fetch results of execution
# myresult = cursor.fetchall()
# # print coumns and rows of call
# cursor.column_names
# for rows in myresult:
#   print(rows)
# # close connection
# cnx.close()