#!/bin/bash
set -e

echo "Aguardando o banco de dados iniciar..."

# Aguarda o banco responder na porta 5432
until pg_isready -h $DB_HOST -p $DB_PORT -U $DB_USER; do
  sleep 1
done

echo "Banco de dados pronto. Rodando migrações..."

# Aplica as migrações existentes
aerich upgrade

echo "Iniciando servidor..."
exec hypercorn run:app --bind 0.0.0.0:8000 --reload
