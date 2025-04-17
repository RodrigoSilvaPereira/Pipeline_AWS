# Desafio Final: Projeto Final - Etapa 1 - AWS S3

Bem-vindo ao Desafio Final do Curso de AWS S3! Este projeto demonstra as habilidades e competências desenvolvidas ao manipular serviços da Amazon, especificamente o S3, utilizando a biblioteca Boto3. O objetivo é realizar operação de criação de um bucket S3 e fazer upload de arquivos CSV em uma estrutura complexa de diretórios.

## Etapas do Projeto:

## Etapa 1: Criação de Bucket e Upload de Arquivos no S3

Nesta etapa, o desafio é desenvolver um código que crie um bucket no Amazon S3, leia arquivos CSV armazenados localmente e faça o upload desses arquivos para o bucket criado, organizando-os com base na data de processamento.

[Código Fonte](main.py)

Os dados foram compactados para hospedagem no github, necessário descompactar para executar.

[Base de Dados](Data/Data.rar)

### Estrutura do Projeto

├── main.py     # Código fonte em Python

├── Data

│ ├── movies.csv     # Base de dados em formato CSV

│ └── series.csv     # Base de dados em formato CSV

├── Dockerfile   # Dockerfile para criar o ambiente de execução

├── README.md   # Documentação do projeto


### Descrição do Código

O código principal (main.py) realiza as seguintes operações:

- Criação de um bucket no Amazon S3 utilizando Boto3.
- Leitura de arquivos CSV localmente.
- Upload dos arquivos CSV para o bucket S3, organizando-os com base na data de processamento.

### Execução do Código

Para executar o código, siga os passos abaixo:

- Configure suas credenciais AWS utilizando o AWS CLI ou definindo variáveis de ambiente.
- Certifique-se de que os arquivos necessários (main.py e os CSVs de dados) estão no diretório correto.
- Execute o script main.py para realizar as operações descritas.

### Dockerfile

O projeto inclui um Dockerfile que configura o ambiente necessário para executar o código. Para construir e executar o contêiner Docker, utilize os seguintes comandos:

```sh
docker volume create FilmesSeries-vol
docker build -t data-lake-rodrigo .
docker run -v FilmesSeries-vol:/FilmesSeries -v C:/Users/Rodrigo/.aws:/root/.aws data-lake-rodrigo
```


## Conclusão

Este projeto demonstra a integração de serviços AWS S3 com Python para manipulação e upload de dados. Através deste desafio, você aprendeu a utilizar a biblioteca Boto3 para interagir com o S3 e a manipular os dados de forma eficiente.
