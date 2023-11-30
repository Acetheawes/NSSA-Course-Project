# server.py
import socket
import pandas as pd
import xml.etree.ElementTree as ET

# student code starts here
# Remember that:
# 1. the server reads data.csv file using pandas
# 2. the server receives an XML query from client
# 3. the server parses the XML message, extracts the query, and applies it to the DB
# 4. the server creates the XML response
# 5. the server sends the XML response to the client
# terminate

#Defining Essential Functions
def get_values(root, parent, child):
    lst = []
    for element in (root.find(str(parent))).findall(str(child)):
        lst.append(element.text)
    return lst
def get_type(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    type_element = root.find('type')
    return type_element.text
def get_conditions(filename):
    root = (ET.parse(filename)).getroot()
    condition_col_list = get_values(root, 'conditions', 'column')
    condition_val_list = get_values(root, 'conditions', 'value')
    condition_dict = dict(zip(condition_col_list, condition_val_list))
    return condition_dict
def get_columns(filename):
    root = (ET.parse(filename)).getroot()
    column_list = get_values(root, 'columns', 'column')
    return column_list


#Server Establishes Itself
hostname = socket.gethostname()
port = 12345
server_socket = socket.socket()
server_socket.bind((hostname, port))
server_socket.listen()
con, addr = server_socket.accept()
print("connection from ", str(addr))

#what to do when recieving the xml file
while True: 
    data = con.recv(1024)
    if not data: 
        break
    query = data.decode()
    msg = 'recieved'
    con.send(msg.encode())
    query_type = get_type(query)
    query_columns = get_columns(query)
    query_conditions = get_conditions(query)
    print(query_conditions)
con.close()


