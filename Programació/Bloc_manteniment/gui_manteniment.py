import tkinter as tk
from tkinter import messagebox, simpledialog
from database import connectar_bd

class FinestraManteniment:
    def __init__(self, usuari):
        self.root = tk.Toplevel()
        self.root.title(f"Gestió Hospital - {usuari}")
        self.root.geometry("550x800")

        #BLOC DE MANTENIMENT
        tk.Label(self.root, text="ANNEX 3: MANTENIMENT", font=("Arial", 12, "bold"), fg="navy").pack(pady=10)
        tk.Button(self.root, text="Alta Nou Personal", width=45, command=self.alta_personal).pack(pady=3)
        tk.Button(self.root, text="Alta Nou Pacient", width=45, command=self.alta_pacient).pack(pady=3)
        tk.Button(self.root, text="Consultar Planta d'Infermer", width=45, command=self.check_infermer).pack(pady=3)
        tk.Button(self.root, text="Operacions Detallades (Dia)", width=45, command=self.operacions_detallades_dia).pack(pady=3)
        tk.Button(self.root, text="Visites Planificades (Dia)", width=45, command=self.visites_dia).pack(pady=3)
        
        #BLOC DE CONSULTES I INFORMES 
        tk.Label(self.root, text="ANNEX 4: CONSULTES I INFORMES", font=("Arial", 12, "bold"), fg="darkgreen").pack(pady=15)
        tk.Button(self.root, text="1. Recursos per Planta (Hab/Quir/Inf)", width=45, bg="#e8f5e9", command=self.recursos_planta).pack(pady=3)
        tk.Button(self.root, text="2. Informe: Tot el Personal de l'Hospital", width=45, bg="#e8f5e9", command=self.informe_personal).pack(pady=3)
        tk.Button(self.root, text="3. Informe: Nombre de Visites per Dia", width=45, bg="#e8f5e9", command=self.informe_visites_dia).pack(pady=3)

        tk.Label(self.root, text="--------------------------------------------------").pack(pady=10)
        tk.Button(self.root, text="Tancar Sessió", command=self.root.destroy, fg="red").pack(pady=5)

# bloc de manteniment

    def alta_personal(self):
        dni = simpledialog.askstring("Dades", "DNI:")
        nom = simpledialog.askstring("Dades", "Nom:")
        cognom = simpledialog.askstring("Dades", "Cognom:")
        telf = simpledialog.askstring("Dades", "Telèfon:")
        direccio = simpledialog.askstring("Dades", "Direcció:")
        tipus = simpledialog.askstring("Dades", "Tipus (MEDIC, INFERMERIA, VARI):").upper()
        extra = simpledialog.askstring("Dades", "Especialitat/Experiència/Feina:")
        
        if not dni or not nom or not tipus:
            messagebox.showwarning("Atenció", "DNI, Nom i Tipus són obligatoris.")
            return

        conn = connectar_bd()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute('CALL hospital.alta_treballador_hospital(%s, %s, %s, %s, %s, %s, %s)', 
                            (dni, nom, cognom, telf, direccio, tipus, extra))
                
                if tipus == "INFERMERIA":
                    cur.execute('SELECT id_empleat FROM hospital.treballador WHERE dni = %s', (dni,))
                    id_nou = cur.fetchone()[0]
                    planta = simpledialog.askinteger("Assignació", f"A quina PLANTA assignem a {nom}? (Buit si no en té):")
                    if planta:
                        cur.execute('INSERT INTO hospital.assigna (id_empleat, id_planta) VALUES (%s, %s)', (id_nou, planta))
                        messagebox.showinfo("Assignació", f"Infermer/a assignat/da a la planta {planta}.")
                    else:
                        messagebox.showinfo("Assignació", "Sense planta assignada. Dependrà d'un metge.")

                conn.commit()
                messagebox.showinfo("Èxit", f"Personal '{nom}' registrat correctament.")
            except Exception as e:
                conn.rollback()
                messagebox.showerror("Error", f"Error en l'alta: {e}")
            finally: conn.close()

    def alta_pacient(self):
        dni = simpledialog.askstring("Dades", "DNI:")
        nom = simpledialog.askstring("Dades", "Nom:")
        telf = simpledialog.askstring("Dades", "Telèfon:")
        if dni and nom:
            conn = connectar_bd()
            if conn:
                try:
                    cur = conn.cursor()
                    cur.execute('INSERT INTO hospital.pacient (dni, nom, telefon) VALUES (%s, %s, %s)', (dni, nom, telf))
                    conn.commit()
                    messagebox.showinfo("Èxit", "Pacient guardat.")
                finally: conn.close()

    def check_infermer(self):
        id_emp = simpledialog.askinteger("Consulta", "Introdueix l'ID de l'empleat d'infermeria:")
        if not id_emp: return
        conn = connectar_bd()
        if conn:
            try:
                cur = conn.cursor()
                cur.execute('SELECT id_planta FROM hospital.assigna WHERE id_empleat = %s', (id_emp,))
                resultat = cur.fetchone()
                if resultat:
                    messagebox.showinfo("Resultat", f"L'empleat ID {id_emp} ÉS de planta.\n\nPLANTA: {resultat[0]}")
                else:
                    messagebox.showinfo("Resultat", f"L'ID {id_emp} no té planta assignada (depèn d'un metge).")
            finally: conn.close()

    def operacions_detallades_dia(self):
        data = simpledialog.askstring("Consulta", "Introdueix la data (Format: AAAA-MM-DD):")
        if not data: return
        
        conn = connectar_bd()
        if conn:
            try:
                cur = conn.cursor()
                # Com que 'operacio' ja té el dia i hora, fem els JOINs directament des d'allà
                query = '''
                    SELECT 
                        o.id_quirofan,
                        o.hora,
                        p.nom AS nom_pacient,
                        t_med.nom AS nom_metge,
                        COALESCE(STRING_AGG(t_inf.nom || ' ' || t_inf.cognom, ', '), 'Cap assignat') AS personal_infermeria
                    FROM hospital.operacio o
                    JOIN hospital.pacient p ON o.id_pacient = p.id_pacient
                    JOIN hospital.treballador t_med ON o.id_medic = t_med.id_empleat
                    LEFT JOIN hospital.assisteix a ON o.id_operacio = a.id_operacio
                    LEFT JOIN hospital.treballador t_inf ON a.id_empleat = t_inf.id_empleat
                    WHERE o.dia = %s
                    GROUP BY o.id_quirofan, o.hora, p.nom, t_med.nom
                    ORDER BY o.id_quirofan ASC, o.hora ASC
                '''
                cur.execute(query, (data,))
                resultats = cur.fetchall()
                
                self.mostrar_taula(
                    f"Operacions Quiròfan - {data}", 
                    "Quiròfan | Hora | Pacient | Metge/ssa | Personal Infermeria", 
                    resultats
                )
            except Exception as e:
                messagebox.showerror("Error SQL", f"Error en la consulta d'operacions: {e}")
            finally: 
                conn.close()

    def visites_dia(self):
        data = simpledialog.askstring("Consulta", "Introdueix la data (Format: 2007-01-01):")
        if data:
            conn = connectar_bd()
            if conn:
                try:
                    cur = conn.cursor()
                    query = 'SELECT id_visita, hora, id_pacient, id_empleat FROM hospital.visita WHERE dia = %s'
                    cur.execute(query, (data,))
                    self.mostrar_taula(f"Visites del dia {data}", "ID Visita | Hora | ID Pacient | ID Mèdic", cur.fetchall())
                finally: conn.close()

