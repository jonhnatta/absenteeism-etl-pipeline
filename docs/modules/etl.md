# Módulo ETL

O módulo `src/etl/etl_absenteeism.py` contém a classe principal responsável por todo o processamento ETL dos dados de absenteísmo.

## Arquitetura

### Classe EtlAbsenteeism

A classe `EtlAbsenteeism` implementa o padrão ETL seguindo os princípios de responsabilidade única e encapsulamento.

```python
class EtlAbsenteeism:
    """Classe para fazer ETL de arquivos em uma pasta específica."""
```

## Métodos Principais

### 1. Extract (Extração)

```python
def extract_data(self, file_type: str) -> List[pd.DataFrame]
```

**Responsabilidade**: Ler todos os arquivos Excel de uma pasta e converter em DataFrames.

**Funcionalidades**:
- Busca arquivos por padrão (ex: `*.xlsx`)
- Carrega cada arquivo como DataFrame usando `pandas.read_excel()`
- Retorna lista de DataFrames para processamento

**Exemplo**:
```python
etl = EtlAbsenteeism("data/raw")
dataframes = etl.extract_data("*.xlsx")
```

### 2. Transform (Transformação)

```python
def tranform_data(self, data_frame_list: List[pd.DataFrame]) -> pd.DataFrame
```

**Responsabilidade**: Combinar múltiplos DataFrames em um único dataset.

**Funcionalidades**:
- Concatena DataFrames verticalmente usando `pandas.concat()`
- Preserva todas as linhas e colunas
- Retorna DataFrame unificado

**Exemplo**:
```python
combined_df = etl.tranform_data(dataframes)
```

### 3. Load (Carregamento)

```python
def load_data(self, data_frame: pd.DataFrame, output_path: str, file_name: str) -> bool
```

**Responsabilidade**: Salvar o DataFrame processado em arquivo Excel.

**Funcionalidades**:
- Cria pasta de destino se não existir
- Salva DataFrame como arquivo Excel
- Retorna `True` para sucesso, `False` para erro
- Implementa tratamento de exceções

**Exemplo**:
```python
success = etl.load_data(df, "data/processed", "resultado_20240920")
```

## Dependências

- **pandas**: Manipulação e análise de dados
- **openpyxl**: Leitura e escrita de arquivos Excel
- **glob**: Busca de arquivos por padrão
- **os**: Operações do sistema operacional

## Fluxo de Dados

```mermaid
graph LR
    A[Arquivos Excel] --> B[extract_data]
    B --> C[Lista de DataFrames]
    C --> D[tranform_data]
    D --> E[DataFrame Único]
    E --> F[load_data]
    F --> G[Arquivo Excel Final]
```

## Vantagens da Arquitetura

1. **Modularidade**: Cada método tem responsabilidade específica
2. **Reutilização**: Métodos podem ser usados independentemente
3. **Testabilidade**: Cada método pode ser testado isoladamente
4. **Manutenibilidade**: Mudanças são localizadas e controladas
5. **Flexibilidade**: Fácil extensão para novos tipos de transformação

## Casos de Uso

- **Consolidação de dados mensais**: Juntar planilhas de diferentes meses
- **Agregação departamental**: Combinar dados de vários departamentos
- **Migração de dados**: Converter múltiplos arquivos em formato único
- **Análise histórica**: Unificar dados de diferentes períodos

## Validações Implementadas

- Verificação de existência da pasta de destino
- Tratamento de exceções no salvamento
- Retorno booleano para validação de sucesso
- Logs informativos sobre o processamento
