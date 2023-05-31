import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_lp9",
)

dbcursor=db.cursor()
sql="INSERT INTO datalp(id, nama) VALUES (%s, %s)" 
val=(2, "algha")
dbcursor.execute(sql, val)
db.commit()
print(dbcursor.rowcount,"data masuk!")

dbcursor=db.cursor()
dbcursor.execute("SELECT * FROM datalp")
myresult = dbcursor.fetchall()
for i in myresult:
    print(i)

dbcursor=db.cursor()
sql="DELETE FROM datalp WHERE nama='algha'"
dbcursor.execute(sql)
db.commit()
print(dbcursor.rowcount,"data dihapus!")