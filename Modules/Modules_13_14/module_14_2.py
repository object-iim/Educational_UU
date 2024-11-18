import sqlite3

not_telegram_2 = sqlite3.connect('not_telegram_2.db')
cursor = not_telegram_2.cursor()

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

cursor.execute("DELETE FROM Users WHERE id = ?", (6, ))

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]
print(all_balances / total_users)

not_telegram_2.commit()
not_telegram_2.close()