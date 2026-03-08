
# Tema 4 – Python com Banco de Dados

## 📌 Descrição

Este diretório contém exemplos práticos de **integração entre Python e diferentes sistemas de banco de dados**.
O objetivo é demonstrar como aplicações Python podem se conectar, consultar, inserir, atualizar e remover dados utilizando conectores específicos para cada tecnologia.

Este material faz parte dos estudos da graduação e tem foco em **desenvolvimento back-end e manipulação de dados**.

---

## 🎯 Objetivos de Aprendizado

* Compreender como Python se conecta a diferentes bancos de dados
* Executar operações CRUD (Create, Read, Update, Delete)
* Utilizar bibliotecas específicas de conexão
* Aplicar boas práticas de organização de código

---

## 🧰 Tecnologias Utilizadas

* Python 3
* SQLite
* MySQL
* PostgreSQL
* MongoDB

---

## 📦 Bibliotecas Utilizadas

| Banco de Dados | Biblioteca Python      |
| -------------- | ---------------------- |
| SQLite         | sqlite3                |
| MySQL          | mysql-connector-python |
| PostgreSQL     | psycopg2               |
| MongoDB        | pymongo                |

---

## 📂 Estrutura do Diretório

```
tema4-python-banco-dados/
│
├── sqlite/
│   └── sqlite_connection.py
│
├── mysql/
│   └── mysql_connection.py
│
├── postgresql/
│   └── postgres_connection.py
│
├── mongodb/
│   └── mongodb_connection.py
│
└── README.md
```

---

## ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd tema4-python-banco-dados
```

Instale as dependências necessárias:

```bash
pip install mysql-connector-python psycopg2 pymongo
```

> O SQLite já vem incluído na biblioteca padrão do Python.

---

## 🔌 Exemplos de Conexão

### SQLite

```python
import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("SELECT sqlite_version();")
print(cursor.fetchone())

conn.close()
```

---

### MySQL

```python
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="senha",
    database="meubanco"
)

cursor = conn.cursor()
cursor.execute("SELECT DATABASE();")

print(cursor.fetchone())

conn.close()
```

---

### PostgreSQL

```python
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="meubanco",
    user="postgres",
    password="senha"
)

cursor = conn.cursor()
cursor.execute("SELECT version();")

print(cursor.fetchone())

conn.close()
```

---

### MongoDB

```python
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["meubanco"]

print(db.list_collection_names())
```

---

## 📚 Conceitos Abordados

* Conexão com banco de dados
* Execução de consultas
* Manipulação de dados
* Integração entre aplicações Python e bancos de dados
* Diferença entre bancos **relacionais** e **não relacionais**

---

## 👨‍💻 Autor

Projeto desenvolvido como parte dos estudos em **Desenvolvimento de Software / Engenharia de Software**, com foco em **Back-end e manipulação de dados com Python**.

---

## 📄 Licença

Este projeto é apenas para fins **educacionais**.
