-- Estoque simples e consulta de baixo nível

CREATE TABLE estoque (
  id INT PRIMARY KEY AUTO_INCREMENT,
  produto VARCHAR(100) NOT NULL,
  quantidade INT NOT NULL DEFAULT 0,
  minimo INT NOT NULL DEFAULT 5
);

INSERT INTO estoque (produto, quantidade, minimo) VALUES
('Cabo USB', 12, 5),
('Carregador', 3, 5),
('Fone de ouvido', 8, 5);

-- Itens abaixo do mínimo
SELECT * FROM estoque WHERE quantidade < minimo ORDER BY quantidade ASC;

-- Reposição (exemplo de update)
-- UPDATE estoque SET quantidade = quantidade + 10 WHERE produto = 'Carregador';
