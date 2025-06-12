# Análise de Tuberculose - Backend

Este projeto tem como objetivo auxiliar pesquisadores da área da saúde, especialmente pesquisadores que realizam estudos epidemiologicos sobre o perfil da tubercolose, a desenvolverem suas pesquisas de uma forma facilitada.

## Pré Requisitos

1. Docker instalado

   Se você não possui o docker instalado, visite https://www.docker.com/get-started/

2. Chave de API do Gemini

   Se você não tem uma chave de API, visite https://aistudio.google.com/app/apikey (não se preocupe, o Gemini possui limite gratuito)

3. yarn ou npm

## Como começar

1. Clone o repositório:

   ```bash
   git clone https://github.com/thiago1591/tuberculosis-analysis
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd tuberculosis-analysis
   ```

3. Crie o arquivo .env

   ```cp .env.example .env``` (linux/mac)


   ```copy .env.example .env``` (windows)

   Coloque a sua chave de API do Gemini em LLM_KEY

4. Rode o Docker
   ```bash
      docker compose up
   ```

   Esse comando irá subir o banco de dados e a API

5. Rode as seeds
   ```bash
    docker exec -it api python3 seed_data.py
   ```

6. Rode o frontend (no windows use copy em vez de cp)
   ```bash
      cd frontend
      cp .env.example .env
      yarn install
      yarn dev
   ```

