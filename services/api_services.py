# Definição da API com FastAPI

from fastapi import FastAPI, HTTPException, Query
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
def get_indicadores(page: int = Query(1, ge=1), page_size: int = Query(10, ge=1, le=100)):
    try:
        #Cosonta todos os dados
        query = "SELECT * FROM indicadores_educacionais"
        df = pd.read_sql(query, engine)

        # Cálculo de início e fim para a página solicitada
        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        # Verificar se a página é válida
        if start_index >= len(df):
            raise HTTPException(status_code=404, detail="Página não encontrada")

        # Retornar apenas os registros da página atual
        paginated_data = df.iloc[start_index:end_index]
        return {
            "page": page,
            "page_size": page_size,
            "total_records": len(df),
            "total_pages": (len(df) // page_size) + (1 if len(df) % page_size > 0 else 0),
            "data": paginated_data.to_dict(orient="records")
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))









# Endpoint para consultar um indicador específico por ID
@app.get("/indicadores/{indicador_id}")
def get_indicador(indicador_id: int):
    try:
        query = f"SELECT * FROM indicadores_educacionais WHERE id = '{indicador_id}'"
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
        query = f"SELECT * FROM indicadores_educacionais WHERE unidade_geográfica = '{estado}'"
        df = pd.read_sql(query, engine)
        if df.shape[0] == 0:
            raise HTTPException(status_code=404, detail="Indicadores não encontrados")
        return df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

# PARA SUBIR A API, EXECUTE O SEGUINTE COMANDO NO TERMINAL: uvicorn services.api_services:app --host 0.0.0.0 --port 8000 --reload --log-level debug

# Acesse no navegador: http://localhost:8000/indicadores/