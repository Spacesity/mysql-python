import mysql.connector
from mysql.connector import Error

commands = {
	"all" : "SELECT * FROM scores"
}
print("MySQL and Python Program - Type 'commands' to see all commands")

try:
	conn = mysql.connector.connect(
		host="localhost",
		user="lucas",
		password="6969",
		database="test"
	)
	
	if conn.is_connected():
		print("Connected to MySQL database")
		cursor = conn.cursor()
		while True:
			command = str(input("execute: ")).strip().lower() 	
			if command == "all":
				cursor.execute("SELECT * FROM scores")
				rows = cursor.fetchall()
				for row in rows:
					print(row)
			elif command == "exit":
				break
			else:
				print("error: unknown command")
		cursor.close()
	else:
		print("Failed to connect to MySQL database")

except mysql.connector.Error as err:
	print("Error: ", err)

finally:
	if conn.is_connected():
		conn.close()
		print("MySQL connection closed")

