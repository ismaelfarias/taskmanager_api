# Task Manager API - MVP

Projeto MVP de API desenvolvido durante a primeira Sprint do curso de Pós-Graduação em Desenvolvimento Full Stack da PUC-Rio Digital, tendo como objetivo exercitar a criação de APIs utilizando a liguagem Python e Flask.

## Dependencias
- Python 3
- Flask 3.0.x
- Flask-SQLAlchemy 3.1.1
- Flask-Cors 5.0.0
- flask_openapi3 3.1.3
- SQLAlchemy 2.0.x
- SQLAlchemy-Utils 0.41.2
- typing-extensions 4.12.2
- pydantic 2.9.1

## Como executar

Será necessário ter todas as dependências listadas no requirements.txt instaladas. Em seguida clonar o repositório, abrir o terminal e entrar no diretório raiz da aplicação flaskr, para executar os comandos descritos abaixo.

É recomendado o uso de ambientes virtuais do tipo virtualenv.

```
(env)$ pip install -r requirements.txt
```
Este comando instala as dependências descritas no arquivo requirements.txt.

Para iniciar a API, estando dentro do diretório **flaskr**, basta executar o comando:
```
(env)$ flask run --host 0.0.0.0 --port 5000
```

Para verificar o status da API em execução, abra o navegador em http://localhost:5000, que exibirá a tela inicial para seleção/visualização da documentação em formato OpenAPI 3.x.

## TODO
- Configurar logs
- Tratamento de erros e responses