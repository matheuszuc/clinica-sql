import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect("../clinica.db")

df_pacientes  = pd.read_sql_query("SELECT * FROM pacientes", conn)
df_medicos    = pd.read_sql_query("SELECT * FROM medicos", conn)
df_consultas  = pd.read_sql_query("SELECT * FROM consultas", conn)

conn.close()


df_final = pd.merge(df_consultas, df_pacientes, on="id_paciente")
df_final = pd.merge(df_final, df_medicos, on="id_medico")

print(df_final.columns.tolist())

df_final["valor_consulta"] = pd.to_numeric(df_final["valor_consulta"], errors="coerce")

faturamento_especialidade = df_final.groupby("especialidade")["valor_consulta"].sum().round(2)
print(f"\nFaturamento por Especialidade: {faturamento_especialidade}")

consultas_cidade = df_final.groupby("cidade_x")["id_consulta"].count()
print(f"\nConsultas: {consultas_cidade}")

valor_consultas = df_final.groupby("plano_saude")["valor_consulta"].mean().round(2)
print(f"\nValor Médio das Consultas por plano de sáude: {valor_consultas}")


# Gráfico 1 - Faturamento por Especialidade
faturamento_especialidade.plot(kind="bar", title="Faturamento especialidade")
plt.ylabel("R$")
plt.xlabel("Especialidade")
plt.tight_layout()
plt.savefig("faturamento_especialidade.png")
plt.show()


# Gráfico 2 - Consultas por cidade

consultas_cidade.plot(kind="barh", title="Consultas por Cidade", color="green")
plt.xlabel("Quantidade")
plt.ylabel("Cidade")
plt.tight_layout()
plt.savefig("consultas_cidade.png")
plt.show()

# Gráfico 3 - Valor Plano
valor_consultas.plot(kind="pie", title="Ticket Médio por Plano de Saúde", autopct="%1.1f%%")
plt.ylabel("")

plt.tight_layout()
plt.savefig("valor_consultas.png")
plt.show()






