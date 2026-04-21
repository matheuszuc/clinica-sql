import sqlite3
import pandas as pd

# conecta no Banco
conn = sqlite3.connect('../clinica.db')


# Lê a tabela de pacientes
df = pd.read_sql_query("SELECT * FROM pacientes", conn)

conn.close()


print(df)
print(f"Shape: {df.shape}")
print(f"Colunas: {df.columns.tolist()}")