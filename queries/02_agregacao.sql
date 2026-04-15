------ Contando as Consultas
Select count(data_consulta)
FROM clinica_pacientes


------ Valor Médio das Consultas 
Select AVG(data_consulta)
FROM clinica_pacientes

------ Faturamento Total da clinica
Select SUM(valor_consulta)
FROM clinica_pacientes

------ Quantas Consultas cada Especialidade Teve
Select id_paciente, especialidade
FROM clinica_pacientes
Group By "especialidade";
ORDER BY count(*) DESC