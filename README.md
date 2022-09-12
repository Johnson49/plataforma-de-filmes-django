# Play  Filmes

> Status do Projeto: ⚠️ Em desenvolvimento.

## Informações gerais
Uma plataforma de filmes com o framework django no backend.

## Tecnologias
> O projeto é criado com:

* Python 3.10
* Django

## Setup

> Para rodar este projeto, clone localmente e depois instale as dependências com um gerenciador de sua preferência.

1. Clone este repositório  e `cd` no diretório do repositório
2. Crie um ambiente virtual com o seguinte comando: `python -m venv venv`
3. Instale as dependências com: `pip install -r requirements `
4. Execute o servidor com : `python manage.py runserver`

## Models

### Filme
- título 
- gênero
- descrição 
- duração
- ano de lançamento
- url da imagem


### Avaliação do filme
- filme 
- nome do usuário
- email do usuário
- comentário
- avaliação


## Planejamento

- [x] Criar a tabela de filme
- [x] Criar a tabela de avaliações
- [] Criar a tabela de usuarios
- [] Definir as regras de negócios
- [] Definir as regras de segurança
- [] Integra Angular com django
