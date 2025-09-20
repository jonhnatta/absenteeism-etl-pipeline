# Projeto ETL - Dados de Absenteísmo

Bem-vindo à documentação do projeto ETL para processamento de dados de absenteísmo.

## Visão Geral

Este projeto implementa um pipeline ETL (Extract, Transform, Load) para processar dados de absenteísmo de funcionários armazenados em arquivos Excel.

## Funcionalidades

- **Extração**: Lê múltiplos arquivos Excel da pasta `data/raw/`
- **Transformação**: Combina todos os DataFrames em um único dataset
- **Carregamento**: Salva o resultado em arquivo Excel na pasta `data/processed/`
- **Testes**: Suite de testes automatizados com pytest
- **Qualidade**: Verificação de código com blue, isort e pydocstyle

## Estrutura do Projeto

```
estrutura-de-projeto/
├── data/
│   ├── raw/          # Dados brutos (arquivos Excel)
│   └── processed/    # Dados processados
├── src/
│   └── etl/
│       ├── __init__.py
│       └── etl_absenteeism.py  # Classe principal ETL
├── tests/
│   └── test_etl.py   # Testes automatizados
├── docs/             # Documentação
├── main.py           # Ponto de entrada
└── pyproject.toml    # Configurações do projeto
```

## Como Usar

### Instalação

```bash
uv sync
```

### Executar ETL

```bash
uv run task run
```

### Rodar Testes

```bash
uv run pytest
```

### Verificar Qualidade do Código

```bash
uv run task format
```

### Servir Documentação

```bash
uv run task docs-serve
```

## Dados

O projeto processa dados de absenteísmo com as seguintes colunas:

- **Colaborador_id**: ID único do funcionário
- **Colaborador_nome**: Nome do funcionário
- **Departamento**: Departamento do funcionário
- **Motivo_da_ausência**: Razão da ausência
- **Horas_de_ausência**: Quantidade de horas ausentes
- **Data_da_ausência**: Data da ausência
- **Salário**: Salário do funcionário

## Configuração

O projeto usa:

- **Python 3.11+**
- **pandas** para manipulação de dados
- **openpyxl** para leitura de arquivos Excel
- **pytest** para testes
- **blue** para formatação de código
- **isort** para organização de imports
- **pydocstyle** para verificação de docstrings
- **mkdocs** para documentação
