import psycopg2

# Connect to the database by creating a connection object
conn = psycopg2.connect(
    host='localhost',
    dbname='students',
    user='postgres',
    password='241540G@ly@'
)

# Create a cursor to work with the database
cur = conn.cursor() # используется для выполнения SQL-запросов к базе данных

# Ищем по имени
def search_user_by_name():
    name = input("Enter the name of the user to search for: ")
    cur.execute("SELECT * FROM students_data WHERE name = %s", (name,))
    user = cur.fetchone()
    if user:
        print(f"Found user: {user}")
    else:
        print("User not found")

# Ищем по номеру
def search_user_by_phone_number():
    phone_number = input("Enter the phone number of the user to search for: ")
    cur.execute("SELECT * FROM students_data WHERE phone_number = %s", (phone_number,))
    user = cur.fetchone()
    if user:
        print(f"Found user: {user}")
    else:
        print("User not found")

# Удалять чела по имени
def delete_user_by_name():
    name = input("Enter the name of the user to delete: ")
    cur.execute("DELETE FROM students_data WHERE name = %s", (name,))
    conn.commit()
    print("User deleted successfully")

# Удалять по номеру 
def delete_user_by_phone_number():
    phone_number = input("Enter the phone number of the user to delete: ")
    cur.execute("DELETE FROM students_data WHERE phone_number = %s", (phone_number,))
    conn.commit()
    print("User deleted successfully")

# Добавляем пользователя 
def add_new_user():
    name = input("Enter the name of the new user: ")
    phone_number = input("Enter the phone number of the new user: ")
    cur.execute("INSERT INTO students_data (name, phone_number) VALUES (%s, %s)",
                (name, phone_number))
    conn.commit()
    print("User added successfully")

# Изменить номер пользователя 
def change_user_phone_number():
    name = input("Enter the name of the user to change the phone number: ")
    new_phone_number = input("Enter the new phone number: ")
    cur.execute("UPDATE students_data SET phone_number = %s WHERE name = %s",
                (new_phone_number, name))
    conn.commit()
    print("Phone number updated successfully")

# Основной цикл
while True:
    print("""
    1) Search for user by name
    2) Search for user by phone number
    3) Delete a user by name
    4) Delete a user by phone number
    5) Add a new user
    6) Change user's phone number
    7) Exit
    """)

    n = input("Enter your choice: ")

    if n == '1':
        search_user_by_name()
    elif n == '2':
        search_user_by_phone_number()
    elif n == '3':
        delete_user_by_name()
    elif n == '4':
        delete_user_by_phone_number()
    elif n == '5':
        add_new_user()
    elif n == '6':
        change_user_phone_number()
    elif n == '7':
        break
    else:
        print("Invalid choice. Please try again.")

cur.close()
conn.close() # разрывает соединение с бд
