# -*- coding: utf-8 -*-

# Importar biblioteca psycopg2
import psycopg2

# Criar uma conexão com o banco de dados
conn = psycopg2.connect('dbname=movies user=guga password=gugasv2 host=127.0.0.1')

# Criar um cursor para manipular o banco de dados
cur = conn.cursor()

# Executar as queries do banco de dados
cur.execute("INSERT INTO ator (nome, data_nasc, bio) VALUES ('Tom Hanks', '1956-07-09', 'Thomas Jeffrey Hanks (born July 9, 1956) is an American actor and filmmaker.')")

conn.commit()
