import psycopg2
from config import config


def connect():
    conn = None
    try:
        params = config(filename='database.ini', section='postgresql')
        conn = psycopg2.connect(**params)
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT version();"
            )
            print(f"Server version: {cursor.fetchone()}")
    except Exception as _ex:
        print(f"[INFO] Error while working with PostgreSQL {_ex}")
    if conn is not None:
        conn.close()
        print("[INFO] PostgreSQL connection closed")


connect()
