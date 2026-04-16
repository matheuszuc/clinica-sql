-- 01_basico.sql
-- Consultas básicas

-- Ver todos os dados
Select *
FROM medicos, consultas, pacientes;

-- Ver Médico e Especialidade
Select nome, especialidade
FROM medicos;

-- Pacientes de São Paulo
SELECT nome, cidade
FROM pacientes
WHERE cidade = 'São Paulo';

-- Ordenar por idade
SELECT nome, idade
FROM pacientes
ORDER BY idade DESC;