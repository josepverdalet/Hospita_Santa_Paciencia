import psycopg2
from psycopg2.extras import execute_values
from faker import Faker
import random
from datetime import datetime, timedelta

# Inicialitzem Faker en espanyol per a noms, cognoms i adreces
fake = Faker('es_ES')

# La teva configuració exacta del servidor Ubuntu
DB_PARAMS = {
    "host": "192.168.56.103",
    "database": "hospital_santa_paciencia",
    "user": "postgres",
    "password": "1234",
    "port": "5432"
}

def calcular_dni_real(numero):
    """Genera un DNI amb format i lletra completament vàlida per a Espanya."""
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    num_str = f"{numero:08d}"
    letra = letras[numero % 23]
    return f"{num_str}{letra}"

def ejecutar_generacio_directa():
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        cursor = conn.cursor()
    except Exception as e:
        print(f"❌ Error de conexión al servidor Ubuntu (192.168.56.103): {e}")
        return

    print("🚀 [PYTHON] ¡Conectado correctamente! Iniciando vaciado e inserción masiva...")
    
    try:
        # Forcem l'esquema 'hospital'
        cursor.execute("SET search_path TO hospital;")

        # --- A. NETEJA EN CASCADA ---
        print("🧹 Vaciando tablas antiguas en el esquema 'hospital'...")
        taules = [
            "RECEPTE", "ASSISTEIX", "ASSIGNA", "RESERVA", "VISITA", "OPERACIO", 
            "APARELL_MEDIC", "HABITACIO", "QUIROFAN", "PLANTA", "MEDIC", 
            "INFERMERIA", "VARI", "TREBALLADOR", "PACIENT", "MEDICAMENT"
        ]
        for taula in taules:
            cursor.execute(f"TRUNCATE TABLE {taula} RESTART IDENTITY CASCADE;")

        # --- B. TREBALLADORS ---
        print("➡️ Generando 400 Trabajadores...")
        treballadors_data = []
        for i in range(1, 401):
            dni_trabajador = calcular_dni_real(10000000 + i)
            treballadors_data.append((
                i, dni_trabajador, fake.first_name(), fake.last_name(),
                fake.phone_number()[:15], fake.address().replace('\n', ', ')
            ))
        execute_values(cursor, "INSERT INTO TREBALLADOR (id_empleat, dni, nom, cognom, telefon, direccio) VALUES %s;", treballadors_data)
        
        ids_medics = list(range(1, 101))       
        ids_infermers = list(range(101, 301))   
        ids_varis = list(range(301, 401))       
        
        # --- C. MEDICS ---
        print("➡️ Generando Médicos...")
        especialitats = ['Pediatria', 'Cardiologia', 'Traumatologia', 'Medicina General', 'Urgències', 'Neurologia', 'Ginecologia']
        medics_data = [(id_emp, random.choice(especialitats), "Universitat de Barcelona", "CV exten...") for id_emp in ids_medics]
        execute_values(cursor, "INSERT INTO MEDIC (id_empleat, especialitat, estudi, cv) VALUES %s", medics_data)
        
        # --- D. INFERMERIA ---
        print("➡️ Generando Enfermería...")
        infermeria_data = [(id_emp, random.randint(1, 25), random.choice(['Matí', 'Tarda', 'Nit'])) for id_emp in ids_infermers]
        execute_values(cursor, "INSERT INTO INFERMERIA (id_empleat, experiencia, disponibilitat) VALUES %s", infermeria_data)
        
        # --- E. VARI ---
        print("➡️ Generando Personal Vario...")
        tipus_feina_llista = ['Neteja', 'Administració', 'Manteniment', 'Seguretat']
        vari_data = [(id_emp, random.choice(tipus_feina_llista)) for id_emp in ids_varis]
        execute_values(cursor, "INSERT INTO VARI (id_empleat, tipus_feina) VALUES %s", vari_data)
        
        # --- F. PLANTA ---
        print("➡️ Generando Plantas (sin columna de empleado)...")
        plantes_data = []
        tipus_plantes = ['Urgències', 'Pediatria', 'Planta General A', 'Planta General B', 'Maternitat']
        for i in range(1, 6):
            plantes_data.append((i, i, tipus_plantes[i-1])) 
        execute_values(cursor, "INSERT INTO PLANTA (id_planta, numero, tipus) VALUES %s", plantes_data)
        
        # --- G. HABITACIONS I QUIROFANS ---
        print("➡️ Generando Habitaciones y Quirófanos...")
        habitacions_data = []
        id_hab = 1
        for id_planta in range(1, 6):
            for num_hab in range(101, 111): 
                habitacions_data.append((id_hab, num_hab + (id_planta * 100), random.choice([1, 2, 4]), id_planta))
                id_hab += 1
        execute_values(cursor, "INSERT INTO HABITACIO (id_habitacio, numero, capacitat, id_planta) VALUES %s", habitacions_data)
        
        quirofans_data = []
        for i in range(1, 6): 
            quirofans_data.append((i, random.choice(['General', 'Cardiovascular', 'Pediàtric']), i))
        execute_values(cursor, "INSERT INTO QUIROFAN (id_quirofan, tipus, id_planta) VALUES %s", quirofans_data)
        
        # --- H. APARELL_MEDIC ---
        print("➡️ Generando Aparatos Médicos...")
        aparells = ['Desfibril·lador', 'Monitor de Constants', 'Ecocardiògraf', 'Respirador']
        aparells_data = [(i, random.choice(aparells), random.randint(1, 3), random.randint(1, 5)) for i in range(1, 21)]
        execute_values(cursor, "INSERT INTO APARELL_MEDIC (id_serie, tipus, quantitat, id_quirofan) VALUES %s", aparells_data)

        # --- I. MEDICAMENTS ---
        print("➡️ Generando Medicamentos...")
        noms_medicaments = ['Paracetamol 1g', 'Ibuprofèn 600mg', 'Amoxicil·lina 500mg', 'Omeprazol 20mg', 'Aspirina 100mg', 'Nolotil', 'Diazepam']
        medicaments_data = [(i, nom, random.randint(10, 500)) for i, nom in enumerate(noms_medicaments, start=1)]
        execute_values(cursor, "INSERT INTO MEDICAMENT (id_medicament, nom, stock) VALUES %s", medicaments_data)

        # --- J. PACIENTS (⚠️ 50.000 REGISTRES) ---
        print("➡️ Generando 50.000 Pacientes...")
        pacients_data = []
        for i in range(1, 50001):
            dni_paciente = calcular_dni_real(20000000 + i)
            pacients_data.append((
                i, dni_paciente, fake.first_name(), fake.last_name(), fake.free_email(), fake.phone_number()[:15]
            ))
        execute_values(cursor, "INSERT INTO PACIENT (id_pacient, dni, nom, cognom, email, telefon) VALUES %s", pacients_data)

        # --- K. VISITES (⚠️ 100.000 REGISTRES) ---
        print("➡️ Generando 100.000 Visitas...")
        visites_data = []
        diagnostics = ['Constipat comú', 'Grip A', 'Esquinç de tormell', 'Dolor abdominal', 'Revisió rutinària', 'Cefalea', 'Hipertensió']
        for i in range(1, 100001):
            data_aleatoria = fake.date_between(start_date='-1y', end_date='today')
            hora_aleatoria = f"{random.randint(0,23):02d}:{random.randint(0,59):02d}:00"
            visites_data.append((
                i, data_aleatoria, hora_aleatoria, random.choice(diagnostics), random.randint(1, 50000), random.choice(ids_medics)
            ))
        execute_values(cursor, "INSERT INTO VISITA (id_visita, dia, hora, diagnostic, id_pacient, id_medic) VALUES %s", visites_data)

        # --- L. OPERACIONS, RESERVES I RELACIONS ---
        print("➡️ Generando Operaciones y Reservas (sin columna 'nom' en OPERACIO)...")
        operacions_data = []
        for i in range(1, 501):
            # Eliminat el random.choice(noms_operacions)
            operacions_data.append((
                i, 'Urgent' if i % 3 == 0 else 'Programada',
                random.randint(1, 5), random.randint(1, 50000), random.choice(ids_medics)
            ))
        # Treta la columna 'nom' de la sentència SQL d'inserció
        execute_values(cursor, "INSERT INTO OPERACIO (id_operacio, tipus, id_quirofan, id_pacient, id_medic) VALUES %s", operacions_data)

        reserves_data = []
        for i in range(1, 1001):
            dia_ing = fake.date_between(start_date='-6m', end_date='today')
            dia_sort = dia_ing + timedelta(days=random.randint(1, 7))
            reserves_data.append((
                i, dia_ing, "08:00:00", dia_sort, "12:00:00", "Ingrés post-operatori",
                random.randint(1, 50), random.randint(1, 50000), None, random.choice(ids_medics)
            ))
        execute_values(cursor, "INSERT INTO RESERVA (id_reserva, dia_ingres, hora_ingres, dia_sortida, hora_sortida, motiu, id_habitacio, id_pacient, id_quirofan, id_medic) VALUES %s", reserves_data)

        print("➡️ Vinculando Recetas...")
        receptes_data = set()
        while len(receptes_data) < 5000:
            receptes_data.add((random.randint(1, len(noms_medicaments)), random.randint(1, 100000)))
        execute_values(cursor, "INSERT INTO RECEPTE (id_medicament, id_visita) VALUES %s", list(receptes_data))

        print("➡️ Vinculando Asignaciones de Planta...")
        assigna_data = set()
        for id_inf in ids_infermers:
            assigna_data.add((id_inf, random.randint(1, 5)))
        execute_values(cursor, "INSERT INTO ASSIGNA (id_empleat, id_planta) VALUES %s", list(assigna_data))

        conn.commit()
        print("🎉 [ÉXITO] ¡DUMMY DATA GENERADO CORRECTAMENTE EN TU SERVIDOR UBUNTU!")

    except Exception as e:
        conn.rollback()
        print(f"❌ Error durante la inserción de datos: {e}")
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    ejecutar_generacio_directa()