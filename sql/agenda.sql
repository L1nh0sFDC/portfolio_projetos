-- Agenda telefônica com busca

CREATE TABLE agenda (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(80) NOT NULL,
  telefone VARCHAR(20) NOT NULL
);

INSERT INTO agenda (nome, telefone) VALUES
('Alice Moraes', '1498888-1000'),
('Gustavo Dias', '1498888-2000'),
('Marina Costa', '1498888-3000');

-- Buscar por parte do nome
SELECT * FROM agenda WHERE nome LIKE '%ma%';
