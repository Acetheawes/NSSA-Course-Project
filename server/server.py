# server.py
import socket
import pandas as pd
import xml.etree.ElementTree as ET
import os

# student code starts here
# Remember that:
# 1. the server reads data.csv file using pandas
# 2. the server receives an XML query from client
# 3. the server parses the XML message, extracts the query, and applies it to the DB
# 4. the server creates the XML response
# 5. the server sends the XML response to the client
# terminate

df = pd.read_csv('/home/ace/college/y2s1/nssa220/project/server/data.csv')

# #Defining Essential Functions
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
def filter_columns(dataframe, conditions, columns):
    filtered_df = dataframe
    for column, value in conditions.items():
        filtered_df=filtered_df[filtered_df[column] == value]
    return pd.DataFrame(filtered_df[columns])
def dataframe_to_xml(df, xml_file_path='output.xml'):
    xml_data = df.to_xml()

    with open(xml_file_path, 'w') as xml_file:
        xml_file.write(xml_data)

    return (os.path.abspath(xml_file_path))
def get_update_columns(filename):
    root = (ET.parse(filename)).getroot()
    condition_col_list = get_values(root, 'columns', 'column')
    condition_val_list = get_values(root, 'columns', 'value')
    condition_dict = dict(zip(condition_col_list, condition_val_list))
    
    

    return condition_dict
def typechanger(dictionary):
    final_dict = {}
    intfields = {'PassengerId','Survived','Pclass','Age','SibSp','Parch'}
    for key, val in dictionary.items():
        if (key in intfields):
            final_dict[key] = int(val)
        elif (key == "Fare"):
            final_dict[key] = float(val)
        else: final_dict[key] = val
    return final_dict

def update_df(df, conditions, columns):
    mask = pd.Series([True] * len(df))
    for col, value in conditions.items():
        mask &= (df[col] == value)
    if mask.any():
        df.loc[mask, list(columns.keys())] = list(columns.values())
        return 'success'
    else:
        return 'failure'
def generate_xml_response(status, xml_file_path='response.xml'):
    root = ET.Element('response')
    status_element = ET.SubElement(root, 'status')
    status_element.text = status


    tree = ET.ElementTree(root)


    tree.write(xml_file_path)

    return xml_file_path

# with open('/home/ace/college/y2s1/nssa220/project/client/query1.xml') as query: 
# query = '/home/ace/college/y2s1/nssa220/project/client/query1.xml'
# query_type = get_type(query)
# query_conditions = get_conditions(query)
# query_columns = get_columns(query)
# print (filter_columns(df, query_conditions, query_columns))


# Server Establishes Itself
hostname = socket.gethostname()
port = 12345
server_socket = socket.socket()
server_socket.bind((hostname, port))
server_socket.listen()
con, addr = server_socket.accept()
print("connection from ", str(addr))

#what to do when recieving the xml file
while True: 
    data = con.recv(4096)
    if not data: 
        break
    query = data.decode()
    query_type = get_type(data)
    query_columns = get_columns(data)
    query_conditions = get_conditions(data)
    if (query_type == 'select'):
        print ("select type query")
        result = filter_columns(df, query_conditions, query_columns)
        output = dataframe_to_xml(result)
        con.send(output.encode())
    elif (query_type == 'update'):
        query_update_columns = get_update_columns(data)
        updatestatus = update_df(df, query_conditions, query_update_columns)
        xml_content = generate_xml_response(str(updatestatus))
        xml_path = os.path.abspath(xml_content)
        con.sendall(xml_path.encode())
con.close()
  




