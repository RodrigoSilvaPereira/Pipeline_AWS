import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.job import Job
from datetime import datetime

# @params: [JOB_NAME, S3_INPUT_PATH, S3_TARGET_PATH]
# Pega os parâmetros passados para o script (nome do job, caminho de entrada e caminho de saída no S3)
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH', 'S3_TARGET_PATH'])

# Inicializa os contextos do Spark e Glue
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Função para extrair a data do caminho S3
def extract_date_from_s3_path(s3_path):
    # Exemplo de caminho de entrada: s3://data-lake-rodrigo/Raw/TMDB/JSON/Movies/2024/06/14/*/*.json
    path_components = s3_path.split('/')
    year, month, day = None, None, None
    for component in path_components:
        try:
            year = int(component)
            if year >= 2000 and year <= 2100:  # Assumindo um intervalo de anos razoável para particionamento de dados
                month = int(path_components[path_components.index(str(year)) + 1])
                day = int(path_components[path_components.index(str(year)) + 2])
                return datetime(year, month, day).strftime('%Y-%m-%d')
        except ValueError:
            continue
    raise ValueError("Data não encontrada no caminho S3.")

# Extrai a data do caminho S3 de entrada
date_from_path = extract_date_from_s3_path(args['S3_INPUT_PATH'])

# Lê os arquivos JSON
df = spark.read.option("multiline", "true").json(args['S3_INPUT_PATH'])

# Lista das colunas a serem excluídas
columns_to_drop = [
    "backdrop_path", "homepage", "id", "original_title", "poster_path", "video",
]

# Excluir as colunas especificadas
df = df.drop(*columns_to_drop)

# Renomear colunas
column_rename_map = {
    "release_date": "data_lancamento_filme",
    "adult": "filme_conteudo_adulto",
    "belongs_to_collection": "pertence_coletanea",
    "budget": "orcamento_filme",
    "genres": "genero_filme",
    "imdb_id": "imdb_id",
    "original_language": "idioma_original_filme",
    "overview": "enredo_filme",
    "popularity": "popularidade_filme",
    "production_companies": "produtora_filme",
    "production_countries": "pais_producao",
    "revenue": "rendimento_filme",
    "runtime": "tempo_execucao_filme",
    "spoken_languages": "idioma_falado_filme",
    "status": "situacao_filme",
    "tagline": "tagline_filme",
    "title": "titulo_filme",
    "vote_average": "media_votos_filme",
    "vote_count": "contagem_votos_filme",
}

for old_col, new_col in column_rename_map.items():
    df = df.withColumnRenamed(old_col, new_col)

# Coalesce para uma única partição
single_part_df = df.coalesce(1)

# Escrever o DataFrame resultante no formato Parquet
parquet_output_path = f"{args['S3_TARGET_PATH']}/date={date_from_path}"
single_part_df.write.parquet(parquet_output_path, mode='overwrite')

# Comitar o job
job.commit()
