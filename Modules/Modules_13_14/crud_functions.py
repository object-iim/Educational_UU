import sqlite3

products = sqlite3.connect('Products.db')
cursor = products.cursor()

def initiate_db():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INTEGER NOT NULL
    )
    ''')

initiate_db()

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

def get_all_products():
    global all_prcts
    products.commit()

cursor.execute("SELECT * FROM Products")
all_prcts = cursor.fetchall()


products.commit()

# перемещен в конец файла module_14_4, чтобы база данных была закрыта после использованя
# products.close()