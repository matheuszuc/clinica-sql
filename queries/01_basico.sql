-- 01_basico.sql
-- Consultas básicas

-- Ver todos os dados
SELECT * 
FROM clinica_pacientes;

-- Ver nome, cidade e a especialidade
Select nome, cidade, especialidade
FROM clinica_pacientes

-- Pacientes de São Paulo
SELECT nome, cidade
FROM clinica_pacientes
WHERE cidade = 'São Paulo';

-- Ordenar por idade
SELECT nome, idade
FROM clinica_pacientes
ORDER BY idade DESC;