import  sqlite3
import pandas as pd
conn = sqlite3.connect('/www/server/panel/data/default.db')
query = "SELECT name FROM sites"
df = pd.read_sql_query(query,conn)
df.to_excel('/www/backup/site.xlsx',index=False)
conn.close()
