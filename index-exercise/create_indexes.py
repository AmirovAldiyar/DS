import psycopg2
con = psycopg2.connect(database="students", user="postgres",
                       password="postgres", host="127.0.0.1", port="5432")

cur = con.cursor()
cur.execute('''CREATE INDEX btindex ON student1 USING btree (name);''')
con.commit()
cur.execute('''CREATE INDEX hindex ON student2 USING hash (name);''')
con.commit()
print("hash made")