### PAINEL DE INDICADORES EDUCACIONAIS DO BRASIL

Este projeto tem como objetivo desenvolver um painel de indicadores educacionais utilizando um pipeline ETL (Extração, Transformação e Carga), armazenamento de dados em PostgreSQL e visualização no Power BI. A solução oferece uma visão clara e interativa sobre taxas de aprovação, reprovação e abandono escolar.

## ESTRUTURA DO PROJETO

O projeto está dividido nas seguintes etapas:

ETL (Extração, Transformação e Carga)

Extração: Leitura de arquivos CSV contendo os dados brutos.
Transformação: Limpeza, normalização e cálculo de indicadores.
Carga: Armazenamento dos dados processados no banco de dados PostgreSQL.
Modelagem e Integração com Power BI

Criação de um modelo de dados otimizado para análise.
Conexão do Power BI ao banco de dados.
Criação do Painel de Indicadores

Construção de gráficos e tabelas dinâmicas para análise de indicadores.
Documentação e Otimização

Criação de documentação clara sobre o pipeline.
Avaliação de melhorias de desempenho e otimização de consultas.

## TECNOLOGIAS UTILIZADAS

Linguagem: Python

Banco de Dados: PostgreSQL

Ferramenta de Visualização: Power BI

Bibliotecas Python:
pandas
sqlalchemy
psycopg2
os (para variáveis de ambiente)

## EXECUTE O PROJETO

# REQUISITOS

Python 3.8 ou superior
PostgreSQL instalado e configurado
Power BI (para visualização)

# INSTALAÇÃO

CLONE:
git clone git@github.com:danilomassoni/painel-indicadores-educacionais-brasil.git
cd indicadores-educacionais

DEPENDÊNCIAS:
pip install -r requirements.txt

CONFIGURE O POSTGRESQL:
export DATABASE_URL="postgresql+psycopg2://usuario:senha@localhost:5432/painel_indicadores_educacionais"

EXECUTE O PROJETO:
python main.py

## CONTRIBUIÇÃO

Contribuições são bem-vindas! Para sugestões, melhorias ou correções, envie um pull request ou abra uma issue.

## LICENÇA

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais informações.
