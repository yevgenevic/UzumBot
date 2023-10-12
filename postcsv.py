import pandas as pd
import psycopg2
from sqlalchemy import create_engine

conn = psycopg2.connect(
    host='95.163.241.85',
    database='ke_bot',
    user='postgres',
    password='1'
)

engine = create_engine(f'postgresql://postgres:1@localhost:5432/ke_bot')


def ostatki_db(csv_url):
    df = pd.read_csv(csv_url)
    df.to_sql('ostatki', engine, if_exists='replace', index=False)

    conn.close()


def prodaja_db(csv_url):
    df = pd.read_csv(csv_url)
    df.to_sql('prodaja', engine, if_exists='replace', index=False)

    conn.close()
