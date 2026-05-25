Sistema de Gestió Hospitalària - ASIX
Aquest projecte correspon al Bloc 1: Connectivitat i Login del projecte intermodular d'ASIX1. L'objectiu principal és permetre l'accés segur dels usuaris al sistema mitjançant una interfície gràfica, gestionant la seguretat de les credencials i la connexió amb una base de dades PostgreSQL.

Característiques principals
Interfície Gràfica (GUI): Desenvolupada íntegramente amb la llibreria tkinter.

Seguretat Avançada:

Hashing de contrasenyes: S'utilitza la llibreria bcrypt perquè les contrasenyes mai es guardin en text pla.

Xifrat de fitxers: Les dades d'usuari s'emmagatzemen en un fitxer separat i xifrat mitjançant cryptography (Fernet) per complir amb els requisits de màxima seguretat (protecció tant d'usuari com de contrasenya).

Connectivitat: Gestió de connexions a la base de dades PostgreSQL mitjançant psycopg2.

Modularitat: Codi dividit en mòduls per facilitar el manteniment i l'escalabilitat del projecte.

Estructura del Projecte
El projecte s'organitza en els següents fitxers:

main.py: És el punt d'entrada de l'aplicació. Gestiona la finestra de Tkinter, els camps d'entrada de text i la lògica dels botons de "Login" i "Registre".

seguretat.py: Conté tota la lògica de seguretat. S'encarrega de xifrar el fitxer d'accés, generar les claus secretoes i verificar que la contrasenya introduïda coincideixi amb la guardada.

database.py: Centralitza la configuració de la base de dades. Aquí es defineixen els paràmetres de connexió (host, usuari, contrasenya de la BD).

requirements.txt: Llista de llibreries externes necessàries perquè el projecte funcioni en qualsevol ordinador.

Instal·lació i Configuració
1. Clonar el repositori i crear l'entorn virtual
Es recomana l'ús d'un entorn virtual per mantenir les dependències aïllades:

# Crear l'entorn virtual
python -m venv venv

# Activar l'entorn
venv\Scripts\activate

pip install psycopg2-binary bcrypt cryptography

3. Configurar la Base de Dades
Assegura't de tenir PostgreSQL funcionant i modifica les dades a database.py:

host: Adreça del servidor .

database: Nom de la teva base de dades de l'hospital.

user: El teu usuari de Postgres.

password: La teva contrasenya d'accés a la BD.

Execució
Per iniciar l'aplicació, executa el fitxer principal:

python main.py

Explicació del flux de treball
Registre: En introduir un usuari i contrasenya per primera vegada i polsar "Registrar", el sistema genera una clau única (secret.key) i crea un fitxer xifrat (access.dat). Dins d'aquest fitxer es guarda el hash de la contrasenya.

Inici de Sessió:

El sistema obre access.dat i en desxifra el contingut.

Compara el hash guardat amb la contrasenya escrita fent servir bcrypt.

Si és correcte, procedeix a obrir la connexió amb PostgreSQL.

Si la connexió té èxit, es mostra un missatge de confirmació i es tanca la connexió de forma segura (conn.close()).
