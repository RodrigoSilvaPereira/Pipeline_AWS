# Desafio Final: Projeto em AWS S3

Bem-vindo ao Desafio Final do Curso de AWS S3! Este projeto demonstra as habilidades e competências desenvolvidas ao manipular serviços da Amazon, especificamente o S3, utilizando a biblioteca Boto3. O objetivo é realizar operações de leitura e manipulação de dados em um bucket S3, e executar uma consulta SQL em um arquivo CSV armazenado no bucket.

## Etapas do Projeto:

## Etapa 1: Leitura e Manipulação de Dados no S3

Nesta etapa, o desafio é desenvolver um código que leia um arquivo CSV armazenado em um bucket S3, execute uma consulta SQL nos dados utilizando a biblioteca pandasql, e salve os resultados em um novo arquivo CSV.

[Código Fonte](Etapa-1/main.ipynb)

[Base de Dados](Etapa-1/date/infracos_transito_07_2023.csv)

[Consulta SQL](Etapa-1/consulta.sql)

[Resultado Consulta](Etapa-1/consulta.csv)

### Estrutura do Projeto

├── Etapa-1

│   ├── main.ipynb              # Código fonte em Python

│   ├── data

│   │   └── infracos_transito_07_2023.csv    # Base de dados em formato CSV

│   ├── consulta.sql            # Arquivo com a consulta SQL

│   └── consulta.csv            # Resultado da consulta SQL

├── README.md                   # Documentação do projeto


### Descrição do Código

O código principal (main.ipynb) realiza as seguintes operações:

- Conexão com o serviço S3 utilizando Boto3.
- Upload de Arquivos necessários para execução do código
- Leitura do arquivo CSV a partir do bucket S3.
- Execução de uma consulta SQL nos dados utilizando pandasql.
- Salvamento do resultado da consulta em um novo arquivo CSV.

### Query SQL

A consulta SQL (consulta.sql) realiza as seguintes operações:

- Filtragem de dados utilizando dois operadores lógicos.
- Uso de duas funções de agregação.
- Utilização de uma função condicional.
- Conversão de tipos de dados.
- Manipulação de datas.
- Manipulação de strings.

### Execução do Código

Para executar o código, siga os passos abaixo:

- Configure suas credenciais AWS utilizando o AWS CLI ou definindo variáveis de ambiente.
- Certifique-se de que os arquivos necessários (main.py, consulta.sql, e o CSV de dados) estão no diretório correto.
- Execute o script main.ipynb para realizar as operações descritas.


## Conclusão

Este projeto demonstra a integração de serviços AWS S3 com Python e SQL para manipulação e análise de dados. Através deste desafio, você aprendeu a utilizar a biblioteca Boto3 para interagir com o S3, pandasql para executar consultas SQL em dataframes pandas, e a manipular os dados de forma eficiente.
