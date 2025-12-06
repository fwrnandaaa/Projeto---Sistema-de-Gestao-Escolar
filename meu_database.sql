CREATE TABLE aluno (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    cpf VARCHAR(11) UNIQUE NOT NULL,
    data_ingresso DATETIME NOT NULL
);

CREATE TABLE curso (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    carga_horaria INT NOT NULL,
    valor_inscricao DECIMAL(8,2) NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('ATIVO','INATIVO'))
);


CREATE TABLE matricula (
    id BIGINT PRIMARY KEY AUTO_INCREMENT,
    data_matricula DATE NOT NULL,
    status VARCHAR(20) NOT NULL CHECK (status IN ('PAGO','PENDENTE')),

    aluno_id BIGINT NOT NULL,
    curso_id BIGINT NOT NULL,

    CONSTRAINT fk_matricula_aluno FOREIGN KEY (aluno_id)
        REFERENCES aluno(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_matricula_curso FOREIGN KEY (curso_id)
        REFERENCES curso(id)
        ON DELETE CASCADE
);
