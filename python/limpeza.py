import sqlite3
import pandas as pd

conn = sqlite3.connect('../clinica.db')
df = pd.read_sql_query("SELECT * FROM pacientes", conn)
conn.close()

df["cidade"] = df["cidade"].fillna("Desconhecida")
df["plano_saude"] = df["plano_saude"].fillna("Sem Plano")
df["idade"] = pd.to_numeric(df["idade"], errors="coerce")
df["idade"] = df["idade"].fillna(df["idade"].median())
df["idade"] = df["idade"].astype(int)


print(df.isnull().sum())
