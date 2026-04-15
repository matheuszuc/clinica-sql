----- Liste os pacientes que nunca tiveram uma consulta
SELECT pacientes.nome
FROM pacientes
LEFT JOIN consultas ON pacientes.id_paciente = consultas.id_paciente
WHERE consultas.id_paciente IS NULL

----- Liste as consultas com o nome do paciente onde o valor_consulta está NULL
Select consultas.valor_consulta, pacientes.nome
FROM consultas
Join pacientes ON consultas.id_paciente = pacientes.id_paciente
Where consultas.valor_consulta IS NULL

----- Mostre o nome e o valor das consultas de pacientes que pagaram acima da média geral 
Select pacientes.nome, consultas.valor_consulta
FROM consultas
Join pacientes ON consultas.id_paciente = pacientes.id_paciente
Where valor_consulta > (SELECT AVG(valor_consulta) FROM  consultas)