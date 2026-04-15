import psycopg2
from tkinter import messagebox

def connectar_bd():
    """Estableix la connexió. Retorna la conexió si té èxit, o None si falla."""
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
    
# Al final de tu archivo database.py, añade esto para probar:
if __name__ == "__main__":
    conexion = connectar_bd()
    if conexion:
        print("La variable 'conexion' ya tiene el control de la BD.")
        conexion.close() # Siempre es bueno cerrar al terminar la prueba