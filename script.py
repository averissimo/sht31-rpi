import matrix8x8
import sensor
import time

sensor.savemongo()

for x in range(0, 5):

  d = sensor.retrieve()
  matrix8x8.draw(d['temperature'], 'temp')
  time.sleep(4.5)
  d = sensor.retrieve()
  matrix8x8.draw(d['humidity'], 'humd')
  time.sleep(4.5)


