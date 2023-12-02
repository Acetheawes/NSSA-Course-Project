import pandas as pd
import xml.etree.ElementTree as ET

query1 = 'client/query2.xml'
df = pd.read_csv('/home/ace/college/y2s1/nssa220/project/server/data.csv')
#Default Functions
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

    print(f"XML file '{xml_file_path}' generated successfully.")


qtype = get_type(query1)
# print(qtype)
conditions = get_conditions(query1)
columns = get_columns(query1)

if (qtype == 'select'):
    filtered_df = filter_columns(df, conditions, columns)
    output = dataframe_to_xml(filtered_df)
    
    pass
elif (qtype == 'update'):
    pass



# print(filter_columns(df, conditions, columns))
# print((filtered_df.columns).tolist())









