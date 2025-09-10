-- Criando tabela de usuários
CREATE TABLE usuarios (
    id INT PRIMARY KEY,
    nome VARCHAR(50),
    email VARCHAR(100)
);

-- Inserindo dados
INSERT INTO usuarios (id, nome, email) VALUES
(1, 'Carlos', 'carlos@email.com'),
(2, 'Ana', 'ana@email.com'),
(3, 'João', 'joao@email.com');

-- Selecionando todos os usuários
SELECT * FROM usuarios;
