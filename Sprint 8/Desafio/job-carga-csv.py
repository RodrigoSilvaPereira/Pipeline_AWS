import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
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
    # Exemplo de caminho de entrada: s3://data-lake-rodrigo/Raw/Local/CSV/movies/2024/05/31/movies.csv
    path_components = s3_path.split('/')
    # Itera pelos componentes do caminho para encontrar ano, mês e dia
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

# Lê o arquivo CSV com delimitador '|'
df = spark.read.option("header", "true").option("delimiter", "|").csv(args['S3_INPUT_PATH'])

# Filtra pelo gênero 'Sci-Fi' ou 'Fantasy'
filtered_df = df.filter((df['genero'] == 'Sci-Fi') | (df['genero'] == 'Fantasy'))

# Seleciona as colunas que devem ser mantidas
columns_to_keep = [
    "generoArtista",
    "nomeArtista",
    "notaMedia",
    "personagem",
    "profissao",
    "anoFalecimento",
    "numeroVotos",
    "anoNascimento",
    "id"
]

selected_df = filtered_df.select(*columns_to_keep)

# Renomeia as colunas
renamed_df = selected_df.withColumnRenamed("generoArtista", "genero_artista") \
                       .withColumnRenamed("nomeArtista", "nome_artista") \
                       .withColumnRenamed("notaMedia", "nota_media_filme") \
                       .withColumnRenamed("personagem", "personagem_artista") \
                       .withColumnRenamed("profissao", "profissao_artista") \
                       .withColumnRenamed("anoFalecimento", "ano_falecimento_artista") \
                       .withColumnRenamed("numeroVotos", "numero_votos_filme") \
                       .withColumnRenamed("anoNascimento", "ano_nascimento_artista") \
                       .withColumnRenamed("id", "id_imdb")

# Coalesce para uma única partição
single_part_df = renamed_df.coalesce(1)

# Escreve o DataFrame resultante no formato Parquet
parquet_output_path = f"{args['S3_TARGET_PATH']}/date={date_from_path}"
single_part_df.write.parquet(parquet_output_path, mode='overwrite')

# Comita o job
job.commit()
