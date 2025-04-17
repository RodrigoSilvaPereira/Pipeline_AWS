# Entregas do Desafio Final

Bem-vindo ao repositório do Desafio Final do Estágio! Aqui você encontrará todas as entregas referentes ao desafio final, que é uma parte integrante de cada sprint ao longo do período de estágio.

Este projeto consiste na criação de um banco de dados dimensional para uma concessionária de veículos. O objetivo é fornecer uma estrutura de dados otimizada para análise e consulta de informações relacionadas às locações de veículos, clientes, carros e vendedores.

## O projeto é composto por categorias principais:

- Modelagem Relacional: Inicialmente, foi criado um modelo relacional que representa as entidades e seus relacionamentos. Esse modelo foi implementado utilizando a linguagem SQL em um banco de dados SQLite.

- Modelagem Dimensional: Em seguida, o modelo relacional foi transformado em um modelo dimensional para otimizar a consulta e análise dos dados. Foram criadas views físicas que representam dimensões (clientes, carros, vendedores) e uma tabela de fatos (locações).

- Documentação: Todo o processo foi documentado e este README.md contém informações sobre a estrutura do banco de dados, as views físicas criadas e instruções para uso e manutenção do projeto.

### Uso do Projeto:

Para utilizar o projeto, siga estas etapas:

Faça o download dos arquivos do repositório.
Execute os scripts SQLite e SQL para criar o banco de dados e inserir os dados.
Utilize as views físicas para consultar e analisar os dados conforme necessário.

### Ferramentas Utilizadas:

DBeaver SQLite: Banco de dados utilizado para implementação do modelo relacional e dimensional.
brModelo: Ferramenta utilizada para criação dos diagramas e documentação do projeto.
MySql Workbench: Para criação de modelos lógicos do banco de dados relacional e dimensional.

## Etapas

### Etapa I:

#### Modelo Relacional do Banco de Dados:

Este projeto inclui um modelo relacional para um banco de dados de uma concessionária de carros. O modelo foi projetado para armazenar informações sobre clientes, carros, vendedores e locações.

Tabelas:

Cliente - Armazena detalhes dos clientes, como nome, cidade, estado e país.

Carro - Contém informações sobre os carros disponíveis para locação, como quilometragem, classificação, marca, modelo, ano e tipo de combustível.

Combustivel - Lista os tipos de combustível disponíveis para os carros.

Locacao - Registra as transações de locação de carros, incluindo detalhes como data, hora, quantidade diária e valor.

Vendedor - Mantém informações sobre os vendedores da concessionária, como nome, sexo e estado.

Relacionamentos:

- A tabela Locacao possui chaves estrangeiras para Cliente, Carro e Vendedor, representando a associação entre uma locação e os clientes, carros e vendedores envolvidos.
- A tabela Carro tem uma chave estrangeira que referencia a tabela Combustivel, indicando o tipo de combustível utilizado pelo carro.
Este modelo relacional fornece uma estrutura organizada para armazenar e gerenciar os dados relacionados às operações da concessionária de carros.

[Etapa I](etapa-1/concessionaria_relacional.sql)

### Etapa II:

#### Modelo Dimensional do Banco de Dados com Views

O modelo dimensional foi projetado para facilitar a análise de dados e consultas complexas. Ele consiste em três dimensões principais (clientes, carros, vendedores) e uma tabela de fatos (locações).

As dimensões representam os aspectos principais do negócio, como clientes, carros e vendedores, enquanto a tabela de fatos contém métricas e medidas relacionadas às locações, como datas, quantidades e valores.

Views Físicas:
Para implementar o modelo dimensional, foram criadas views físicas que representam cada dimensão e a tabela de fatos. As views foram projetadas para fornecer uma visualização conveniente dos dados e facilitar consultas complexas.

[Etapa II](etapa-2/concessionaria_dimensional.sql)

Continue acompanhando este README.md para atualizações e novas entregas conforme avançamos nas etapas subsequentes do desafio final.