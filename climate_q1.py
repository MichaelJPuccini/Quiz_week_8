import matplotlib.pyplot as plt
import sqlite3

years = []
co2 = []
temp = []

connection = sqlite3.connect("climate.db")
cursor = connection.cursor()

# Year, CO2, Temperature
sql_command = "SELECT Year FROM ClimateData;"
cursor.execute(sql_command)
years = cursor.fetchall()

sql_command = "SELECT CO2 FROM ClimateData;"
cursor.execute(sql_command)
co2 = cursor.fetchall()

sql_command = "SELECT Temperature FROM ClimateData;"
cursor.execute(sql_command)
temp = cursor.fetchall()

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--') 
plt.title("Climate Data") 
plt.ylabel("[CO2]") 
plt.xlabel("Year (decade)") 

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-') 
plt.ylabel("Temp (C)") 
plt.xlabel("Year (decade)") 
plt.show() 
plt.savefig("co2_temp_1.png") 

connection.close()
