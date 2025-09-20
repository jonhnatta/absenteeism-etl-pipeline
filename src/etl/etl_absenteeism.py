"""Módulo para processamento ETL de dados."""

import glob
import os
from typing import List

import pandas as pd


class EtlAbsenteeism:
    """Classe para fazer ETL de arquivos em uma pasta específica."""

    def __init__(self, data_path: str):
        """Inicializa o processador ETL.

        Args:
            data_path: Caminho da pasta.
        """
        self.data_path = data_path

    def extract_data(self, file_type: str) -> List[pd.DataFrame]:
        """Método para ler os arquivos e retornar uma lista de dataframes.

        Args:
            file_type (str): tipo de arquivo.

        Returns:
            Lista de dataframes.
        """
        files = glob.glob(os.path.join(self.data_path, file_type))

        df_list = []

        for file in files:
            df_list.append(pd.read_excel(file))

        return df_list

    def tranform_data(
        self, data_frame_list: List[pd.DataFrame]
    ) -> pd.DataFrame:
        """Método para juntar os dataframes.

        Args:
            data_frame_list: Lista de DataFrames para combinar.

        Returns:
            DataFrame unido.
        """
        return pd.concat(data_frame_list)

    def load_data(
        self, data_frame: pd.DataFrame, output_path: str, file_name: str
    ) -> bool:
        """Recebe o dataframe e cria o arquivo xlsx final.

        Args:
            data_frame (pd.DataFrame): dataframe a ser salvo.
            output_path: pasta de destino.
            file_name: nome do arquivo salvo.

        Returns:
            True se sucesso, False se erro.
        """
        try:

            if not os.path.exists(output_path):
                os.makedirs(output_path)

            data_frame.to_excel(f'{output_path}/{file_name}.xlsx', index=False)
            return True
        except Exception:
            return False
