# server.py
import socket
import pandas as pd
import xml

# student code starts here
# Remember that:
# 1. the server reads data.csv file using pandas
# 2. the server receives an XML query from client
# 3. the server parses the XML message, extracts the query, and applies it to the DB
# 4. the server creates the XML response
# 5. the server sends the XML response to the client
# terminate

def readXML(xmlfile):
    with open(xmlfile).read() as file:
        




df = pd.read_csv("/home/ace/college/y2s1/nssa220/project/server/data.csv")
host_name = socket.gethostname()
port = 12345
ssock = socket.socket()
ssock.bind(host_name, port)
