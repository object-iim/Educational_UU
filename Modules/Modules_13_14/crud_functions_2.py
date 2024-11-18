import sqlite3

products = sqlite3.connect('Products.db')
not_telegram_3 = sqlite3.connect('not_telegram_3.db')

cursor_1 = products.cursor()
cursor_2 = not_telegram_3.cursor()


def initiate_db():
    cursor_1.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')
# initiate_db()

def initiate_db_2():
    cursor_2.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER NOT NULL,
    balance INTEGER NOT NULL
    )
    ''')
initiate_db_2()


def insert_products():
    cursor.execute("INSERT OR IGNORE INTO Products (title, description, price) VALUES (?, ?, ?)",
                   (f'Гранат', f'Благотворен для сердца и сосудов', f'100'))
    cursor.execute("INSERT OR IGNORE INTO Products (title, description, price) VALUES (?, ?, ?)",
                   (f'Яблоки', f'Уникальный комплекс витаминов и минералов', f'60'))
    cursor.execute("INSERT OR IGNORE INTO Products (title, description, price) VALUES (?, ?, ?)",
                   (f'Апельсины', f'Некоторые считают, что апельсины полезнее гранатов', f'80'))
    cursor.execute("INSERT OR IGNORE INTO Products (title, description, price) VALUES (?, ?, ?)",
                   (f'Клубника', f'Вкусно', f'10000'))
    products.commit()
# insert_products()

def add_user(username, email, age):
    cursor_2.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (username, email, age, 1000))
    not_telegram_3.commit()

def is_included(username):
    cursor_2.execute("SELECT username FROM Users WHERE username = ?", (username,))
    result = cursor_2.fetchone()
    return result is not None

def get_all_products():
    global all_prcts
    products.commit()
cursor_1.execute("SELECT * FROM Products")
all_prcts = cursor_1.fetchall()

products.commit()

# перемещен в конец файла module_14_5, чтобы база данных была закрыта после использованя
# products.close()