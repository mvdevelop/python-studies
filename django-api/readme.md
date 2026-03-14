
## 📚 Biblioteca API
Uma API robusta para gerenciamento de livros desenvolvida em Python utilizando o framework Django. O projeto segue o padrão de arquitetura MVC (Model-View-Controller), adaptado ao estilo MVT (Model-View-Template/Task) do Django para o desenvolvimento de APIs.

## 🚀 Tecnologias Utilizadas
Python 3.x
Django (Framework Web)
Django REST Framework (Para construção da API)
SQLite (Banco de dados padrão)
Venv (Ambiente Virtual)

## 📂 Estrutura do Projeto (MVC)
O projeto está organizado da seguinte forma:
text
biblioteca_api/
├── core/                # Configurações centrais do Django
├── livros/              # App principal (O "Coração" da API)
│   ├── models/          # M - Models (Definição do Banco de Dados)
│   ├── views.py         # V - Views/Controllers (Lógica de Negócio)
│   ├── serializers.py   # Transformação de dados (JSON)
│   └── urls.py          # Roteamento de endpoints
├── manage.py
├── .env                 # Variáveis de ambiente (não versionado)
└── requirements.txt     # Dependências do projeto
Use o código com cuidado.

## 🛠️ Como Configurar o Projeto
Siga os passos abaixo para rodar o projeto localmente:
1. Clonar o repositório
bash
git clone https://github.com
cd biblioteca-api
Use o código com cuidado.

2. Configurar o Ambiente Virtual (Windows)
powershell
python -m venv .venv
.\.venv\Scripts\activate
Use o código com cuidado.

3. Instalar as dependências
bash
pip install -r requirements.txt
Use o código com cuidado.

4. Rodar as Migrações (Banco de Dados)
bash
python manage.py makemigrations
python manage.py migrate
Use o código com cuidado.

5. Iniciar o Servidor
bash
python manage.py run.py
Use o código com cuidado.

A API estará disponível em: http://127.0.0.1

## 📡 Endpoints Principais (Exemplos)
Método	Endpoint	Descrição
GET	/api/livros/	Listar todos os livros
POST	/api/livros/	Cadastrar um novo livro
GET	/api/livros/{id}/	Detalhes de um livro específico
PUT	/api/livros/{id}/	Atualizar dados de um livro
DELETE	/api/livros/{id}/	Remover um livro do acervo

## 📝 Variáveis de Ambiente
Crie um arquivo .env na raiz do projeto e configure as chaves necessárias (Exemplo):
env
DEBUG=True
SECRET_KEY=sua_chave_secreta_aqui
Use o código com cuidado.

## ⌨️ desenvolvido por mvdevelop
