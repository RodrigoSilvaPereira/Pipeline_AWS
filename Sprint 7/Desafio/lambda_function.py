import boto3  # Biblioteca para interagir com os serviços da AWS, como S3
import csv  # Biblioteca para manipular arquivos CSV
import json  # Biblioteca para manipular dados em formato JSON
from io import StringIO  # Biblioteca para manipulação de strings como arquivos
import requests  # Biblioteca para fazer requisições HTTP
from datetime import datetime  # Biblioteca para manipulação de datas e horas

# Função para processar registros de filmes e salvá-los no S3
def processar_registros(registros, chave_api, s3, bucket, data_atual):
    ids_processados = set()  # Conjunto para rastrear IDs de filmes já processados
    for row in registros:
        id_filme = row['id']  # ID do filme
        ano_lancamento = row['anoLancamento']  # Ano de lançamento do filme
        genero = row['genero']  # Gênero do filme

        if id_filme not in ids_processados:  # Verifica se o ID já foi processado
            ids_processados.add(id_filme)  # Adiciona o ID ao conjunto de processados

            # Verifica se o ano de lançamento é válido e se o gênero é 'Sci-Fi' ou 'Fantasy'
            if (ano_lancamento == '\\N' or (1980 <= int(ano_lancamento) <= 2023)) and (genero == 'Sci-Fi' or genero == 'Fantasy'):
                url = f'https://api.themoviedb.org/3/movie/{id_filme}?api_key={chave_api}'  # URL da API do TMDB para obter detalhes do filme
                #url = f'https://api.themoviedb.org/3/tv/{id_filme}?api_key={chave_api}'  # URL da API do TMDB para obter detalhes de séries (comentada)
                response = requests.get(url)  # Faz a requisição à API do TMDB

                # Verifica se a resposta da API é bem-sucedida e se contém dados
                if response.status_code == 200 and response.json():
                    dados_filme = response.json()  # Obtém os dados do filme em formato JSON
                    # Filtra os dados relevantes do filme
                    dados_filtrados = {key: dados_filme[key] for key in ["genres", "id", "imdb_id", "original_language",
                                                                        "original_title", "overview", "popularity", "release_date",
                                                                        "revenue", "runtime", "status", "title", "video",
                                                                        "vote_average", "vote_count"] if key in dados_filme}

                    # Determina o path no S3 com base no ano de lançamento
                    s3_path = f'Raw/TMDB/JSON/Movies/{data_atual}/unknown-year/{id_filme}.json' if ano_lancamento == '\\N' else \
                              f'Raw/TMDB/JSON/Movies/{data_atual}/{ano_lancamento}/{id_filme}.json'

                    # Salva os dados filtrados no S3
                    s3.put_object(Body=json.dumps(dados_filtrados), Bucket=bucket, Key=s3_path)

# Função handler para a AWS Lambda
def lambda_handler(event, context):
    chave_api = os.getenv('TMDB_API_KEY')  # É melhor usar variáveis de ambiente para maior segurança
    data_atual = datetime.utcnow().strftime("%Y/%m/%d")  # Data atual no formato YYYY/MM/DD
    bucket = 'data-lake-rodrigo'  # Nome do bucket no S3
    file_path = 'Raw/Local/CSV/movies/2024/05/31/movies.csv'  # Caminho do arquivo CSV no S3
    #file_path = 'Raw/Local/CSV/series/2024/05/31/series.csv'  # Caminho do arquivo CSV para séries (comentado)
    s3 = boto3.client('s3')  # Cliente do S3

    try:
        # Lê o arquivo CSV do S3
        arquivo_csv = s3.get_object(Bucket=bucket, Key=file_path)
        conteudo_csv = arquivo_csv['Body'].read().decode('utf-8')  # Decodifica o conteúdo do CSV

        registros = list(csv.DictReader(StringIO(conteudo_csv), delimiter='|'))  # Converte o conteúdo do CSV para uma lista de dicionários
        tamanho_lote = 100  # Tamanho do lote para processamento

        # Processa os registros em intervalos de 10 anos (de 1980 a 2023)
        for start_year in range(1980, 2024, 10):
            end_year = start_year + 9  # Define o intervalo de anos
            # Filtra os registros dentro do intervalo de anos
            registros_intervalo = [r for r in registros if r['anoLancamento'] == '\\N' or (start_year <= int(r['anoLancamento']) <= end_year)]

            # Processa os registros em lotes
            for i in range(0, len(registros_intervalo), tamanho_lote):
                lote = registros_intervalo[i:i + tamanho_lote]
                processar_registros(lote, chave_api, s3, bucket, data_atual)

        # Retorna uma resposta de sucesso
        return {
            'statusCode': 200,
            'body': 'Dados processados e salvos no S3 com sucesso.'
        }
    except Exception as e:
        # Em caso de erro, retorna uma resposta de erro
        return {
            'statusCode': 500,
            'body': f'Erro ao processar e salvar os dados no S3: {str(e)}'
        }
