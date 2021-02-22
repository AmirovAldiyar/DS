from faker import Faker
import psycopg2
con = psycopg2.connect(database="students", user="postgres",
                       password="postgres", host="127.0.0.1", port="5432")
faker = Faker()
print("Database opened successfully")
cur = con.cursor()
cur.execute('''CREATE TABLE STUDENT1
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      ADDRESS           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      REVIEW        TEXT    NOT NULL);''')
cur.execute('''CREATE TABLE STUDENT2
      (ID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      ADDRESS           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      REVIEW        TEXT    NOT NULL);''')
print("Tables created successfully")

for i in range(100000):
    cur.execute(f"INSERT INTO STUDENT1 (ID,NAME,ADDRESS,AGE,REVIEW) VALUES ({str(i)}, '{faker.name()}', '{faker.address()}', {faker.pyint(min_value=18, max_value=25)}, '{faker.text()}');")
    cur.execute(f"INSERT INTO STUDENT2 (ID,NAME,ADDRESS,AGE,REVIEW) VALUES ({str(i)}, '{faker.name()}', '{faker.address()}', {faker.pyint(min_value=18, max_value=25)}, '{faker.text()}');")
con.commit()
print("Record inserted successfully")
cur = con.cursor()
cur.execute("SELECT id, name, address, age , review from STUDENT1")
rows = cur.fetchall()

print(rows)
for row in rows:
    print("ID =", row[0])
    print("NAME =", row[1])
    print("ADDRESS =", row[2])
    print("AGE =", row[3])
    print("REVIEW =", row[4], "\n")
print('\n\n\n')
cur = con.cursor()
cur.execute("SELECT id, name, address, age , review from STUDENT2")
rows = cur.fetchall()

print(rows)
for row in rows:
    print("ID =", row[0])
    print("NAME =", row[1])
    print("ADDRESS =", row[2])
    print("AGE =", row[3])
    print("REVIEW =", row[4], "\n")
print("Operation done successfully")
con.close()

