# Módulo principal do projeto

from etl.etl_pipeline import run_etl
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Servir os arquivos estáticos da pasta static
app.mount("/", StaticFiles(directory="static", html=True), name="static")

def main():
    """
    Ponto de entrada do projeto de Engenharia de Dados.
    """
    print("Iniciando o Projeto de Engenharia de Dados.....")
    run_etl()
    print("Pipeline ETL executado com sucesso!")

if __name__ == "__main__":
    main()


# Subir aplicação index: uvicorn main:app --host 0.0.0.0 --port 8000 --reload