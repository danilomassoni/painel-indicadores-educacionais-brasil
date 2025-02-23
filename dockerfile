# Usa uma imagem base do Python
FROM python:3.10

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copia os arquivos do projeto para dentro do contêiner
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta que será usada
EXPOSE 8000

# Comando para rodar a aplicação
CMD ["python", "app.py"]
