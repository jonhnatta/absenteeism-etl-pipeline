"""Módulo principal para execução do pipeline ETL de dados."""

from datetime import datetime

from src.etl.etl_absenteeism import EtlAbsenteeism


def main():
    """Executa o pipeline ETL completo para processamento dos dados."""
    print('=== Iniciando  ETL ===')

    file_type = 'xlsx'
    output_path = 'data/processed'
    input_path = 'data/raw'

    try:
        etl = EtlAbsenteeism(input_path)
        dataframes = etl.extract_data(f'*.{file_type}')

        if not dataframes:
            print('Nenhum arquivo processados!')
            return

        print(f'{len(dataframes)} arquivos carregados...')

        print('Juntando os dataframes...')

        transform = etl.tranform_data(dataframes)

        if transform is not None and not transform.empty:
            print('Dataframe combinado com sucesso!')
        else:
            print('Erro ao juntar os dataframes')

        print('Salvando na pasta processed')

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename_with_timestamp = f'absenteeism_data_{timestamp}'

        load = etl.load_data(transform, output_path, filename_with_timestamp)

        if load:
            print(
                f'Arquivo {filename_with_timestamp}.{file_type} salvo com sucesso!'
            )
        else:
            print('Falha ao salvar arquivo')

    except Exception as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    main()
