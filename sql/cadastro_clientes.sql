-- Tabela simples de clientes + exemplos
CREATE TABLE clientes (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(100) NOT NULL,
  email VARCHAR(120) UNIQUE,
  telefone VARCHAR(20)
);

INSERT INTO clientes (nome, email, telefone) VALUES
('Ana Silva', 'ana@email.com', '1499999-0001'),
('Bruno Souza', 'bruno@email.com', '1499999-0002'),
('Carla Lima', NULL, '1499999-0003');

-- Listar em ordem alfabética
SELECT * FROM clientes ORDER BY nome;

-- Buscar por parte do nome
-- :busca -> substitua por '%an%'
SELECT * FROM clientes WHERE nome LIKE '%an%';
