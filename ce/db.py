import psycopg2
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


##### VARIABLES ########

conn = psycopg2.connect(database="booking1685151146470mztpglwhzpempjtf",
                        host="psql-mock-database-cloud.postgres.database.azure.com",
                        user="mfhgjloqpkwpbbykjvoiugqi@psql-mock-database-cloud",
                        password="ofqzqndtxuhprdaspfwfxgvr",
                        port="5432")


cursor = conn.cursor()

tableName = "bookings"

postgreSQL_select_Query = ("select * from " + tableName)

cursor.execute(postgreSQL_select_Query)
print("Selecting rows from X table using cursor.fetchall")
x_records = cursor.fetchall()

#print("Print each row and it's columns values")
#for row in x_records:
	#print("Id (hopefully) = ", row[0], )
	#print("Row1 Title = ", row[1])
	#print("Row2 Title  = ", row[2], "\n")

rowOne = []
rowTwo = []
for rec in x_records:
  rowOne.append(rec[0])
  rowTwo.append(rec[1])


x = np.array(rowOne)
y = np.array(rowTwo)

plt.plot(rowOne, rowTwo, 'o')
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x+b)
plt.show()


#####test tables

#('gceusers_bck',)
#('users',)
#('appartments',)
#('bookings',)
#('company',)
#('property_history',)
#('worker_type',)
#('worker',)
#('address',)
#('poc_worker',)
#('config_item',)
#('gceusers',)
#('gceuser_userrole',)
#('gceuser_report',)
#('sameCASEname',)
#('samecasename',)
