import socket
import pandas as pd
import xml.etree.ElementTree as ET
import os

df = pd.read_csv('/home/ace/college/y2s1/nssa220/project/server/data2.csv')
query = '/home/ace/college/y2s1/nssa220/project/client/query5.xml'

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
    # Apply conditions to filter the DataFrame
    mask = pd.Series([True] * len(df))
    for col, value in conditions.items():
        mask &= (df[col] == value)
    
    # Update specified columns for the filtered rows
    if mask.any():
        df.loc[mask, list(columns.keys())] = list(columns.values())
        return True
    else:
        return False
def generate_xml_response(xml_file_path, status):
    root = ET.Element('response')
    status_element = ET.SubElement(root, 'status')
    status_element.text = status

    tree = ET.ElementTree(root)
    tree.write(xml_file_path)


conditions = typechanger(get_conditions(query))
updates = typechanger(get_update_columns(query))

ustatus =  update_df(df, conditions, updates)
generate_xml_response('/home/ace/college/y2s1/nssa220/project/server/output.xml', 'True')
print('output.xml')













    
