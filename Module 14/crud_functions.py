import sqlite3

def initiate_db(db_name='products.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    price INT NOT NULL
    );
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INT NOT NULL,
    balance INT NOY NULL
    );
    ''')
    connection.commit()
    connection.close()

def add_user(username, email, age):
    connection = sqlite3.connect('Users')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (username, email, age, 1000))
    connection.close()

def is_included(username):
    connection = sqlite3.connect('Users')
    cursor = connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM Users WHERE username = ?', (username))
    user_count = cursor.fetchone()[0]
    connection.close()
    return user_count > 0

def get_all_products(db_name='products.db'):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    select_query = "SELECT * FROM Products;"
    cursor.execute(select_query)
    products = cursor.fetchall()
    connection.close()
    return products

initiate_db()
connection = sqlite3.connect('products.db')
cursor = connection.cursor()
cursor.execute('INSERT INTO products (id, title, description, price) VALUES (?,?,?,?)', (1,'Продукт1', 'Описание1', 100))
cursor.execute('INSERT INTO products (id, title, description, price) VALUES (?,?,?,?)', (2,'Продукт2', 'Описание2', 200))
cursor.execute('INSERT INTO products (id, title, description, price) VALUES (?,?,?,?)', (3,'Продукт3', 'Описание3', 300))
cursor.execute('INSERT INTO products (id, title, description, price) VALUES (?,?,?,?)', (4,'Продукт4', 'Описание4', 400))
connection.commit()
connection.close()