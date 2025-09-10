-- Produtos e vendas resumidos com consultas úteis

CREATE TABLE produtos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(100) NOT NULL,
  preco DECIMAL(10,2) NOT NULL
);

CREATE TABLE vendas (
  id INT PRIMARY KEY AUTO_INCREMENT,
  produto_id INT NOT NULL,
  qtd INT NOT NULL,
  data DATE NOT NULL,
  FOREIGN KEY (produto_id) REFERENCES produtos(id)
);

INSERT INTO produtos (nome, preco) VALUES
('Caderno', 15.90), ('Caneta', 4.50), ('Mochila', 120.00);

INSERT INTO vendas (produto_id, qtd, data) VALUES
(1, 2, '2025-09-01'), (2, 10, '2025-09-02'), (3, 1, '2025-09-03');

-- Total de vendas por produto
SELECT p.nome, SUM(v.qtd) AS total_qtd, SUM(v.qtd * p.preco) AS total_rs
FROM vendas v
JOIN produtos p ON p.id = v.produto_id
GROUP BY p.id, p.nome
ORDER BY total_rs DESC;

-- Total vendido no mês (substitua o mês)
SELECT SUM(v.qtd * p.preco) AS total_mes
FROM vendas v JOIN produtos p ON p.id = v.produto_id
WHERE DATE_FORMAT(v.data, '%Y-%m') = '2025-09';
