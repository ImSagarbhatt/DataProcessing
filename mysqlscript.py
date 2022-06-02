import mysql.connector

# creating the connection with database
conn = mysql.connector
mydb = conn.connect(
    host="localhost",
    port="3306",
    user="root",
    password="init1234",
    database="testapp",
)
if mydb.is_connected():
    print("************ Database successfully connected *************\n\n")

cur = mydb.cursor()

# Insert data in the table
# s = """ INSERT INTO users (name, city,country)
#         VALUES(%s,%s,%s)
# """
# val = ("Ajinkya", "Karnataka", "India")
# cur.execute(s, val)
# mydb.commit()
# mydb.close()

# Fetch the data from the table
# s = "SELECT name FROM users WHERE country = 'India'"
# cur.execute(s)
# result = cur.fetchall()
# for i in result:
#     print(i)
# mydb.close()


# to update the data from the table
# s = "UPDATE users SET country = 'India' WHERE country = 'Pakistan'"
# cur.execute(s)
# mydb.commit()
# mydb.close()
