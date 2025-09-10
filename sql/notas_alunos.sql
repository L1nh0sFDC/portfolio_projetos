-- Cadastro de notas e média por aluno

CREATE TABLE alunos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  nome VARCHAR(100) NOT NULL
);

CREATE TABLE notas (
  id INT PRIMARY KEY AUTO_INCREMENT,
  aluno_id INT NOT NULL,
  disciplina VARCHAR(60) NOT NULL,
  nota DECIMAL(4,2) NOT NULL,
  FOREIGN KEY (aluno_id) REFERENCES alunos(id)
);

INSERT INTO alunos (nome) VALUES ('Bianca'), ('Diego'), ('Rafaela');

INSERT INTO notas (aluno_id, disciplina, nota) VALUES
(1, 'Matemática', 8.5), (1, 'Português', 7.0),
(2, 'Matemática', 6.0), (2, 'Português', 6.5),
(3, 'Matemática', 9.0), (3, 'Português', 8.0);

-- Média por aluno
SELECT a.nome, ROUND(AVG(n.nota), 2) AS media
FROM notas n JOIN alunos a ON a.id = n.aluno_id
GROUP BY a.id, a.nome
ORDER BY media DESC;
