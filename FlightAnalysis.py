#Team-Y : Chandu,Saran and Wen
#Project Title: Analysing the flight delay information to better assist passenger

#Importing the Python pandas package for data cleaning and matplotlib package for data visualization

import pandas as pd
import matplotlib.pyplot as plt

#reading the .csv file and obtaining the required columns

df = pd.read_csv('C:\FALL 1\Scripting language\R\ICQS-6337\lec-01\Flights_Delay_Info.csv')
x = df.drop(['CRSDepTime','CRSArrTime','UniqueCarrier','FlightNum','TailNum','AirTime','Distance','TaxiIn','TaxiOut','Cancelled','CancellationCode','Diverted'],axis = 1)
x.to_csv('C:\FALL 1\Scripting language\R\ICQS-6337\lec-01\Flights_Delay2.csv',index = False)


#Number of flights in pie chart:
    
c1 = [df['DayOfWeek'].count()]
c2=df.groupby(by=['DayOfWeek']).count()
c3=c2['FlightNum']
labels = ['Mon','Tue','Wed','Thr','Fri','Sat','Sun']
sizes = c3
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','red','blue','green']
explode = (0.1, 0, 0, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%' ,shadow=True, startangle=140)
plt.title('Percentage of flights by each day of the week') 
plt.axis('equal')
plt.rcParams['font.size'] = 18