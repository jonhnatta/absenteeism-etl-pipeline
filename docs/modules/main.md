# Módulo Main

O módulo `main.py` é o ponto de entrada principal do pipeline ETL. Ele orquestra todo o processo de extração, transformação e carregamento dos dados.

## Responsabilidades

- **Configuração**: Define os caminhos de entrada e saída dos dados
- **Orquestração**: Coordena a execução das etapas ETL
- **Validação**: Verifica se cada etapa foi executada com sucesso
- **Logging**: Fornece feedback sobre o progresso do processamento

## Fluxo de Execução

1. **Inicialização**: Cria instância da classe `EtlAbsenteeism`
2. **Extração**: Carrega arquivos Excel da pasta `data/raw/`
3. **Validação**: Verifica se arquivos foram encontrados
4. **Transformação**: Combina DataFrames em um único dataset
5. **Carregamento**: Salva resultado com timestamp na pasta `data/processed/`
6. **Confirmação**: Exibe mensagens de sucesso ou erro

## Configuração

```python
file_type = 'xlsx'          # Tipo de arquivo a processar
output_path = 'data/processed'  # Pasta de saída
input_path = 'data/raw'     # Pasta de entrada
```

## Exemplo de Uso

```bash
# Executar o pipeline ETL
uv run python main.py

# Saída esperada:
# === Iniciando ETL ===
# 3 arquivos carregados...
# Juntando os dataframes...
# Dataframe combinado com sucesso!
# Salvando na pasta processed
# Arquivo absenteeism_data_20240920_143052.xlsx salvo com sucesso!
```

## Tratamento de Erros

O módulo implementa tratamento básico de erros:

- **Arquivos não encontrados**: Informa quando nenhum arquivo é processado
- **Erro na transformação**: Verifica se o DataFrame foi combinado corretamente
- **Erro no salvamento**: Valida se o arquivo foi salvo com sucesso
- **Exceções gerais**: Captura e exibe erros inesperados

## Outputs

O arquivo gerado segue o padrão:
```
absenteeism_data_YYYYMMDD_HHMMSS.xlsx
```

Onde:
- `YYYY`: Ano (4 dígitos)
- `MM`: Mês (2 dígitos)
- `DD`: Dia (2 dígitos)
- `HH`: Hora (2 dígitos)
- `MM`: Minuto (2 dígitos)
- `SS`: Segundo (2 dígitos)
