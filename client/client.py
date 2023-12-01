import socket
import sys
import os
import pandas as pd

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
msg = query_path

host_name = socket.gethostname()
port = 12345
client_socket = socket.socket()
client_socket.connect((host_name, port))
client_socket.send(msg.encode())

reply = client_socket.recv(4096)
print (reply.decode())










# remember that:
# 1. the client read an XML query (already done above)
# 2. the client sends an XML query to the server       
# 3. the client receives an XML response from server
# 4. the client parses the XML response, and store data inside output file, if any
# 5. terminate