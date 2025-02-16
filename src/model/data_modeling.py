# Criação de tabelas fato/dimensão
import pandas as pd
from database.connection import get_connection

def creat_fact_dim_tables():
    """
    Cria tabelas fato e dimensão para modelagem de dados no Power BI.
    """

    conn = get_connection()

    
