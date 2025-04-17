# Use uma imagem base Python
FROM python:3.9-slim

# Copie os arquivos necessários para o contêiner
COPY . /app

# Defina o diretório de trabalho
WORKDIR /app

# Instale as dependências Python
RUN pip install --no-cache-dir boto3

# Comando de entrada padrão
CMD ["python", "main.py"]
