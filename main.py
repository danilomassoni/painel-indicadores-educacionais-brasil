# Módulo principal do projeto
import os
import threading
import uvicorn
from services.api_services import app
from etl.etl_pipeline import run_etl
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Servir os arquivos estáticos da pasta static
app.mount("/", StaticFiles(directory="static", html=True), name="static")

def execute_etl():
    """
    Endpoint para executar o pipeline ETL manualmente."""

    run_etl()
    return {"message": "Pipeline ETL executada com suecesso!"}


def start_api():
    """ 
    Inicia a API em uma thread separada.
    """
    uvicorn.run(app, host="0.0.0.0", port=8000)

    print("API iniciada em http://localhost:8000")



if __name__ == "__main__":
    # Criando uma thread para rodar a API sem bloquear o script
    api_thread = threading.Thread(target=start_api, daemon=True)
    api_thread.start()

    print("API iniciada em http://localhost:8000")

    # Mantém o script rodando
    api_thread.join()    
    


# Subir aplicação index: uvicorn main:app --host 0.0.0.0 --port 8000 --reload