# Script principal que executa o ETL completo
import sys
import os
import pandas as pd

# Adiciona o diretório do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from extract import extract_data
from transform import transform_data
from load import load_to_postgres

def run_etl():
    """
    Orquestração do pipeline ETL: Extração, transformação e Carga. 
    """

    # Configuração
    raw_data_path = "data/raw/merged_df.csv"
    processed_data_path = "data/processed/transformed_data.csv"
    indicadores = "indicadores_educacionais"
    db_url = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:1234@localhost:5432/painel_indicadores_educacionais")

    # Extração
    print ("Extraindo os dados........")
    df = extract_data(raw_data_path)

    # Transformação
    print("Transformando os dados.........")
    df = transform_data(df)
    df.to_csv(processed_data_path, index=False)

    # Carga
    print("Carregando os dados no banco............")
    load_to_postgres(df, indicadores, db_url)

    print("PIPELINE ETL CONCLUÍDO COM SUCESSO!")

if __name__ == "__main__":
    run_etl()
    