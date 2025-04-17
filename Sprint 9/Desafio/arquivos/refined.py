import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, explode

## @params: [JOB_NAME]
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'S3_INPUT_PATH_1', 'S3_INPUT_PATH_2', 'S3_TARGET_PATH'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file_1 = args['S3_INPUT_PATH_1']
source_file_2 = args['S3_INPUT_PATH_2']
target_path = args['S3_TARGET_PATH']

df1 = spark.read.parquet(source_file_1)
df2 = spark.read.parquet(source_file_2)

# Faz a junção usando as colunas de referência
join_condition = df1["id_imdb"] == df2["imdb_id"]
joined_df = df1.join(df2, join_condition, "inner")

# Explodir a coluna "genero_filme" para desaninhar
joined_df = joined_df.withColumn("genero_filme_exploded", explode("genero_filme"))

# Selecionar os campos do array desaninhado
joined_df = joined_df.withColumn("id_genero_filme", joined_df["genero_filme_exploded"]["id"].cast("string"))
joined_df = joined_df.withColumn("nome_genero_filme", joined_df["genero_filme_exploded"]["name"])

# Remover colunas intermediárias
joined_df = joined_df.drop("genero_filme", "genero_filme_exploded")

# Escrever o resultado em parquet
joined_df.write.mode("overwrite").parquet(target_path)

job.commit()
