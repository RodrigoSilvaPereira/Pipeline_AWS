
-- CRIANDO TABELAS DO MODELO RELACIONAL 

/*
Cliente:

Descrição: Tabela que armazena informações dos clientes.
Campos:
idCliente: ID único do cliente (chave primária).
nomeCliente: Nome do cliente.
cidadeCliente: Cidade do cliente.
estadoCliente: Estado do cliente.
paisCliente: País do cliente.

 */

CREATE TABLE Cliente (
    idCliente INTEGER PRIMARY KEY,
    nomeCliente VARCHAR(100),
    cidadeCliente VARCHAR(100),
    estadoCliente VARCHAR(100),
    paisCliente VARCHAR(100)
)

/*
Carro:

Descrição: Tabela que armazena informações dos carros.
Campos:
idCarro: ID único do carro (chave primária).
kmCarro: Quilometragem do carro.
classiCarro: Classificação do carro.
marcaCarro: Marca do carro.
modeloCarro: Modelo do carro.
anoCarro: Ano do carro.
idCombustivel: ID do tipo de combustível do carro (chave estrangeira referenciando a tabela Combustivel).

 */

CREATE TABLE Carro (
    idCarro INTEGER PRIMARY KEY,
    kmCarro REAL,
    classiCarro VARCHAR(100),
    marcaCarro VARCHAR(100),
    modeloCarro VARCHAR(100),
    anoCarro INTEGER,
    idCombustivel INTEGER,
    FOREIGN KEY (idCombustivel) REFERENCES Combustivel(idCombustivel)
)

/*
Combustivel:

Descrição: Tabela que armazena os tipos de combustível disponíveis.
Campos:
idCombustivel: ID único do tipo de combustível (chave primária).
tipoCombustivel: Tipo de combustível.

 */

CREATE TABLE Combustivel (
    idCombustivel INTEGER PRIMARY KEY,
    tipoCombustivel VARCHAR(100)
)

/*
Locacao:

Descrição: Tabela que registra as locações de carros.
Campos:
idLocacao: ID único da locação (chave primária).
idCliente: ID do cliente associado à locação (chave estrangeira referenciando a tabela Cliente).
idCarro: ID do carro associado à locação (chave estrangeira referenciando a tabela Carro).
dataLocacao: Data da locação.
horaLocacao: Hora da locação.
qtdDiaria: Quantidade diária da locação.
vlrDiaria: Valor diário da locação.
dataEntrega: Data de entrega do carro.
horaEntrega: Hora de entrega do carro.
idVendedor: ID do vendedor associado à locação (chave estrangeira referenciando a tabela Vendedor).

 */

CREATE TABLE Locacao (
    idLocacao INTEGER PRIMARY KEY,
    idCliente INTEGER,
    idCarro INTEGER,
    dataLocacao DATE,
    horaLocacao TIME,
    qtdDiaria INTEGER,
    vlrDiaria REAL,
    dataEntrega DATE,
    horaEntrega TIME,
    idVendedor INTEGER,
    FOREIGN KEY (idCliente) REFERENCES Cliente(idCliente),
    FOREIGN KEY (idCarro) REFERENCES Carro(idCarro),
    FOREIGN KEY (idVendedor) REFERENCES Vendedor(idVendedor)
)

/*
Vendedor:

Descrição: Tabela que armazena informações dos vendedores.
Campos:
idVendedor: ID único do vendedor (chave primária).
nomeVendedor: Nome do vendedor.
sexoVendedor: Sexo do vendedor.
estadoVendedor: Estado do vendedor.

 */

CREATE TABLE Vendedor (
    idVendedor INTEGER PRIMARY KEY,
    nomeVendedor VARCHAR(100),
    sexoVendedor VARCHAR(100),
    estadoVendedor VARCHAR(100)
)

-- REALIZANDO A INSERÇÃO DE DADOS NO MODELO RELACIONAL 

/*
Foram realizadas inserções de dados nas tabelas Cliente, Carro, Combustivel, Locacao e Vendedor
para preencher os registros com informações relevantes.
 */

