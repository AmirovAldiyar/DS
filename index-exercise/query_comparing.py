import psycopg2
con = psycopg2.connect(database="students", user="postgres",
                       password="postgres", host="127.0.0.1", port="5432")

cur = con.cursor()
cur.execute("EXPLAIN analyze SELECT * FROM student1 WHERE name = 'Amanda Santos'")
hash_analyze = cur.fetchall()
print("RESULTS ON HASH INDEXING SEARCH:")
for item in hash_analyze:
    print(item)


print("\n\n\nRESULTS ON B-TREE INDEXING SEARCH:")
cur.execute("EXPLAIN analyze SELECT * FROM student2 WHERE name = 'Amanda Santos'")
btree_analyze = cur.fetchall()
for item in btree_analyze:
    print(item)