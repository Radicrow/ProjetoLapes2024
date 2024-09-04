# Startup API - Processo Seletivo LAPES





Esta API foi desenvolvida como parte do processo seletivo para o LAPES - Laboratório de Pesquisa de Engenharia de Software do CESUPA. Ela permite consultar dados sobre startups, utilizando um backend construído em um framework chamado FastAPI e a base de dados fornecida pelo processo em .CSV
## Estrutura do Projeto
- main: Contém a implementação das rotas da API.
- models: Define o modelo ORM para a base de dados das startups utilizando sqlalchemy e sqlite.
- database: Configura e gerencia a conexão com o banco de dados SQLite (startups.db).
- startup data.csv: Arquivo CSV contendo os dados das startups.
- startups.db: Banco de dados SQLite gerado a partir do CSV.
- requirements.txt: Arquivo com as dependências do projeto.

## Features:

### Root:
- Rota: ./
- Mostra uma mensagem de boas vindas à API.
  
### Listar Startups:
- Rota: ./startups/{page_num}
- Retorna uma lista paginada de startups.

### Buscar Startup por Nome:

- Rota: ./startups/name/{startup_name}
- Busca uma startup pelo seu nome.

### Buscar Startup por ID:

- Rota: ./startups/id/{startup_id}
- Busca uma startup pelo seu ID único.

### Buscar Startups por Cidade:

- Rota: ./startups/city/{city}
- Retorna todas as startups localizadas em uma cidade específica.

### Buscar Startups por Estado:
- Rota: ./startups/state/{state_code}
- Retorna todas as startups localizadas em um estado específico.

## Pré-Requisitos
- Python 3.8 ou superior
- pip (Python package installer)

## Como Executar
- Clone o Repositório:
> git clone https://github.com/Radicrow/ProjetoLapes2024.git
>
> cd ProjetoLapes2024
- Crie e ative o Venv
> python3 -m venv .venv
> 
> .venv\Scripts\activate
- Instale as dependêcias listadas no arquivo "requirements.txt"
> pip install -r requirements.txt
- Coloque o arquivo CSV  contendo os dados das startups na pasta do projeto.
- Inicie o servidor com o comando:
> uvicorn main:app --reload
- E acesse a API na porta http://127.0.0.1:8000

Você também pode acessar a documentação interativa utilizando
> http://127.0.0.1:8000/docs


