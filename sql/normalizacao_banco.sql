-- Exemplo simples de normalização com 3 tabelas

CREATE TABLE usuarios (
    id INT PRIMARY KEY,
    nome VARCHAR(50)
);

CREATE TABLE permissoes (
    id INT PRIMARY KEY,
    descricao VARCHAR(50)
);

CREATE TABLE usuario_permissao (
    usuario_id INT,
    permissao_id INT,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (permissao_id) REFERENCES permissoes(id)
);
