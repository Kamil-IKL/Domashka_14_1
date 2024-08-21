import sqlite3

# Основные операторы:
# "SELECT"(получить)
# "FROM" (от)
# "WHERE"(где)
# "GROUP BY" (группировать по)
# "HAVING" (имеющий)
# "ORDER BY" (заказать по)

connection = sqlite3.connect('not_telegram.db')

# создаю курсор
cursor = connection.cursor()

# создаю БДешку
cursor.execute("""
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL 
)
""")

# метод добавления с использованием цикла for
# for i in range(10):
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                    (f"User{i+1}",f"example{i+1}gmail.com", int(i*10+10), int(1000)))

# запрос на изменение
cursor.execute("UPDATE Users SET balance = ? WHERE user EVEN NUMBERS", (500,))


connection.commit()
connection.close()