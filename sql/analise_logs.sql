-- Criando tabela de logs
CREATE TABLE logs (
    id INT PRIMARY KEY,
    usuario VARCHAR(50),
    ip VARCHAR(20),
    acao VARCHAR(50),
    horario TIMESTAMP
);

-- Exemplo de consulta: IPs com mais acessos
SELECT ip, COUNT(*) as total
FROM logs
GROUP BY ip
ORDER BY total DESC;
