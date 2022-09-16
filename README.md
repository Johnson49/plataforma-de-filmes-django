# Play  Filmes

Uma plataforma de filmes com o framework django.

## Começando

### 1. Crie um ambiente virtual 

` pip -m venv venv`

<h4> Ative o ambiente virtual </h4>

Linux ou Mac: `source venv/bin/activate`

Windows: `venv/Script/activate `

### 2. Clone o projeto e instale as dependências

` git clone https://github.com/Johnson49/plataforma-de-filmes-django`

<h4> Instale as dependências com o pip: </h4>

` pip install -r requirements `


### 3. Crie o banco de dados

<h4> Realize o makemigrations:</h4>

`python manage.py makemigrations plataformaFilmes`


<h4> E então a migrate:</h4>

> Ao executar este comando, um arquivo de banco de dados SQLITE será criando na raiz do projeto.

`python manage.py migrate`

### 3. Crie um super usuário para acessar o painel administrativo

` python manage.py createsuperuser `

### 4. Inicie o servidor

` python manage.py runserver `






