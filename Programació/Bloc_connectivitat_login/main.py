import tkinter as tk
import os
from tkinter import messagebox
from seguretat import validar_login, registrar_usuari
from database import connectar_bd

class AplicacioHospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital ASIX - Login")
        self.root.geometry("400x300")
        
        # Elements de la interfície
        tk.Label(root, text="SISTEMA HOSPITALARI", font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(root, text="Usuari:").pack()
        self.entry_usuari = tk.Entry(root)
        self.entry_usuari.pack(pady=5)
        
        tk.Label(root, text="Contrasenya:").pack()
        self.entry_pass = tk.Entry(root, show="*")
        self.entry_pass.pack(pady=5)
        
        # Botons
        tk.Button(root, text="Iniciar Sessió", command=self.login, bg="lightblue").pack(pady=10)
        tk.Button(root, text="Registrar Nou Usuari", command=self.registrar).pack()

    def login(self):
        """Gestiona l'intent de login."""
        usuari = self.entry_usuari.get()
        pwd = self.entry_pass.get()
        
        if validar_login(usuari, pwd):
            # Si el login és correcte, provem la connectivitat a la BD
            conn = connectar_bd()
            if conn:
                messagebox.showinfo("Èxit", f"Benvingut {usuari}. Connexió a BD establerta.")
                # Aquí tancaríem aquesta finestra i obriríem el menú principal
                conn.close()
        else:
            messagebox.showerror("Error", "Usuari o contrasenya incorrectes")

    def registrar(self):
        """Funció d'ajuda per crear usuaris inicials amb missatges de depuració."""
        usuari = self.entry_usuari.get()
        pwd = self.entry_pass.get()
        
        if usuari and pwd:
            try:
                registrar_usuari(usuari, pwd)
                # Això et dirà ON s'està guardant realment
                ruta = os.path.abspath("access.dat")
                messagebox.showinfo("Registre", f"Usuari registrat!\nFitxer creat a: {ruta}")
            except Exception as e:
                messagebox.showerror("Error greu", f"No s'ha pogut crear el fitxer: {e}")
        else:
            messagebox.showwarning("Atenció", "Omple els camps per registrar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacioHospital(root)
    root.mainloop()