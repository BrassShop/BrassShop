import sqlite3
import pandas as pd

conn = sqlite3.connect('{}.sqlite'.format(r'C:\!P\primer\datebase.db'))
s = pd.read_sql('select * from skills', conn)
print(s)
conn.commit()
conn.close()