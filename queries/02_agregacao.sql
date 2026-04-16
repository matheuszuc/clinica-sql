------ Contando as Consultas
Select count(data_consulta) AS "Todas as Consultas"
FROM consultas


------ Valor Médio das Consultas 
Select AVG(valor_consulta) AS "Valor da Consulta"
FROM consultas

------ Faturamento Total da clinica
Select SUM(valor_consulta) AS "Total Faturado"
FROM consultas

------ Qual foi o Plano de Saúde mais utilizado
Select count(id_paciente) AS "Pacientes", plano_saude
FROM pacientes
Group By "plano_saude"
ORDER BY count(*) DESC
