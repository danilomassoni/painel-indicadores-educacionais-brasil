# Código para carregar os dados no banco de dados
import pandas as pd
from sqlalchemy import create_engine
import os

def load_to_postgres(df: pd.DataFrame, indicadores: str, db_url: str):
    """
    Carrega os dados transformados para um banco de dados PostgreSQL

    :param df: DataFram contendo os dados processados
    :param indicadores: Tabela onde os dados irão ser inseridos
    :param db_url: URL de conexão com o PostgreSQL
    """
    engine = create_engine(db_url)

    with engine.connect() as connection:
        df.to_sql(indicadores, con=connection, if_exists='replace', index=False)

        print(f"Dados carregados com sucesso na tablea '{indicadores}'!")

# Teste de Carga 
if __name__ == "__main__":
    DATABASE_URL =os.getenv("DATABASE_URL", "postgresql://postgres:1234d@localhost:5432/educacao")
    df = pd.read_csv("./data/processed/trasnformed_data.csv")
    load_to_postgres(df, "indicadores_educacionais", DATABASE_URL)