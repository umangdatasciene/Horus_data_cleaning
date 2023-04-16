import pandas as pd
import xml.etree.ElementTree as ET

# Define columns for CSV file
cols = ["name", "phone", "email"]

rows = []

tree = ET.parse('employee.xml')
root = tree.getroot()
for elem in root:
    name = elem.find('name').text
    phone = elem.find('phone').text
    email = elem.find('email').text
    rows.append({"name": name, "phone": phone, "email": email})

df = pd.DataFrame(rows, columns=cols)
df.to_csv('employee.csv', index=False)


df.to_csv('AllinOne.csv', mode='a', index=False, header=True)

print("XML to CSV format")
emp = pd.read_csv('employee.csv')
print(emp)

sInputFileName = 'student.csv'
InputData = pd.read_csv(sInputFileName)
print("CSV to CSV format")
print("============Input Data Value============")
print(InputData)

ProcessData = InputData
OutputData = ProcessData
OutputData.to_csv('AllinOne.csv', mode='a', index=False, header=True)


print('Done')