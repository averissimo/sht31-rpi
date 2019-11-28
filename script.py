import matrix8x8
import sensor
import time
import sys

#
# Reusable method
#
def call_sensor(measurement, short):
  d = sensor.retrieve()
  try:
    matrix8x8.draw(d[measurement], short)
  except:
    print "error writing to screen"

#
# Error writing to matrix
#
def error():
  try:
    matrix8x8.draw(d[measurement], short)
  except:
    try:
      matrix8x8.draw(99, 'error')
    except:
      print "error writing to screen"

#
# Run for a minute, every 5 seconds alternate
#  between temperature and humidity
#
try:
  for x in range(0, 5):

    call_sensor('temperature', 'temp')
    time.sleep(4.5)

    call_sensor('humidity', 'humd')
    time.sleep(4.5)
except:
  e = sys.exc_info()[0]
  print "Error! Can't take measurement", e
