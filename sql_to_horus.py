import pandas as pd
import sqlite3 as sq


sInputFileName = 'student.csv'
InputData = pd.read_csv(sInputFileName)
print(InputData)

ProcessData = InputData
OutputData = ProcessData

SOutputFileName = 'utility.db'
sOutputTable = 'Employee'

with sq.connect(SOutputFileName) as conn:
    OutputData.to_sql(sOutputTable, conn, if_exists="replace")

print('Done')

import pandas as pd
import sqlite3 as sq


sInputFileName = 'utility.db'
sInputTable = 'Employee'

conn = sq.connect(sInputFileName)

sSql = 'select * from ' + sInputTable + ';'
InputData = pd.read_sql_query(sSql, conn)
print(InputData)

ProcessData = InputData.copy()
ProcessData.drop('email', axis=1, inplace=True)

print("===============Process data value===============")
print(ProcessData)

ProcessData.rename(columns={'name': 'emp_name', 'phone': 'emp_Phone'}, inplace=True)
print(ProcessData)

OutputData = ProcessData
OutputData.to_csv('Practical03.csv', index=False)
print('Done')