import psycopg2
from tkinter import messagebox

def connectar_bd():
    try:
        conn = psycopg2.connect(
            host="192.168.56.105",
            database="postgres",
            user="postgres",
            password="12345"
        )
        print("Connexió a PostgreSQL establerta correctament.")
        return conn

    except Exception as e:
        messagebox.showerror("Error de BD", f"No s'ha pogut connectar: {e}")
        return None  
    
