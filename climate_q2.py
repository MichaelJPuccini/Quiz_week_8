import matplotlib.pyplot as plt
import pandas as pd
import openpyxl

years = []
co2 = []
temp = []

wb = openpyxl.load_workbook('climate')
sheet = wb.get_sheet_by_name('climate')

years = sheet['A2':'A100']
co2 = sheet['B2':'B100']
temp = sheet['C2':'C100']

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
plt.savefig("co2_temp_2.png") 

