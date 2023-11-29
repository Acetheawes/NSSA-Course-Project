import socket
import sys
import pandas as pd

print('reading the input query ...')

try:
    query_file = sys.argv[1]
    xml_query = open(query_file).read()
    output_file = sys.argv[2]
except:
    print("Error")
    exit(1)  

# student code starts here
# remember that:
# 1. the client read an XML query (already done above)
# 2. the client sends an XML query to the server       
# 3. the client receives an XML response from server
# 4. the client parses the XML response, and store data inside output file, if any
# 5. terminate
