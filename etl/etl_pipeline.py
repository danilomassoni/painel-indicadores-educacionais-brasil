# Script principal que executa o ETL completo
import os
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_to_postgres

def run_etl():
    """
    Orquestração do pipeline ETL: Extração, transformação e Carga. 
    """

    # Configuração
    raw_data_path = "data/raw/merged_df.csv"
    processed_data_path = "data/processed/transformed_data.csv"
    indicadores = "indicadores_educacionais"
    db_url = os.getenv("DATABASE_URL", "postgresql://user:password@localhost:5432/meubanco")

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
    