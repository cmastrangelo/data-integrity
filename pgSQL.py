import psycopg2

conn = psycopg2.connect(host = 'ec2-18-205-44-21.compute-1.amazonaws.com',
                        dbname = 'd8tms6m46hau5b',
                        user = 'mjtiuafpjjhdwe',
                        password = '7df751552daa2810b986defa3659d739dd2d9f433f685f61dea4ddb2cfef80d5',
                        port = 5432)

cur = conn.cursor()

cur.execute('SELECT * FROM state')
for item in cur.fetchone():
    print(item)

cur.close()
conn.close()
