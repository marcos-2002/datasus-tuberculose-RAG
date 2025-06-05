# Usa imagem base com Python 3.11.9
FROM python:3.11.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependências primeiro para aproveitar cache
COPY requirements.txt .

# Instala dependências do sistema e Python
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    postgresql-client \
    && pip install --upgrade pip \
    && pip install -r requirements.txt \
    && apt-get purge -y --auto-remove build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia todo o restante da aplicação
COPY . .

# Dá permissão de execução ao script de entrypoint
RUN chmod +x /app/docker-entrypoint.sh

RUN pip install watchgod

# Expõe a porta padrão
EXPOSE 8000

# Define o script de entrada como comando padrão
ENTRYPOINT ["/app/docker-entrypoint.sh"]
