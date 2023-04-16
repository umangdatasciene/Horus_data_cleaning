import pandas as pd
import xml.etree.ElementTree as ET

cols = ["name", "phone", "email"]
rows = []

# Parse XML file
tree = ET.parse('employee.xml')
root = tree.getroot()

for elem in root:
    name = elem.find('name').text
    phone = elem.find('phone').text
    email = elem.find('email').text
    rows.append({"name": name, "phone": phone, "email": email})

df = pd.DataFrame(rows, columns=cols)
df.to_csv('employee.csv', index=False)
print("XML to CSV format")
emp = pd.read_csv('employee.csv')
print(emp)
print('Done')