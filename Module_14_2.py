import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS not_telegram(
id INTEGER PRIMARY KEY,
user TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON not_telegram (email)')

for i in range(1, 11):
    cursor.execute('INSERT INTO not_telegram (user, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', i*10, 1000))

cursor.execute('UPDATE not_telegram SET balance = ? WHERE id % 2 = 1', (1500,))

cursor.execute('DELETE FROM not_telegram WHERE id % 3 = 1')

cursor.execute('SELECT user, email, age, balance FROM not_telegram WHERE age != 60')
results = cursor.fetchall()

for row in results:
    print(f"Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}")

cursor.execute('DELETE FROM not_telegram WHERE id = 6')

cursor.execute('SELECT COUNT(*) FROM not_telegram')
total_users = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM not_telegram')
all_balances = cursor.fetchone()[0]

print(all_balances / total_users)

connection.commit()
connection.close()