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
timeT = []
timeH = []

for el in results:
  if 'createdAt' not in el:
    continue
  if 'temperature' in el:
    temp.append(el['temperature'])
    timeT.append(dateutil.parser.parse(el['createdAt']))
  if 'humidity' in el:
    humd.append(el['humidity'])
    timeH.append(dateutil.parser.parse(el['createdAt']))


timeT = matplotlib.dates.date2num(timeT)
timeH = matplotlib.dates.date2num(timeH)

sns.set_style('whitegrid', { 'grid.color': '.9'})

fig = plt.figure(figsize=(20,10))

myFmt = mdates.DateFormatter('%d/%m/%y %H:%M')

if len(temp) > 0:
  ax1 = fig.add_subplot(121)
  plt.gcf().autofmt_xdate()
  ax1.plot_date(timeT, temp, markersize = 2)
  ax1.xaxis.set_major_formatter(myFmt)
  ax1.set_ylim(math.floor(min(temp)) - 2, math.ceil(max(temp)) + 2)
  ax1.set(title="Temperature", xlabel="Time", ylabel="Celsius")

if len(humd) > 0:
  ax2 = fig.add_subplot(122)
  plt.gcf().autofmt_xdate()
  ax2.plot_date(timeH, humd, markersize = 2)
  ax2.xaxis.set_major_formatter(myFmt)
  ax2.set_ylim(math.floor(min(humd)) - 2, math.ceil(max(humd)) + 2)
  ax2.set(title="Relative Humidity", xlabel="Time", ylabel="% Relative humidity")

plt.tight_layout()

plt.savefig("sensor.png")

plt.close()
