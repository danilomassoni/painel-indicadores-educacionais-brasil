# Arquitetura do Pipeline ETL

## VISÃO GERAL 

Este documento descreve a arquitetura do pipeline ETL (Extração, Transformação e Carga) para o projeto de indicadores educacionais. O objetivo é fornecer uma visão clara das etapas envolvidas, tecnologias usadas e o fluxo de dados.

## ESTRUTURA DO PROJETO

O pipeline é dividido em três principais etapas: Extração, Transformação e Carga, com os seguintes diretórios e arquivos principais:

etl_pipeline.py: Orquestração de todas as etapas do pipeline ETL.
extract.py: Contém funções para leitura e carregamento dos dados.
transform.py: Contém funções para limpeza e transformação dos dados.
load.py: Contém funções para carregamento de dados no banco de dados PostgreSQL.
database/schema.sql: Define a estrutura das tabelas utilizadas no banco de dados.

## ETAPAS DO PIPELINE ETL

# EXTRAÇÃO
-Os dados são extraídos de arquivos CSV armazenados em data/raw/.
-Verificação de qualidade dos dados, como formatos inválidos ou campos ausentes, antes de continuar para a próxima etapa.

# TRANSFORMAÇÃO
-Limpeza e normalização dos dados:
-Tratamento de valores nulos.
--Padronização de tipos de dados (e.g., conversão de strings para datas).
Criação de colunas úteis, como taxas de aprovação, reprovação e abandono.

## CARGA
-Os dados transformados são carregados para um banco de dados PostgreSQL.
-A tabela indicadores_educacionais é usada para armazenar os dados finais.

## DIAGRAMA DE FLUXO DE DADOS

Fluxograma TD
    A[Dados CSV] --> B[Extração]
    B --> C[Transformação]
    C --> D[Carga para PostgreSQL]

## TECNOLOGIAS UTILIZADAS
-Python: Linguagem de programação principal para o pipeline ETL.
-PostgreSQL: Banco de dados para armazenamento dos dados transformados.
-Power BI: Ferramenta de visualização conectada ao banco de dados para criação de relatórios e painéis.

## CONFIGURAÇÕES E VARIÁVEIS
-As credenciais e a URL do banco de dados são definidas por variáveis de ambiente (DATABASE_URL).
-Os arquivos de dados estão organizados nas seguintes pastas:
--data/raw/: Dados originais extraídos.
--data/processed/: Dados transformados e prontos para carga.


