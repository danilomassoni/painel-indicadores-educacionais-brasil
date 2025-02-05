# Código de extração dos dados (ler CSV)
import pandas as pd
import os

def extract_data(filepath: str) -> pd.DataFrame: 
    """
    Lê um arquivo em CSV e retorna um DataFrame Pandas.
    
    :param filepath: Caminho para o CSV.
    :return: DataFrame com os dados lidos.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Arquivo não encontrado: {filepath}")
    
    df = pd.read_csv(filepath)
    print(f"Dados extraídos com sucesso! {df.shape[0]} linhas e {df.shape[1]} colunas.")
    return df

# Caso precise testar a extração 
if __name__ == "__main__":
    df = extract_data("./data/raw/merged_df.csv")
    print(df.head(10))