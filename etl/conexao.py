from sqlalchemy import create_engine

db_url = "postgresql://postgres:1234@localhost:5432/painel_indicadores_educacionais"

try:
    engine = create_engine(db_url)
    connection = engine.connect()
    print("✅ Conexão com o PostgreSQL bem-sucedida!")
    connection.close()
except Exception as e:
    print(f"❌ Erro ao conectar ao PostgreSQL: {e}")