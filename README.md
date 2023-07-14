<h1 align="center">FastAPI 101</h1>

<p align="center">Sistema WebApp simples para cadastro de usuários com FastAPI.</p>

<p align="center">
    <a target="_blank" href="https://github.com/pyenv/pyenv">PyENV</a> | 
    <a target="_blank" href="https://python-poetry.org/docs">Poetry</a> | 
    <a target="_blank" href="https://fastapi.tiangolo.com">FastAPI</a> | 
    <a target="_blank" href="https://sqlmodel.tiangolo.com">SQLModel</a> | 
    <a target="_blank" href="https://css-tricks.com/snippets/css/a-guide-to-flexbox">CSS Flex</a> | 
    <a target="_blank" href="https://css-tricks.com/snippets/css/a-guide-to-grid">CSS Grid</a>
</p>


### Configurando Ambiente

Definir versão do Python com PyENV

```bash
> pyenv install --list
> pyenv install 3.11.4
> pyenv global 3.11.4
> pyenv shell 3.11.4
```

Clonar projeto

```bash
> git clone https://github.com/dalmofelipe/FastApi101.git
```

Iniciar shell poetry

```bash
> cd FastApi101
> poetry shell
```

Instalar dependências do `pyproject.toml`

```bash
> poetry install
```

### Executando o Projeto

```bash
> fast runserver
```

O servidor ouvirá a porta 8000 em http://localhost:8000

A porta pode ser modificada informando a option `--port=3333`.

```bash
> fast runserver --port=3333
```

Acesse a ajuda com os comandos:

```bash
> fast --help
> fast runserver --help
```