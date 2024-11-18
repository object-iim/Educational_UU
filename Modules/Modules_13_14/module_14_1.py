import sqlite3

not_telegram = sqlite3.connect('not_telegram.db')
cursor = not_telegram.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL UNIQUE,
email TEXT NOT NULL UNIQUE,
age INTEGER,
balance INTEGER NOT NULL
)
''')

for i in range(1, 11):
    cursor.execute("INSERT OR IGNORE INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f'User{i}', f'example{i}@gmail.com', f'{i}0', 1000))

for i in range(1, 11):
    if i % 2 != 0:
        cursor.execute("UPDATE OR IGNORE Users SET balance = ? WHERE username = ?", (500, f'User{i}'))
    else:
        pass

for i in range(1, 11, 3):
    cursor.execute("DELETE FROM Users WHERE username = ?", (f'User{i}', ))

cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
usernames_age_not_60 = cursor.fetchall()
for user in usernames_age_not_60:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')

not_telegram.commit()
not_telegram.close()