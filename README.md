# Sistema de Gestão Escolar

Projeto desenvolvido utilizando **Django**, **Django REST Framework**, **SQL bruto** e **Docker**.

A aplicação possui:

- Frontend em Django (HTML + CSS)
- API REST (DRF)
- Consulta SQL bruta com JOIN e GROUP BY
- Validações via `clean()`
- Camada de serviços (Service Layer)
- CRUD de alunos, cursos e matrículas
- Relatórios via endpoint JSON
- Execução padronizada via Docker

---

##  Tecnologias utilizadas

- Python 3.11  
- Django  
- Django REST Framework  
- SQLite  
- Docker  
- Docker Compose  

---
### Pré-requisitos para rodar o projeto
- [Docker](https://www.docker.com/products/docker-desktop/) instalado
- [Git](https://git-scm.com/) (para clonar o repositório)
##  Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/fwrnandaaa/Projeto---Sistema-de-Gestao-Escolar.git
```
### 2. Pelo terminal, acesse o projeto
```bash
cd gestao_escolar
```

### 3. Construa e inicie os containers
```bash
docker-compose up --build
```

##  Acessando o projeto
### 1. Para acessar o FrontEnd(HTML)

```bash
http://localhost:8000
```
### 2. Endpoints principais de Relatórios:
```bash
http://localhost:8000/api/alunos/
http://localhost:8000/api/cursos/
http://localhost:8000/api/matriculas/
http://localhost:8000/api/relatorios/matriculas-por-curso/
```