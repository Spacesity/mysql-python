import mysql.connector
import getpass

commands = [
	"list-commands",
	"create-list",
	"view-list",
	"create-task",
	"remove-task"
]

class Command():
	def view_commands():
		if command == commands[0]:
			for com in commands:
				print(com)
	def create_list():
		if command == commands[1]:
			list_name = str(input("Enter new list name:"))
			list_creation = f"CREATE TABLE {list_name} (task int, description varchar(200))"
			cursor.execute(list_creation)
	def view_list():
		if command == commands[2]:
			list_view = f"SELECT * FROM {database_input}"
			cursor.execute(list_view)
			rows = cursor.fetchall()
			for row in rows:
				print(row)
	def create_task():
		if command == commands[3]:
			pass
	def remove_task():
		if command == commands[4]:
			pass

print(f"MySQL and Python Program - Type '{commands[0]}' to see all commands")

while True:
	menu = str(input("Login (L) or Exit (E)?: ")).upper()
	if menu == "L":
		host_input = str(input("Enter host name (localhost if on local device): "))
		user_input = str(input("Enter user name: "))
		password_input = str(getpass.getpass("Enter password: "))
		database_input = str(input("Enter database name: "))
		try:
			conn = mysql.connector.connect(
				host = host_input,
				user = user_input,
				password = password_input,
				database = database_input
			)
			if conn.is_connected():
				print("Connected to database")
				cursor = conn.cursor()
				while True:
					command = str(input("Execute: ")).strip().lower() 	
					try:
						Command.view_commands()
						Command.create_list()
						Command.view_list()
						Command.create_task()
						Command.remove_task()
					except mysql.connector.Error as error:
						print("Error:", error)
					if command == "exit":
							break
				cursor.close()
				conn.close()
		except Exception as error:
			print("Login failed")
			print("Error:", error)
	elif menu == "E":
		print("Goodbye")
		break
	else:
		print("Invalid")
