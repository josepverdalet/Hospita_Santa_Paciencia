import psycopg2
from tkinter import messagebox

def connectar_bd():
    try:
        conn = psycopg2.connect(
            host="192.168.56.105",
            database="hospital",
            user="postgres",
            password="12345",
        )
        cur = conn.cursor()
        # Forcem l'esquema hospital
        cur.execute("SET search_path TO hospital, public;")     
        cur.close()
        return conn
    except Exception as e:
        print(f"Error de connexió: {e}")
        return None