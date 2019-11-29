import matrix8x8
import sensor
import time
import sys
from datetime import datetime

def draw(val, short):
  try:
    with open('screen_on.txt') as f:
      try:
        matrix8x8.draw(val, short)
      except:
        print("error writing to screen")
  except FileNotFoundError:
    matrix8x8.draw('00', 'clear')

#
# Reusable method
#
def call_sensor(measurement, short):
  d = sensor.retrieve()
  draw(d[measurement], short)

#
# Run for a minute, every 5 seconds alternate
#  between temperature and humidity
#

start = datetime.now()
try:
  while (datetime.now() - start).total_seconds() < 58:
    call_sensor('temperature', 'temp')
    time.sleep(4.5)

    call_sensor('humidity', 'humd')
    time.sleep(4.5)
except:
  draw(99, 'error')
  e = sys.exc_info()[0]
  print("Error! Can't take measurement", e)
