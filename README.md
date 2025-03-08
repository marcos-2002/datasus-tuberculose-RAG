# Análise de Tuberculose - Backend

Este projeto em Python é responsável por executar o processo de ETL (Extract, Transform, Load) para a importação de dados do datasus em diversos anos, referente a turbeculose. O objetivo é popular uma base de dados com dados estruturados e fornecer endpoints de consulta, para possibilitar a criação de um sistema web interativo.

## Tecnologias utilizadas

- Python: Linguagem principal usada para desenvolvimento do ETL.
- Flask: Microframework web usado para criar endpoints de API
- Tortoise ORM: Ele permite que você interaja com bancos de dados usando classes e objetos Python em vez de SQL direto, facilitando o desenvolvimento e a manutenção de aplicativos.
- Postgres: Banco de dados para armazenamento principal dos dados.

## Como começar

1. Clone o repositório:

   ```bash
   git clone https://github.com/thiago1591/tuberculosis-analysis
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd tuberculosis-analysis
   ```

3. Crie um ambiente virtual e ative-o:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows use `venv\Scripts\activate`
   ```

4. Instale as dependências:

   ```bash
   pip3 install -r requirements.txt
   ```

5. Rodar as migrations:

   ```bash
   aerich migrate
   ```

6. Iniciar a API:

   ```bash
   hypercorn run:app --bind 127.0.0.1:5000
   ```

## Banco de dados

Para mais informações, consulte a documentação do [aerich](https://github.com/tortoise/aerich).

- Executar as migrations:

  ```bash
  aerich upgrade
  ```

- Criar uma nova migration:

  ```bash
  aerich migrate --name name_of_migration
  ```

- Inicializar o banco (apenas uma vez caso não tenha migrations)

  ```bash
  aerich init-db
  ```