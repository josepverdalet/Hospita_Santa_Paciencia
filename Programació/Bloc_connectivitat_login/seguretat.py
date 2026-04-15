import json
import os
import bcrypt
from cryptography.fernet import Fernet

# Fitxer on es guarden les credencials
CREDENTIALS_FILE = "access.dat"
# Clau de xifrat
KEY_FILE = "secret.key"

def carregar_o_crear_clau():
    """Genera o carrega una clau per xifrar el fitxer d'usuaris."""
    if not os.path.exists(KEY_FILE):
        clau = Fernet.generate_key()
        with open(KEY_FILE, "wb") as kf:
            kf.write(clau)
    else:
        with open(KEY_FILE, "rb") as kf:
            clau = kf.read()
    return Fernet(clau)

def registrar_usuari(usuari, contrasenya):
    """Guarda un usuari nou al fitxer separat amb seguretat total."""
    f = carregar_o_crear_clau()
    
    # Hashegem la contrasenya amb bcrypt
    pwd_hash = bcrypt.hashpw(contrasenya.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    dades = {}
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "rb") as file:
            contingut_xifrat = file.read()
            dades = json.loads(f.decrypt(contingut_xifrat))
    
    dades[usuari] = pwd_hash
    
    # Xifrem tot el diccionari (així l'usuari també està protegit)
    dades_xifrades = f.encrypt(json.dumps(dades).encode())
    with open(CREDENTIALS_FILE, "wb") as file:
        file.write(dades_xifrades)

def validar_login(usuari, contrasenya):
    """Verifica les credencials comparant el hash."""
    if not os.path.exists(CREDENTIALS_FILE):
        return False
    
    f = carregar_o_crear_clau()
    with open(CREDENTIALS_FILE, "rb") as file:
        contingut_xifrat = file.read()
        dades = json.loads(f.decrypt(contingut_xifrat))
    
    if usuari in dades:
        hash_guardat = dades[usuari].encode('utf-8')
        return bcrypt.checkpw(contrasenya.encode('utf-8'), hash_guardat)
    return False