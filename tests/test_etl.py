import os
import sys

import pandas as pd

# Adicionar o diretório raiz ao path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(current_dir)
sys.path.insert(0, project_dir)

from src.etl.etl_absenteeism import EtlAbsenteeism

etl = EtlAbsenteeism('data/raw')


def test_extract_data():
    """Testa se consegue extrair todos os dados"""
    dataframes = etl.extract_data('*.xlsx')

    # Verificar se retornou uma lista
    assert isinstance(dataframes, list)
    # Verificar se encontrou arquivos (assumindo que tem arquivos na pasta)
    assert len(dataframes) > 0
    # Verificar se cada item é um DataFrame
    for df in dataframes:
        assert isinstance(df, pd.DataFrame)


def test_transform_data_join():
    """Testa se junta os DataFrames corretamente"""
    df1 = pd.DataFrame(
        {'ID': [1, 2], 'Nome': ['João', 'Maria'], 'Salario': [5000, 6000]}
    )

    df2 = pd.DataFrame(
        {'ID': [3, 4], 'Nome': ['Pedro', 'Ana'], 'Salario': [7000, 8000]}
    )

    join = etl.tranform_data([df1, df2])

    assert isinstance(join, pd.DataFrame)
    assert len(join) == 4
    assert len(join.columns) == 3
    assert join['ID'].tolist() == [1, 2, 3, 4]
