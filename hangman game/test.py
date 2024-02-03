import sqlite3
con = sqlite3.connect('scores.db')
curs = con.cursor()
bob = [4, 3]
#curs.execute('CREATE TABLE player_score(name, guesses)')
#curs.execute("INSERT INTO player_score VALUES(?,?)", bob)
#curs.execute("DELETE FROM player_score WHERE name=4")
con.commit()

con = sqlite3.connect('scores.db')
curs = con.cursor()
player_name = 'g'
guesses = 2
values=[]
values.append(player_name)
values.append(guesses)
print(values)
curs.execute("INSERT INTO player_score(?,?)", bob)
con.commit()
for row in curs.execute("SELECT * FROM player_score ORDER BY guesses asc"):
        print(row[1], row[0])

num = 2
if num == int():
    print('n')

def boo():
        print('lol')
