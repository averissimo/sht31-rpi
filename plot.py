import pymongo
import datetime
import dateutil.parser
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import math

from pymongo import MongoClient
client = MongoClient()

db = client.sensor

results = db.readings.find()

temp = []
humd = []
time = []

for el in results:
    temp.append(el['temperature'])
    humd.append(el['humidity'])
    time.append(dateutil.parser.parse(el['createdAt']))

time = matplotlib.dates.date2num(time)

sns.set_style('whitegrid', { 'grid.color': '.9'})

fig = plt.figure(figsize=(20,10))

ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

plt.gcf().autofmt_xdate()
myFmt = mdates.DateFormatter('%d/%m/%y %H:%M')

ax1.plot_date(time, temp, markersize = 2)

ax2.plot_date(time, humd, markersize = 2)

ax1.xaxis.set_major_formatter(myFmt)
ax2.xaxis.set_major_formatter(myFmt)

ax1.set_ylim(math.floor(min(temp)) - 2, math.ceil(max(temp)) + 2)
ax2.set_ylim(math.floor(min(humd)) - 2, math.ceil(max(humd)) + 2)

ax1.set(title="Temperature", xlabel="Time", ylabel="Celsius")
ax2.set(title="Relative Humidity", xlabel="Time", ylabel="% Relative humidity")

plt.tight_layout()

plt.savefig("sensor.png")

plt.close()
