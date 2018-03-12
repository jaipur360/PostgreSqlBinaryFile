import psycopg2
conn_string = "host='localhost' dbname='postgres' user='postgres' password='password_here'"

###### Connect to PG

conn = psycopg2.connect(conn_string)

###### Read image from file and write to PostgreSql

mypdf=open('file.pdf','rb').read()
cursor = conn.cursor()
cursor.execute("INSERT INTO tmp_table(sno,bindata) VALUES (%s,%s);", (1,psycopg2.Binary(mypdf)))
conn.commit()

###### Read image from database and write to a file

cursor = conn.cursor()
cursor.execute("SELECT bindata FROM tmp_table;")
mypdf2 = cursor.fetchone()
open('file_copy.pdf', 'wb').write((mypdf2[0]))

###### Close Connection
cursor.close()
conn.close()
