# Módulo principal do projeto

from etl.etl_pipeline import run_etl

def main():
    """
    Ponto de entrada do projeto de Engenharia de Dados.
    """
    print("Iniciando o Projeto de Engenharia de Dados.....")
    run_etl()
    print("Pipeline ETL executado com sucesso!")

if __name__ == "__main__":
    main()