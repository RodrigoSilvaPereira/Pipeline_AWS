# Desafio Final: Projeto Final - Etapa 3 - AWS Glue e Parquet

Bem-vindo à Etapa 3 do Desafio Final do Curso de AWS! Nesta fase, vamos expandir nossas habilidades na manipulação de dados utilizando AWS Glue, Spark e arquivos Parquet. O objetivo é criar jobs de ETL (Extract, Transform, Load) para transformar e carregar dados CSV e JSON em formato Parquet no Amazon S3.

## Estrutura do Projeto

├── job-carga-csv    # Código para job de carga de dados CSV

│    

├── job-carga-dados-tmdb   # Código para job de carga de dados TMDB

│

│───│ Teste_parquet  

│   │   ├── CSV

│   │   │   └── arquivo.parquet

│   │   └── TMDB

│   │       └── arquivo.parquet

│   └── Teste_Job.py    # Código para teste de leitura de arquivos Parquet

│

└── README.md


## Descrição do Desafio

### Objetivo

O objetivo desta etapa é desenvolver jobs de ETL utilizando AWS Glue e Spark para:

1. **Ler dados CSV do Amazon S3**: Carregar arquivos CSV do S3, transformá-los e armazená-los no formato Parquet.
2. **Ler dados JSON do Amazon S3**: Carregar arquivos JSON do S3, transformá-los e armazená-los no formato Parquet.
3. **Testar a leitura de arquivos Parquet**: Garantir que os dados transformados podem ser lidos corretamente.

## Descrição dos Códigos

### job-carga-csv

O código `job-carga-csv` realiza as seguintes operações:

1. **Inicialização dos Contextos Spark e Glue**: Criação das sessões do Spark e Glue para processamento dos dados.
2. **Leitura de Arquivos CSV do Amazon S3**: Utiliza o caminho de entrada especificado para ler arquivos CSV.
3. **Filtragem e Transformação dos Dados**: 
   - Filtra dados com os gêneros 'Sci-Fi' ou 'Fantasy'.
   - Seleciona colunas específicas e renomeia-as para um formato mais consistente.
4. **Escrita dos Dados em Formato Parquet**: Armazena os dados transformados em um bucket S3, particionando por data.

### job-carga-dados-api.py

O código `job-carga-dados-api.py` realiza as seguintes operações:

1. **Inicialização dos Contextos Spark e Glue**: Criação das sessões do Spark e Glue para processamento dos dados.
2. **Leitura de Arquivos JSON do Amazon S3**: Utiliza o caminho de entrada especificado para ler arquivos JSON.
3. **Transformação e Limpeza dos Dados**: 
   - Exclui colunas desnecessárias.
   - Renomeia colunas para um formato mais descritivo.
4. **Escrita dos Dados em Formato Parquet**: Armazena os dados transformados em um bucket S3, particionando por data.

### Teste_Job.py

O código `Teste_Job.py` realiza as seguintes operações:

1. **Inicialização de uma SparkSession**: Criação de uma sessão Spark para leitura dos dados.
2. **Leitura de Arquivos Parquet**: Lê arquivos Parquet de um caminho especificado.
3. **Exibição de Dados**: Mostra os primeiros 20 registros do DataFrame.
4. **Exibição do Esquema do DataFrame**: Exibe a estrutura do DataFrame lido.
5. **Contagem de Linhas**: Conta o número de linhas no DataFrame e exibe o resultado.

## Execução dos Códigos

### job-carga-csv e job-carga-dados-api.py

Para executar os jobs de ETL, siga os passos abaixo:

1. **Configurar Credenciais AWS**: Utilize o AWS CLI ou defina variáveis de ambiente para configurar suas credenciais AWS.
2. **Preparar os Arquivos Necessários**: Certifique-se de que os arquivos `job-carga-csv` e `job-carga-dados-api.py` estão no diretório correto.
3. **Executar os Scripts no AWS Glue**: Utilize o AWS Glue para executar os scripts.

### Teste_Job.py

Para testar a leitura dos arquivos Parquet, siga os passos abaixo:

1. **Verificar Caminho dos Arquivos Parquet**: Certifique-se de que os arquivos Parquet estão no caminho correto.
2. **Executar o Script**: Execute o script `Teste_Job.py` para ler e visualizar os dados.

## Evidências

É possível identificar evidências da execução do código em seu respectivo diretório [Evidencias](../Evidencias)
