import sqlite3
conn = sqlite3.connect('compania.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE parameter_group (id INT PRIMARY KEY, name
VARCHAR(20), list_parameters )''')

conn.commit()



# curs.execute('''CREATE TABLE product (id INT PRIMARY KEY, name
# VARCHAR(20), id_category INT, description Text, release_date DATE,)''')
