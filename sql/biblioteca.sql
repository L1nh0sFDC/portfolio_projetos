-- Livros e empréstimos básicos

CREATE TABLE livros (
  id INT PRIMARY KEY AUTO_INCREMENT,
  titulo VARCHAR(150) NOT NULL,
  autor VARCHAR(100)
);

CREATE TABLE emprestimos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  livro_id INT NOT NULL,
  usuario VARCHAR(100) NOT NULL,
  data_emprestimo DATE NOT NULL,
  data_devolucao DATE,
  FOREIGN KEY (livro_id) REFERENCES livros(id)
);

INSERT INTO livros (titulo, autor) VALUES
('Dom Casmurro', 'Machado de Assis'),
('Capitães da Areia', 'Jorge Amado'),
('Memórias Póstumas', 'Machado de Assis');

-- Livros mais emprestados
SELECT l.titulo, COUNT(*) AS vezes
FROM emprestimos e JOIN livros l ON l.id = e.livro_id
GROUP BY l.id, l.titulo
ORDER BY vezes DESC;

-- Não devolvidos
SELECT l.titulo, e.usuario, e.data_emprestimo
FROM emprestimos e JOIN livros l ON l.id = e.livro_id
WHERE e.data_devolucao IS NULL;
