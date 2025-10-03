# Dockerfile
FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Dependências do sistema (se precisar de compilar libs, adicione aqui)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY . .

# Criar diretórios de static e media para coletar/servir arquivos
RUN mkdir -p /app/staticfiles /app/media

# Comando padrão: gunicorn (ajustado no docker-compose para esperar DB)
CMD ["gunicorn", "TrucSite.wsgi:application", "--bind", "0.0.0.0:8000"]
