import psycopg2
from tkinter import messagebox

def connectar_bd():
    try:
        conn = psycopg2.connect(
            host="192.168.56.103",
            database="hospital_santa_paciencia",
            user="postgres",
            password="1234",
            sslmode="require"
        )
        cur = conn.cursor()
        # Forcem l'esquema hospital
        cur.execute("SET search_path TO hospital, public;")     
        cur.close()
        return conn
    except Exception as e:
        print(f"Error de connexió: {e}")
        return None