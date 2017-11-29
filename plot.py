import pymongo
import datetime
import dateutil.parser
import matplotlib
import matplotlib.pyplot as plt

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

fig = plt.figure(figsize=(20,10))

ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.plot_date(time, temp)
ax2.plot_date(time, humd)

ax1.set_ylim(min(temp) - 5, max(temp) + 5)
ax2.set_ylim(min(humd) - 5, max(humd) + 5)

ax1.set(title="Temperature", xlabel="Time", ylabel="Celsius")
ax2.set(title="Relative Humidity", xlabel="Time", ylabel="% Relative humidity")

plt.tight_layout()

plt.savefig("sensor.png")
