# Projeto ETL - Dados de Absenteísmo

Pipeline ETL para processamento de dados de absenteísmo de funcionários a partir de arquivos Excel.

## Visão Geral

Este projeto implementa um pipeline ETL (Extract, Transform, Load) completo para consolidar dados de absenteísmo armazenados em múltiplos arquivos Excel. O sistema automatiza a extração, transformação e carregamento dos dados, gerando um arquivo único para análise.

## Funcionalidades

- **Extração**: Lê múltiplos arquivos Excel da pasta `data/raw/`
- **Transformação**: Combina todos os DataFrames em um único dataset
- **Carregamento**: Salva o resultado em arquivo Excel na pasta `data/processed/`
- **Validação**: Verificação de sucesso em cada etapa do processo
- **Timestamp**: Adiciona timestamp automático aos arquivos gerados
- **Testes**: Suite de testes automatizados com pytest
- **Qualidade**: Verificação de código com blue, isort e pydocstyle
- **Documentação**: Documentação automática com MkDocs

## Estrutura do Projeto

```
estrutura-de-projeto/
├── data/
│   ├── raw/          # Dados brutos (arquivos Excel)
│   ├── input/        # Pasta para dados de entrada
│   ├── output/       # Pasta para dados de saída
│   └── processed/    # Dados processados pelo ETL
├── src/
│   └── etl/
│       ├── __init__.py
│       └── etl_absenteeism.py  # Classe principal ETL
├── tests/
│   └── test_etl.py   # Testes automatizados
├── docs/             # Documentação MkDocs
│   ├── index.md
│   ├── modules/
│   ├── api/
│   └── tests.md
├── main.py           # Ponto de entrada do pipeline
├── pyproject.toml    # Configurações e dependências
├── mkdocs.yml        # Configuração da documentação
└── README.md         # Este arquivo
```

## Pré-requisitos

- **Python 3.11+**
- **uv** (gerenciador de dependências)

## Instalação

1. **Clone o repositório:**
```bash
git clone <url-do-repositorio>
cd estrutura-de-projeto
```

2. **Instale as dependências:**
```bash
uv sync
```

## Como Usar

### Executar Pipeline ETL

```bash
uv run task run
```

### Rodar Testes

```bash
# Todos os testes
uv run pytest

# Testes com verbosidade
uv run pytest -v

# Testes específicos
uv run pytest tests/test_etl.py
```

### Verificar Qualidade do Código

```bash
# Formatação, organização de imports e verificação de docstrings
uv run task format

# Executar apenas formatação
uv run blue .

# Executar apenas organização de imports
uv run isort .

# Executar apenas verificação de docstrings
uv run pydocstyle .
```

### Documentação

```bash
# Servir documentação localmente (http://localhost:8000)
uv run task docs-serve

# Gerar documentação estática
uv run task docs-build
```

## Estrutura dos Dados

O pipeline processa arquivos Excel com as seguintes colunas esperadas:

- **Colaborador_id**: ID único do funcionário
- **Colaborador_nome**: Nome do funcionário
- **Departamento**: Departamento do funcionário
- **Motivo_da_ausência**: Razão da ausência
- **Horas_de_ausência**: Quantidade de horas ausentes
- **Data_da_ausência**: Data da ausência
- **Salário**: Salário do funcionário

## Fluxo do Pipeline

1. **Extração**: Localiza e carrega todos os arquivos `.xlsx` da pasta `data/raw/`
2. **Validação**: Verifica se arquivos foram encontrados
3. **Transformação**: Combina todos os DataFrames em um único dataset
4. **Carregamento**: Salva resultado com timestamp na pasta `data/processed/`
5. **Confirmação**: Exibe mensagens de sucesso ou erro

## Exemplo de Saída

```bash
=== Iniciando ETL ===
3 arquivos carregados...
Juntando os dataframes...
Dataframe combinado com sucesso!
Salvando na pasta processed
Arquivo absenteeism_data_20240920_143052.xlsx salvo com sucesso!
```

## Tecnologias Utilizadas

- **Python 3.11+**: Linguagem principal
- **pandas**: Manipulação e análise de dados
- **openpyxl**: Leitura e escrita de arquivos Excel
- **pytest**: Framework de testes
- **blue**: Formatação de código (fork do black)
- **isort**: Organização de imports
- **pydocstyle**: Verificação de docstrings
- **mkdocs**: Geração de documentação
- **mkdocs-material**: Tema da documentação
- **mkdocstrings**: Extração automática de docstrings
- **taskipy**: Automação de tarefas
- **uv**: Gerenciador de dependências e ambientes

## Comandos Taskipy

O projeto utiliza `taskipy` para automação de tarefas:

```bash
uv run task format      # Formatação completa do código
uv run task test        # Execução dos testes
uv run task run         # Execução do pipeline ETL
uv run task docs-serve  # Servir documentação
uv run task docs-build  # Gerar documentação
```

## Estrutura de Classes

### EtlAbsenteeism

Classe principal que implementa o padrão ETL:

- `extract_data(file_type)`: Extrai dados dos arquivos Excel
- `tranform_data(dataframe_list)`: Combina múltiplos DataFrames
- `load_data(dataframe, output_path, file_name)`: Salva dados processados

## Testes

O projeto inclui testes abrangentes:

- **Testes unitários**: Validam métodos individuais
- **Testes de integração**: Verificam o pipeline completo
- **Validação de dados**: Garantem integridade dos dados processados

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Padrões de Código

- **Formatação**: blue (configurado para linha de 88 caracteres)
- **Imports**: isort (estilo black)
- **Docstrings**: Google Style (verificado com pydocstyle)
- **Testes**: pytest com cobertura mínima recomendada

## Licença

Este projeto está sob licença MIT. Veja o arquivo LICENSE para mais detalhes.

## Autor

Desenvolvido como parte do projeto de estruturação ETL.

## Suporte

Para dúvidas ou problemas:

1. Verifique a [documentação completa](docs/)
2. Execute os testes para validar o ambiente
3. Consulte os logs de execução para debugging
