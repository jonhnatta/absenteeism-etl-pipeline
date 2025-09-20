# Testes

Este projeto utiliza **pytest** para garantir a qualidade e confiabilidade do código. Os testes cobrem as principais funcionalidades do pipeline ETL.

## Estratégia de Testes

### Tipos de Teste

1. **Testes Unitários**: Testam métodos individuais da classe `EtlAbsenteeism`
2. **Testes de Integração**: Verificam o funcionamento completo do pipeline
3. **Testes de Validação**: Garantem que os dados são processados corretamente

## Testes Implementados

### `test_extract_data()`

**Objetivo**: Verificar se a extração de dados funciona corretamente.

**Validações**:
- Retorna uma lista de DataFrames
- Encontra arquivos na pasta especificada
- Cada item da lista é um DataFrame válido

```python
def test_extract_data():
    """Testa se consegue extrair todos os dados"""
    etl = EtlData("data/raw")
    dataframes = etl.extract_data("*.xlsx")

    assert isinstance(dataframes, list)
    assert len(dataframes) > 0
    for df in dataframes:
        assert isinstance(df, pd.DataFrame)
```

### `test_transform_data_join()`

**Objetivo**: Testar a combinação de múltiplos DataFrames.

**Validações**:
- Combina DataFrames corretamente
- Preserva todas as linhas e colunas
- Mantém a ordem dos dados

```python
def test_transform_data_join():
    """Testa se junta os DataFrames corretamente"""
    # Cria DataFrames de teste
    df1 = pd.DataFrame({...})
    df2 = pd.DataFrame({...})

    # Testa a junção
    result = etl.tranform_data([df1, df2])

    assert isinstance(result, pd.DataFrame)
    assert len(result) == 4  # 2 + 2 = 4 linhas
```

### `test_transform_single_dataframe()`

**Objetivo**: Verificar comportamento com apenas um DataFrame.

**Validações**:
- Processa corretamente um único DataFrame
- Mantém estrutura original
- Não introduz erros desnecessários

### `test_integration_full_pipeline()`

**Objetivo**: Testar o pipeline completo end-to-end.

**Validações**:
- Extração → Transformação funciona
- Dados são processados corretamente
- Pipeline completo é executado sem erros

## Executando os Testes

### Todos os Testes
```bash
uv run pytest
```

### Testes com Verbosidade
```bash
uv run pytest -v
```

### Testes Específicos
```bash
uv run pytest tests/test_etl.py::test_extract_data
```

### Com Coverage
```bash
uv run pytest --cov=src
```

## Estrutura dos Dados de Teste

Os testes utilizam DataFrames simulados com a estrutura:

```python
df_test = pd.DataFrame({
    "ID": [1, 2],
    "Nome": ["João", "Maria"],
    "Salario": [5000, 6000]
})
```

## Validações de Qualidade

### Assertions Principais

- **Tipo de retorno**: `isinstance(result, expected_type)`
- **Tamanho dos dados**: `len(dataframes) > 0`
- **Estrutura**: `len(result.columns) == expected_columns`
- **Conteúdo**: `result["column"].tolist() == expected_values`

### Cenários Testados

1. **Cenário Normal**: Múltiplos arquivos válidos
2. **Cenário Unitário**: Apenas um arquivo
3. **Cenário Vazio**: Nenhum arquivo encontrado (implícito)
4. **Cenário de Integração**: Pipeline completo

## Benefícios dos Testes

- **Confiabilidade**: Garante que o código funciona como esperado
- **Manutenibilidade**: Detecta quebras durante mudanças
- **Documentação**: Serve como documentação viva do comportamento
- **Refatoração Segura**: Permite mudanças com confiança

## Métricas de Cobertura

Os testes cobrem:
- ✅ Método `extract_data()`
- ✅ Método `tranform_data()`
- ✅ Pipeline de integração
- ⚠️ Método `load_data()` (pode ser adicionado)

## Configuração de Teste

O arquivo `test_etl.py` inclui configuração para:
- Resolução de paths de módulos
- Imports corretos do código fonte
- Execução independente com `if __name__ == "__main__"`

## Exemplo de Execução

```bash
$ uv run pytest tests/test_etl.py -v

=== test session starts ===
tests/test_etl.py::test_extract_data PASSED
tests/test_etl.py::test_transform_data_join PASSED
tests/test_etl.py::test_transform_single_dataframe PASSED
tests/test_etl.py::test_integration_full_pipeline PASSED

=== 4 passed in 0.15s ===
```
