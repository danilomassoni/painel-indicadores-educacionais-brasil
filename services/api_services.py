# Definição da API com FastAPI

from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
import pandas as pd
import os

# Configuração da API
app = FastAPI(title="API de Indicadores Educacionais")

# Conexão com o banco de dados
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:1234@localhost:5432/painel_indicadores_educacionais")
engine = create_engine(DATABASE_URL)

# Endpoint raiz
@app.get("/")
def read_root():
    return {"message": "API de Indicadores Educacionais"}


# Endpoint para consultar todos os indicadores
@app.get("/indicadores/")
def get_indicadores():
    try:
        query = "SELECT * FROM indicadores"
        df = pd.read_sql(query, engine)
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# Endpoint para consultar um indicador específico
@app.get("/indicadores/{indicador_id}")
def get_indicador(indicador_id: int):
    try:
        query = f"SELECT * FROM indicadores WHERE id = {indicador_id}"
        df = pd.read_sql(query, engine)
        if df.shape[0] == 0:
            raise HTTPException(status_code=404, detail="Indicador não encontrado")
        return df.to_dict(orient="records")[0]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# Endpoint para consultar indicadores por estado
@app.get("/indicadores/estado/{estado}")
def get_indicadores_estado(estado: str):
    try:
        query = f"SELECT * FROM indicadores WHERE unidade_geográfica = '{estado}'"
        df = pd.read_sql(query, engine)
        if df.shape[0] == 0:
            raise HTTPException(status_code=404, detail="Indicadores não encontrados")
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))