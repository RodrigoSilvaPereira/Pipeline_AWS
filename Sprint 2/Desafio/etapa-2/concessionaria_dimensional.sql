/*
DimCliente

Descrição: Esta view representa uma dimensão para clientes, contendo informações
 como ID do cliente, nome, cidade, estado e país.

Campos:
idCliente: ID único do cliente.
nomeCliente: Nome do cliente.
cidadeCliente: Cidade do cliente.
estadoCliente: Estado do cliente.
paisCliente: País do cliente.
*/

-- View de dimensão para Cliente
CREATE VIEW DimCliente AS
SELECT idCliente, nomeCliente, cidadeCliente, estadoCliente, paisCliente
FROM Cliente

/*
DimCarro

Descrição: Esta view representa uma dimensão para carros, incluindo informações
como ID do carro, quilometragem, classificação, marca, modelo, ano e tipo de combustível.

Campos:
idCarro: ID único do carro.
kmCarro: Quilometragem do carro.
classiCarro: Classificação do carro.
marcaCarro: Marca do carro.
modeloCarro: Modelo do carro.
anoCarro: Ano do carro.
tipoCombustivel: Tipo de combustível do carro.
*/

-- View de dimensão para Carro
CREATE VIEW DimCarro AS
SELECT c.idCarro, c.kmCarro, c.classiCarro, c.marcaCarro, c.modeloCarro, c.anoCarro, co.tipoCombustivel
FROM Carro c
JOIN Combustivel co ON c.idCombustivel = co.idCombustivel

/*
DimVendedor

Descrição: Esta view representa uma dimensão para vendedores, incluindo informações 
como ID do vendedor, nome, sexo e estado.

Campos:
idVendedor: ID único do vendedor.
nomeVendedor: Nome do vendedor.
sexoVendedor: Sexo do vendedor.
estadoVendedor: Estado do vendedor.
*/

-- View de dimensão para Vendedor
CREATE VIEW DimVendedor AS
SELECT idVendedor, nomeVendedor, sexoVendedor, estadoVendedor
FROM Vendedor

/*
FatoLocacao
Descrição: Esta view representa uma tabela de fatos para locações, contendo informações 
sobre as transações de locação de carros.

Campos:
idLocacao: ID único da locação.
idCliente: ID do cliente associado à locação.
idCarro: ID do carro associado à locação.
idVendedor: ID do vendedor associado à locação.
dataLocacao: Data da locação.
horaLocacao: Hora da locação.
qtdDiaria: Quantidade diária da locação.
vlrDiaria: Valor diário da locação.
dataEntrega: Data de entrega do carro.
horaEntrega: Hora de entrega do carro.
*/

-- View de fato para Locacao
CREATE VIEW FatoLocacao AS
SELECT l.idLocacao, 
       c.idCliente, 
       ca.idCarro, 
       v.idVendedor,
       l.dataLocacao, 
       l.horaLocacao, 
       l.qtdDiaria, 
       l.vlrDiaria, 
       l.dataEntrega, 
       l.horaEntrega
FROM Locacao l
JOIN Cliente c ON l.idCliente = c.idCliente
JOIN Carro ca ON l.idCarro = ca.idCarro
JOIN Vendedor v ON l.idVendedor = v.idVendedor

/*
Exemplos de consultas para recuperar dados das views criadas:

-- DimCliente: Retorna todas as informações sobre os clientes.
-- DimCarro: Retorna todas as informações sobre os carros.
-- DimVendedor: Retorna todas as informações sobre os vendedores.
-- FatoLocacao: Retorna todas as informações sobre as locações de carros.
 */

-- Exemplo de chamada da view DimCliente
SELECT * FROM DimCliente

-- Exemplo de chamada da view DimCarro
SELECT * FROM DimCarro

-- Exemplo de chamada da view DimVendedor
SELECT * FROM DimVendedor

-- Exemplo de chamada da view FatoLocacao
SELECT * FROM FatoLocacao