from pyspark.sql import SparkSession

# Inicializa a SparkSession
spark = SparkSession.builder.appName("ReadParquet").getOrCreate()

# Caminho para o arquivo Parquet baixado
#parquet_file_path = "CSV/part-00000-8a9405af-eacd-417a-a2d2-414cfeca1a7f-c000.snappy.parquet"
#parquet_file_path = "TMDB/part-00000-8555bb5a-2714-4fea-a123-530108d640fb-c000.snappy.parquet"
parquet_file_path = "Refine/part-00000-a02bf9a2-7cb0-43bf-ba8c-f633a43b997d-c000.snappy.parquet"

# Lê o arquivo Parquet
df = spark.read.parquet(parquet_file_path)

# Mostra os primeiros 20 registros
df.show()

# Exibir o esquema do DataFrame
df.printSchema()

# Contar o número de linhas no DataFrame
row_count = df.count()
print(f"Número de linhas no DataFrame: {row_count}")
