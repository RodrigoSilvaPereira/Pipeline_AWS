# Desafio Final: Projeto Final - Etapa 2 - AWS S3

Bem-vindo ao Desafio Final do Curso de AWS S3! Este projeto demonstra as habilidades e competências desenvolvidas ao manipular serviços da Amazon, especificamente o S3, utilizando a biblioteca Boto3. O objetivo é realizar operações de leitura de arquivos CSV, fazer requisições à API do TMDB, e salvar os dados processados no bucket S3.

## Etapas do Projeto:

### Etapa 1: Processamento e Upload de Dados no S3

Nesta etapa, o desafio é desenvolver um código que leia arquivos CSV armazenados no S3, faça requisições à API do TMDB para obter detalhes dos filmes, filtre os dados relevantes e faça o upload dos dados processados para um bucket S3, organizando-os com base na data de processamento e ano de lançamento.

[Código Fonte](lambda_function.py)

### Descrição do Código

O código principal (lambda_function.py) realiza as seguintes operações:

- Leitura de arquivos CSV armazenados no S3.
- Filtragem dos registros com base no ano de lançamento e gênero.
- Requisições à API do TMDB para obter detalhes dos filmes.
- Upload dos dados filtrados para o bucket S3, organizando-os com base na data de processamento e ano de lançamento.

### Execução do Código

Para executar o código, siga os passos abaixo:

- Configure suas credenciais AWS utilizando o AWS CLI ou definindo variáveis de ambiente.
- Certifique-se de que os arquivos necessários (lambda_function.py e os CSVs de dados) estão no diretório correto no S3.
- Configure a função Lambda na AWS para utilizar o script lambda_function.py.
- Execute a função Lambda para realizar as operações descritas.

### Configuração da AWS Lambda

1. Faça login na AWS Management Console e vá para o serviço Lambda.
2. Crie uma nova função Lambda e faça o upload do script `lambda_function.py`.
3. Configure as permissões da função para permitir acesso ao S3.
4. Defina as variáveis de ambiente necessárias para o script, como a chave da API do TMDB e o nome do bucket S3.
5. Teste a função com um evento de teste adequado e verifique os logs para garantir que os dados estão sendo processados e salvos corretamente.

## Conclusão

Este projeto demonstra a integração de serviços AWS S3 com Python para manipulação e upload de dados. Através deste desafio, você aprendeu a utilizar a biblioteca Boto3 para interagir com o S3 e a manipular os dados de forma eficiente.
