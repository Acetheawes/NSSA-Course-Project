import socket
import sys
import os
import pandas as pd
import xml.etree.ElementTree as ET
def get_type(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    type_element = root.find('type')
    return type_element.text
def get_response(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    type_element = root.find('status')
    return type_element.text

print('reading the input query ...')

# try:
#     query_file = sys.argv[1]
#     xml_query = open(query_file).read()
#     output_file = sys.argv[2]
# except:
#     print("Error")
#     exit(1)  

query_file = sys.argv[1]
query_path = os.path.abspath(query_file)

# student code starts here
qtype  = (get_type(query_path))
msg = query_path

host_name = socket.gethostname()
port = 12345
client_socket = socket.socket()
client_socket.connect((host_name, port))
client_socket.send(msg.encode())
if (qtype == 'select' and len(sys.argv) == 3):
    outfile = sys.argv[2]
    outpath = os.path.abspath(outfile)
    print('sending select query')
    reply = client_socket.recv(4096)
    data = pd.read_xml(reply.decode())
    data.to_csv(outpath)
elif (qtype == 'update' and len(sys.argv) == 2):
    print('sending update query')
    reply = client_socket.recv(4096)
    status = get_response(reply.decode())
    print(status)












# remember that:
# 1. the client read an XML query (already done above)
# 2. the client sends an XML query to the server       
# 3. the client receives an XML response from server
# 4. the client parses the XML response, and store data inside output file, if any
# 5. terminate