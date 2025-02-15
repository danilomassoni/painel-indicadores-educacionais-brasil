# Código de limpeza, tratamento e normalização dos dados
import pandas as pd

def clean_column_names(df : pd.DataFrame) -> pd.DataFrame:
    """
    Renomeia colunas para um formato padrão (minúsculo e undercores) 
    """
    df.columns = (
        df.columns.str.lower()
        .str.replace(" ", "_")
        .str.replace("[()%-]", "", regex=True)
    )
    return df

def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Trata valores nulos, preenchendo com a média ou 0
    Esta função precisa de mais atenção
    """
    df["remuneração_média"] = df["remuneração_média"].fillna(df["remuneração_média"].mean())
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numeric_cols] = df[numeric_cols].fillna(0)
    return df

def convert_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converta colunas numéricas para o tipo correto
    """
    numeric_cols = [col for col in df.columns if df[col].dtype == 'object' and df[col].str.replace('.', '', 1).str.isnumeric().all()]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def add_country(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adiciona coluna com o nome do país
    """
    df["country"] = "Brasil"
    return df

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Aplica todas as transformações necessárias
    """
    df = clean_column_names(df)
    df = handle_missing_values(df)
    df = convert_data_types(df)
    df = add_country(df)

    df.to_csv("./data/processed/transformed_df.csv", index=False) # Cria um arquivo CSV com os dados transformados
    print("Dados transformados e salvo com sucesso!")

    return df

# Opcional para testar
if __name__ == "__main__":
    df = pd.read_csv("./data/raw/merged_df.csv")
    df = transform_data(df)
    print(df.head())
    print("Colunas disponíveis:", df.columns.tolist())

