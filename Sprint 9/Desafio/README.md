# Desafio Final: Projeto Final - Etapa 4 - AWS Glue e Parquet

Bem-vindo à Etapa 4 do Desafio Final do Curso de AWS! Nesta fase, vamos expandir nossas habilidades na manipulação de dados utilizando Data Catalog, Parquet e Athena. O objetivo é realizar o catálogo do arquivo refinado na Sprint passada, converter para um database no Athena e criar views para utilizar no QuickSight na Sprint 10.

## Estrutura do Projeto

├── querys.sql    # Código com as querys sql utilizadas no Athena

├── refined.py    # Código utilizado para criar a camada refined

└── README.md


## Descrição do Desafio

### Objetivo

O objetivo desta etapa é utilizar o AWS Glue e o AWS Athena para:

1. **Refinar Dados da Camada Trusted**: Unir dois arquivos Parquet de diferentes origens (TMDB e API) na camada Refined.
2. **Criação de Database e Tabelas no Athena**: Catalogar os dados refinados e criar tabelas para análise no Athena.
3. **Preparação de Views para o QuickSight**: Criar visualizações baseadas nas tabelas criadas para uso no QuickSight.

## Descrição dos Códigos

### refined.py

O código `refined` realiza as seguintes operações:

1. **Inicialização dos Contextos Spark e Glue**: Inicia as sessões do Spark e Glue para processamento de dados.

2. **Leitura de Arquivos Parquet do Amazon S3**: Lê os arquivos Parquet do S3 especificado como entrada.

3. **Junção e Transformação dos Dados**:
   - Realiza a junção dos dados de duas fontes diferentes (TMDB e API) usando colunas de referência.
   - Explode a coluna "genero_filme" para desaninhar os gêneros de cada filme.
   - Seleciona e renomeia colunas específicas para um formato mais consistente.

4. **Escrita dos Dados em Formato Parquet**: Salva os dados transformados em um bucket S3, particionando por data.

### Querys.sql

O arquivo `querys.sql` contém consultas SQL utilizadas no AWS Athena para manipulação dos dados refinados na camada REFINED do S3. As consultas principais são:

1. **Criação da Tabela de Métricas Principal (Tabela Fato)**:
   - Esta query cria a tabela `tb_metricas_filme`, que contém métricas importantes dos filmes, como nota média, popularidade, rendimento, entre outras.

2. **Criação da Tabela de Subgênero mais Frequente**:
   - A tabela `subgenero_frequente` é criada para mostrar a quantidade de filmes por subgênero, ordenados do mais frequente para o menos frequente.

3. **Criação da Tabela de Popularidade dos Filmes**:
   - A tabela `popularidade_filme` é criada para listar os filmes mais populares de cada subgênero, ordenados por popularidade.

4. **Criação da Tabela de Média de Votos do Subgênero Science Fiction**:
   - A tabela `media_votos_subgenero` calcula a média de votos para o subgênero "Science Fiction".

5. **Criação da Tabela de Frequência de Lançamento de Filmes do Subgênero Science Fiction**:
   - A tabela `frequencia_lancamento` mostra a frequência de lançamento de filmes do subgênero "Science Fiction" ao longo dos anos.

6. **Criação da Tabela da Métrica de Popularidade por Ano de Lançamento**:
   - A tabela `metrica_popularidade` calcula a média de popularidade dos filmes do subgênero "Science Fiction" por ano de lançamento.

Cada consulta é projetada para extrair insights específicos dos dados refinados, preparando-os para análise no QuickSight.

## Execução dos Códigos

### refined.py

Para executar os jobs de refined, siga os passos abaixo:

1. **Configurar Credenciais AWS**: Utilize o AWS CLI ou defina variáveis de ambiente para configurar suas credenciais AWS.
2. **Preparar os Arquivos Necessários**: Certifique-se de que os arquivos necessários para executar o `refined.py` estão no S3.
3. **Executar os Scripts no AWS Glue**: Utilize o AWS Glue para executar os scripts.

### Querys.sql

Para executar as Querys, siga os passos abaixo:

1. **Data Catalog**: Utilize o AWS Glue - Data Catalog no arquivo gerado pelo arquivo `refined.py`.
2. **Utilize o Serviço Athena**: Acesse o serviço Athena da AWS e verifique se a tabela foi criada.
3. **Execute os Scripts no Athena**: Execute os Scripts selecionando o seu Database criado.

## Evidências

É possível identificar evidências da execução do código em seu respectivo diretório [Evidencias](../Evidencias)