-- Inserções na tabela Cliente
INSERT INTO Cliente (nomeCliente, cidadeCliente, estadoCliente, paisCliente)
VALUES ('João Silva', 'São Paulo', 'SP', 'Brasil'),
       ('Maria Santos', 'Rio de Janeiro', 'RJ', 'Brasil'),
       ('Carlos Oliveira', 'Belo Horizonte', 'MG', 'Brasil'),
       ('Ana Costa', 'Salvador', 'BA', 'Brasil'),
       ('Fernanda Almeida', 'Porto Alegre', 'RS', 'Brasil'),
       ('Roberto Lima', 'Fortaleza', 'CE', 'Brasil'),
       ('Juliana Fernandes', 'Curitiba', 'PR', 'Brasil'),
       ('Lucas Pereira', 'Recife', 'PE', 'Brasil'),
       ('Mariana Vieira', 'Brasília', 'DF', 'Brasil'),
       ('Paulo Santos', 'Manaus', 'AM', 'Brasil')

-- Inserções na tabela Carro
INSERT INTO Carro (kmCarro, classiCarro, marcaCarro, modeloCarro, anoCarro, idCombustivel)
VALUES (50000, 'SUV', 'Toyota', 'RAV4', 2019, 1),
       (30000, 'Sedan', 'Honda', 'Civic', 2020, 2),
       (40000, 'Hatchback', 'Volkswagen', 'Golf', 2018, 3),
       (60000, 'SUV', 'Ford', 'EcoSport', 2017, 4),
       (20000, 'Sedan', 'Chevrolet', 'Cruze', 2021, 5),
       (35000, 'Hatchback', 'Renault', 'Sandero', 2019, 6),
       (45000, 'SUV', 'Hyundai', 'Creta', 2020, 7),
       (25000, 'Sedan', 'Nissan', 'Versa', 2018, 8),
       (55000, 'Hatchback', 'Fiat', 'Palio', 2017, 9),
       (15000, 'Sedan', 'Kia', 'Cerato', 2022, 10)

-- Inserções na tabela Combustivel
INSERT INTO Combustivel (idCombustivel, tipoCombustivel)
VALUES (1, 'Gasolina'),
       (2, 'Etanol'),
       (3, 'Diesel'),
       (4, 'Flex'),
       (5, 'Gás Natural'),
       (6, 'Elétrico'),
       (7, 'Híbrido'),
       (8, 'Biodiesel'),
       (9, 'GLP'),
       (10, 'Metanol')

-- Inserções na tabela Locacao
INSERT INTO Locacao (idCliente, idCarro, dataLocacao, horaLocacao, qtdDiaria, vlrDiaria, dataEntrega, horaEntrega, idVendedor)
VALUES (1, 1, '2024-04-01', '10:00:00', 3, 150.00, '2024-04-04', '10:00:00', 1),
       (2, 2, '2024-04-02', '09:00:00', 2, 120.00, '2024-04-04', '09:00:00', 2),
       (3, 3, '2024-04-03', '08:00:00', 4, 200.00, '2024-04-07', '08:00:00', 3),
       (4, 4, '2024-04-01', '11:00:00', 3, 160.00, '2024-04-04', '11:00:00', 4),
       (5, 5, '2024-04-02', '10:30:00', 2, 130.00, '2024-04-04', '10:30:00', 5),
       (6, 6, '2024-04-03', '09:30:00', 3, 170.00, '2024-04-06', '09:30:00', 6),
       (7, 7, '2024-04-01', '12:00:00', 4, 180.00, '2024-04-05', '12:00:00', 7),
       (8, 8, '2024-04-02', '11:30:00', 2, 140.00, '2024-04-04', '11:30:00', 8),
       (9, 9, '2024-04-03', '08:30:00', 3, 190.00, '2024-04-06', '08:30:00', 9),
       (10, 10, '2024-04-01', '13:00:00', 2, 110.00, '2024-04-03', '13:00:00', 10)

-- Inserções na tabela Vendedor
INSERT INTO Vendedor (nomeVendedor, sexoVendedor, estadoVendedor)
VALUES ('Pedro Oliveira', 'Masculino', 'SP'),
       ('Ana Souza', 'Feminino', 'RJ'),
       ('Marcos Santos', 'Masculino', 'MG'),
       ('Julia Costa', 'Feminino', 'BA'),
       ('Rafaela Lima', 'Feminino', 'RS'),
       ('Lucas Almeida', 'Masculino', 'CE'),
       ('Camila Fernandes', 'Feminino', 'PR'),
       ('Gustavo Pereira', 'Masculino', 'PE'),
       ('Mariana Vieira', 'Feminino', 'DF'),
       ('Bruno Silva', 'Masculino', 'AM')

       
-- CRIANDO SELECTS DO MODELO RELACIONAL
select * from Carro c 
select * from Cliente c 
Select * from Combustivel c 
select * from Locacao l 
Select * from Vendedor v


