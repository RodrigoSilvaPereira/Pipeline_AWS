import os
import csv
import datetime
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError


def create_s3_bucket(bucket_name, region=None):
    try:
        # Inicializa a sessão e o cliente S3 usando o perfil configurado
        session = boto3.Session(profile_name="default")
        s3_client = session.client("s3", region_name=region)

        # Cria o bucket com a região especificada
        if region is None or region == "us-east-1":
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            location = {"LocationConstraint": region}
            s3_client.create_bucket(
                Bucket=bucket_name, CreateBucketConfiguration=location
            )

        print(f"Bucket '{bucket_name}' criado com sucesso.")

    except NoCredentialsError:
        print("Credenciais não encontradas.")
    except PartialCredentialsError:
        print("Credenciais incompletas.")
    except ClientError as e:
        print(f"Ocorreu um erro ao tentar criar o bucket: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Criando o bucket
bucket_name = "data-lake-rodrigo"
region = "us-east-1"
create_s3_bucket(bucket_name, region)


def read_csv(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data


def upload_file_to_s3(bucket_name, file_path, object_name=None):
    try:
        session = boto3.Session(profile_name="default")
        s3_client = session.client("s3")

        if object_name is None:
            object_name = os.path.basename(file_path)

        # Obtendo a data de processamento para construir o caminho
        processing_date = datetime.datetime.now().strftime("%Y/%m/%d")
        # Construindo o caminho do arquivo no S3
        file_name = os.path.splitext(object_name)[0]  # Remove a extensão do arquivo
        s3_key = f"Raw/Local/CSV/{file_name}/{processing_date}/{object_name}"

        s3_client.upload_file(file_path, bucket_name, s3_key)

        print(f"Arquivo '{file_path}' enviado para o bucket '{bucket_name}' como '{s3_key}'.")

    except NoCredentialsError:
        print("Credenciais não encontradas.")
    except PartialCredentialsError:
        print("Credenciais incompletas.")
    except ClientError as e:
        print(f"Ocorreu um erro ao tentar enviar o arquivo: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Upload dos arquivos
upload_file_to_s3(bucket_name, 'Data/movies.csv', 'movies.csv')
upload_file_to_s3(bucket_name, 'Data/series.csv', 'series.csv')
