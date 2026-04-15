------ Mostrando Data e Nome do Paciente 
Select *
FROM consultas
JOIN pacientes ON consultas.id_paciente = pacientes.id_paciente

------ Mostrando Data, Nome do Paciente e Nome do Médico
Select *
FROM consultas
JOIN pacientes ON consultas.id_paciente = pacientes.id_paciente
JOIN medicos ON consultas.id_medico = medicos.id_medico

------ Nome do Médico e o Valor Total Faturado por eles
SELECT medicos.nome, SUM(valor_consulta) AS total_faturado
FROM medicos
JOIN consultas ON consultas.id_medico = medicos.id_medico
GROUP BY medicos.nome
ORDER BY total_faturado DESC