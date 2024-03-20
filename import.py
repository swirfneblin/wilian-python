import pandas as pd
import sqlite3

# Carregar os arquivos CSV para DataFrames pandas
df1 = pd.read_csv('satisfacao.csv', sep=';')
df2 = pd.read_csv('metricas.csv', sep=';')

# Conectar ao banco de dados SQLite
conn = sqlite3.connect('seu_banco_de_dados.db')

# Salvar os DataFrames como tabelas no banco de dados SQLite
df1.to_sql('satisfacao', conn, if_exists='replace', index=False)
df2.to_sql('metricas', conn, if_exists='replace', index=False)

# Fechar a conexão com o banco de dados
conn.close()

