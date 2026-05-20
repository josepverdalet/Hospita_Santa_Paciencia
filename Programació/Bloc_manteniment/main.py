import tkinter as tk
import os
from tkinter import messagebox
from seguretat import validar_login, registrar_usuari
from database import connectar_bd
from gui_manteniment import FinestraManteniment

class AplicacioHospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Santa Paciencia - Login")
        self.root.geometry("400x300")
        

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
        usuari = self.entry_usuari.get()
        pwd = self.entry_pass.get()
        
        if validar_login(usuari, pwd):
            conn = connectar_bd()
            if conn:
                conn.close()
                messagebox.showinfo("Èxit", f"Benvingut {usuari}")
                
                self.root.withdraw()
                FinestraManteniment(usuari)
            else:
                messagebox.showerror("Error de BD", "No s'ha pogut connectar amb els servidors de la base de dades.")
        else:
            messagebox.showerror("Error", "Usuari o contrasenya incorrectes")
        

    def registrar(self):
        usuari = self.entry_usuari.get()
        pwd = self.entry_pass.get()
        
        if usuari and pwd:
            try:
                registrar_usuari(usuari, pwd)
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