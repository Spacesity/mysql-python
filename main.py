import mysql.connector
import getpass
from mysql.connector import Error

commands = [
			"list-commands",
			"create-list",
			"view-list",
			"create-task",
			"remove-task"
		]

class Command():
	def view_commands():
		if command == "list-commands":
			for com in commands:
				print(com)
	def create_list():
		pass
	def view_list():
		if command == "view-list":
			cursor.execute("SELECT * FROM scores")
			rows = cursor.fetchall()
			for row in rows:
				print(row)
	def create_task():
		pass
	def remove_task():
		pass

host_input = str(input("Enter host name (localhost if on local device):"))
user_input = str(input("Enter user name:"))
password_input = str(getpass.getpass("Enter password:"))
database_input = str(input("Enter database name:"))

print("MySQL and Python Program - Type 'commands' to see all commands")
try:
	conn = mysql.connector.connect(
		host = host_input,
		user = user_input,
		password = password_input,
		database = database_input
	)
	
	if conn.is_connected():
		print("Connected to MySQL database")
		cursor = conn.cursor()
		while True:
			command = str(input("execute: ")).strip().lower() 	
			Command.view_commands()
			Command.create_list()
			Command.view_list()
			Command.create_task()
			Command.remove_task()
			if command == "exit":
				break
		cursor.close()
	else:
		print("Failed to connect to MySQL database")

except mysql.connector.Error as err:
	print("Error:", err)

finally:
	if conn.is_connected():
		conn.close()
		print("MySQL connection closed")
