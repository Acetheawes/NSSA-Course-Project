# server.py
import socket
import pandas as pd
import xml.etree.ElementTree as et

# student code starts here
# Remember that:
# 1. the server reads data.csv file using pandas
# 2. the server receives an XML query from client
# 3. the server parses the XML message, extracts the query, and applies it to the DB
# 4. the server creates the XML response
# 5. the server sends the XML response to the client
# terminate
hostname = socket.gethostname()
port = 12345
serversocket = socket.socket()
serversocket.bind((hostname, port))
serversocket.listen()
connection, address = serversocket.accept()
print('con', str(address))
while True:
    data = connection.recv(1024)
    if not data:
        break
    print('recieved: ', data.decode())
    msg = 'fuck off'
    connection.send(msg.encode())
connection.close()

def parse(content):
    tree = et.parse(content)
    root = tree.getroot()
    