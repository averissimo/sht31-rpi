import socket
import yaml
import json

#
# Load config file
#
with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

#
# Send a UDP packet to the network with temperature and humidity values
#
def sendToNetworkDB(temperature, humidity):

  msgFromClient = json.dumps({
    'temperature': temperature,
    'humidity': humidity,
    'host': cfg['agent']['name']
  })

  bytesToSend         = msgFromClient.encode('utf-8')
  serverAddressPort   = (cfg['agent']['server'], cfg['agent']['port'])
  bufferSize          = 1024

  # Create a UDP socket at client side
  UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

  # Send to server using created UDP socket
  UDPClientSocket.sendto(bytesToSend, serverAddressPort)