# CONSULTES I INFORMES
    
    def recursos_planta(self):
        id_planta = simpledialog.askinteger("Annex 4", "Introdueix l'ID o Número de la planta:")
        if not id_planta: return
        
        conn = connectar_bd()
        if conn:
            try:
                cur = conn.cursor()
                
                cur.execute('SELECT COUNT(*) FROM hospital.habitacio WHERE id_planta = %s', (id_planta,))
                habs = cur.fetchone()[0]
                
                cur.execute('SELECT COUNT(*) FROM hospital.quirofan WHERE id_planta = %s', (id_planta,))
                quirs = cur.fetchone()[0]
                
                cur.execute('SELECT COUNT(*) FROM hospital.assigna WHERE id_planta = %s', (id_planta,))
                infs = cur.fetchone()[0]
                
                resum = [
                    ["Habitacions totals", habs],
                    ["Quiròfans totals", quirs],
                    ["Personal d'Infermeria", infs]
                ]
                self.mostrar_taula(f"Recursos Planta {id_planta}", "Recurs o Atribut | Quantitat Trobadada", resum)
                
            except Exception as e:
                messagebox.showerror("Error", f"Error en calcular recursos: {e}")
            finally: conn.close()

    def informe_personal(self):
        conn = connectar_bd()
        if conn:
            try:
                cur = conn.cursor()
                query = '''
                    SELECT t.id_empleat, t.dni, t.nom, t.cognom, t.telefon,
                           CASE 
                               WHEN m.id_empleat IS NOT NULL THEN 'MÈDIC (' || m.especialitat || ')'
                               WHEN i.id_empleat IS NOT NULL THEN 'INFERMERIA (' || i.experiencia || ')'
                               WHEN v.id_empleat IS NOT NULL THEN 'VARI (' || v.tipus_feina || ')'
                               ELSE 'SENSE CATEGORIA'
                           END as rol
                    FROM hospital.treballador t
                    LEFT JOIN hospital.medic m ON t.id_empleat = m.id_empleat
                    LEFT JOIN hospital.infermeria i ON t.id_empleat = i.id_empleat
                    LEFT JOIN hospital.vari v ON t.id_empleat = v.id_empleat
                    ORDER BY t.id_empleat ASC
                '''
                cur.execute(query)
                self.mostrar_taula("Informe General de Personal", "ID | DNI | Nom | Cognom | Telèfon | Rol / Categoria", cur.fetchall())
            except Exception as e:
                messagebox.showerror("Error", f"Error a l'informe de personal: {e}")
            finally: conn.close()

    def informe_visites_dia(self):
        conn = connectar_bd()
        if conn:
            try:
                cur = conn.cursor()
                query = '''
                    SELECT dia, COUNT(id_visita)
                    FROM hospital.visita
                    GROUP BY dia
                    ORDER BY dia DESC
                '''
                cur.execute(query)
                self.mostrar_taula("Informe: Visites totals per Dia", "Data (Dia) | Nombre de Visites Registrades", cur.fetchall())
            except Exception as e:
                messagebox.showerror("Error", f"Error a l'informe de visites: {e}")
            finally: conn.close()


    def mostrar_taula(self, titol, cap, dades):
        win = tk.Toplevel(self.root)
        win.title(titol)
        txt = tk.Text(win, width=80, height=15)
        txt.pack(padx=10, pady=10)
        txt.insert(tk.END, cap + "\n" + "-"*75 + "\n")
        if not dades: txt.insert(tk.END, "Sense resultats per a aquesta consulta.")
        for f in dades: txt.insert(tk.END, " | ".join(map(str, f)) + "\n")
        txt.config(state=tk.DISABLED)