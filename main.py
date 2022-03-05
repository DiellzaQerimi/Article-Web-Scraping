import sqlite3

conn = sqlite3.connect('articles.db')
c = conn.cursor()

#c.execute('''CREATE TABLE AlsatM(Title TEXT, Article TEXT, Date DATE)''')
#c.execute('''CREATE TABLE VizionPlus(Title TEXT, Article TEXT)''')
c.execute('''Select * from VizionPlus''')
#c.execute('''Select * from AlsatM''')
results = c.fetchall()
print(results)
