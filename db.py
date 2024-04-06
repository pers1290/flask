import sqlite3

connection = sqlite3.connect('db/Reg.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Reg (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
password TEXT NOT NULL,
phone TEXT NOT NULL,
profil_img TEXT NOT NULL,
fon_img TEXT NOT NULL,
favourites TEXT NOT NULL
)
''')
connection = sqlite3.connect('db/Messanger.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Reg (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
friends TEXT NOT NULL,
messages TEXT NOT NULL
)
''')
cursor.execute('INSERT INTO Reg (name, friends, messages) VALUES (?, ?, ?)',
               ('Василий', 'Хомяк', '[]'))
cursor.execute('INSERT INTO Reg (name, friends, messages) VALUES (?, ?, ?)',
               ('Хомяк', 'Василий', '[]'))
# cursor.execute('INSERT INTO Users (name, topic, post_text, img_url) VALUES (?, ?, ?, ?)',
# ('Mark', 'комната', '', '/static/img/m3.jpg'))
connection.commit()
connection.close()
