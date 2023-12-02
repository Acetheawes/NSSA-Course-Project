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
query = '/home/ace/college/y2s1/nssa220/project/client/query4.xml'

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
def get_updates(filename):
    root = (ET.parse(filename)).getroot()
    condition_col_list = get_values(root, 'columns', 'column')
    condition_val_list = get_values(root, 'columns', 'value')
    condition_dict = dict(zip(condition_col_list, condition_val_list))
    return condition_dict


dict = {'key':'val'}
# print(dict.get('key'))

query_type = get_type(query)
query_conditions = get_conditions(query)
query_updates = get_updates(query)