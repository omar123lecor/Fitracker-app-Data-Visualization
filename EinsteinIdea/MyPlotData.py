import time

import mysql.connector
conn = mysql.connector.connect(
	user='root',
	host='localhost',
	database='fittracker',
	passwd='omar123Lecor'
)
cursor = conn.cursor(buffered=True)
def plotdata(username,date):
	day = date.split()
	if len(day[2]) == 1:
		choice = day[0] + ' ' + day[1] + '  ' + day[2]
	else:
		choice = day[0] + ' ' + day[1] + ' ' + day[2]
	year = day[4]
	cursor.execute(
		f"select sum(protein),sum(fats),sum(carbs),sum(calories) from foodcont where username=%s and times like '%{choice}%' and times like'%{year}%'",[username])
	response = cursor.fetchone()
	return [response[0],response[1],response[2],response[3]]
print(plotdata('omar',time.ctime()))