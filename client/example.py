import xml.etree.ElementTree as et
import sys

xmlfile = sys.argv[1]

tree = et.parse(xmlfile)
root = tree.getroot()
# print(et.tostring(root))
query_type = root.find('type').text
print("Query Type:", query_type)

# Get the columns to select
columns = [column.text for column in root.find('columns')]
print("Columns to Select:", columns)

# Get the conditions
# for condition in root.find('conditions'):
#     conditions[condition.tag] = condition.text
# print("Conditions:", conditions)
conditions = []
values = []

for condition in root.find('conditions'):
    for column in condition.findall('column'):
        conditions.append(column.text)

    for value in condition.findall('value'):
        values.append(value.text)

finalcond = {}
for c in conditions:
    for v in values:
        finalcond.update(conditions[c], values[v])





