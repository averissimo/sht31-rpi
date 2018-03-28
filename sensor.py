import smbus
import time
import datetime
import pymongo

def retrieve():
  # Get I2C bus
  bus = smbus.SMBus(1)
 
  # SHT31 address, 0x44(68)
  bus.write_i2c_block_data(0x45, 0x2C, [0x06])
 
  time.sleep(0.5)
 
  # SHT31 address, 0x44(68)
  # Read data back from 0x00(00), 6 bytes
  # Temp MSB, Temp LSB, Temp CRC, Humididty MSB, Humidity LSB, Humidity CRC
  data = bus.read_i2c_block_data(0x45, 0x00, 6)
 
  # Convert the data
  temp = data[0] * 256 + data[1]
  cTemp = -45 + (175 * temp / 65535.0)
  humidity = 100 * (data[3] * 256 + data[4]) / 65535.0
  
  
  return {
    "temperature": cTemp,
    "humidity": humidity,
    "createdAt": datetime.datetime.utcnow()
  }
   

def savemongo():
  
  reading = retrieve()

  from pymongo import MongoClient
  client = MongoClient()

  db = client.sensor

  db.readings.insert_one(reading)

