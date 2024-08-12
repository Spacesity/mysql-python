import mysql.connector
import getpass

commands = [
	"list-commands",
	"create-list",
	"view-list",
	"create-task",
	"remove-task",
	"exit"
]

class Command():
	def view_commands():
		if command == commands[0]:
			for com in commands:
				print(com)
	def create_list():
		if command == commands[1]:
			list_name = str(input("Enter new list name: "))
			list_creation = f"CREATE TABLE {list_name} (task int, description varchar(200))"
			cursor.execute(list_creation)
	def view_list():
		if command == commands[2]:
			database_input = str(input("Enter list name: "))
			list_view = f"SELECT * FROM {database_input}"
			cursor.execute(list_view)
			rows = cursor.fetchall()
			for row in rows:
				print(row)
	def create_task():
		if command == commands[3]:
			list_name = str(input("Enter list name: "))
			task_name = str(input("Enter task name: "))
			task_description = str(input("Enter task description: ")).strip().lower()
			task_creation = f"INSERT INTO {list_name} (task, description) VALUES ({task_name}, {task_description})"
			cursor.execute(task_creation)
	def remove_task():
		if command == commands[4]:
			list_name = str(input("Enter list name: "))
			task_name = str(input("Enter task name: "))
			task_deletion = f"DELETE FROM {list_name} WHERE task = {task_name}"
			cursor.execute(task_deletion)

print(f"MySQL and Python Program - Type '{commands[0]}' to see all commands")

while True:
	menu = str(input("Login (L) or Quit (Q)?: ")).upper()
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
					if command != "exit":
						try:
							Command.view_commands()
							Command.create_list()
							Command.view_list()
							Command.create_task()
							Command.remove_task()
						except mysql.connector.Error as error:
							print("Error:", error)
					elif command == "exit":
							break
					else:
						print("Invalid")
				cursor.close()
				conn.close()
		except Exception as error:
			print("Login failed")
			print("Error:", error)
	elif menu == "Q":
		print("Goodbye")
		break
	else:
		print("Invalid")
