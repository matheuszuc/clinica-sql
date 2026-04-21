import sqlite3
import pandas as pd

conn = sqlite3.connect("../clinica.db")

df_pacientes  = pd.read_sql_query("SELECT * FROM pacientes", conn)
df_medicos    = pd.read_sql_query("SELECT * FROM medicos", conn)
df_consultas  = pd.read_sql_query("SELECT * FROM consultas", conn)

conn.close()


df_final = pd.merge(df_consultas, df_pacientes, on="id_paciente")
df_final = pd.merge(df_final, df_medicos, on="id_medico")

print(df_final.columns.tolist())

df_final["valor_consulta"] = pd.to_numeric(df_final["valor_consulta"], errors="coerce")
faturamento_total = df_final.groupby("especialidade")["valor_consulta"].sum().round(2)
print(f"\nFaturamento por Especialidade: {faturamento_total}")

consultas = df_final.groupby("cidade_x")["id_consulta"].count()
print(f"\nConsultas: {consultas}")

valor_consultas = df_final.groupby("plano_saude")["valor_consulta"].mean().round(2)
print(f"\nValor Médio das Consultas por plano de sáude: {valor_consultas}")







