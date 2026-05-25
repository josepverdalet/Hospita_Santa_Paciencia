# Característiques principals
Interfície Gràfica (GUI): Desenvolupada íntegramente amb la llibreria tkinter.

# Seguretat Avançada:

Hashing de contrasenyes: S'utilitza la llibreria bcrypt perquè les contrasenyes mai es guardin en text pla.

Xifrat de fitxers: Les dades d'usuari s'emmagatzemen en un fitxer separat i xifrat mitjançant cryptography (Fernet) per complir amb els requisits de màxima seguretat (protecció tant d'usuari com de contrasenya).

Connectivitat: Gestió de connexions a la base de dades PostgreSQL mitjançant psycopg2.

Modularitat: Codi dividit en mòduls per facilitar el manteniment i l'escalabilitat del projecte.

# Estructura del Projecte
El projecte s'organitza en els següents fitxers:

main.py: És el punt d'entrada de l'aplicació. Gestiona la finestra de Tkinter, els camps d'entrada de text i la lògica dels botons de "Login" i "Registre".

seguretat.py: Conté tota la lògica de seguretat. S'encarrega de xifrar el fitxer d'accés, generar les claus secretoes i verificar que la contrasenya introduïda coincideixi amb la guardada.

database.py: Centralitza la configuració de la base de dades. Aquí es defineixen els paràmetres de connexió (host, usuari, contrasenya de la BD).

Llibrerias necessarias: psycopg2-binary, bcrypt, cryptography

# Instal·lació i Configuració
1. Clonar el repositori i crear l'entorn virtual
Es recomana l'ús d'un entorn virtual per mantenir les dependències aïllades:

# Crear l'entorn virtual
python -m venv venv

# Activar l'entorn
venv\Scripts\activate

pip install psycopg2-binary bcrypt cryptography

# Configurar la Base de Dades
Assegura't de tenir PostgreSQL funcionant i modifica les dades a database.py:

host: Adreça del servidor.

database: Nom de la teva base de dades de l'hospital.

user: El teu usuari de Postgres.

password: La teva contrasenya d'accés a la BD.

# Execució
Per iniciar l'aplicació, executa el fitxer principal: main.py
