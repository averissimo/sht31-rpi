
import sensor


d = sensor.retrieve()
# Output data to screen
print "Temperature in Celsius is : %.2f C" %d['temperature']
print "Relative Humidity is : %.2f %%RH" %d['humidity']
