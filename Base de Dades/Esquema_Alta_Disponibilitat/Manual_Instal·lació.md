# Manual d'Instal·lació i Administració de la Rèplica de Base de Dades
## Projecte: Alta Disponibilitat PostgreSQL (Node 1 Local - Node 2 Cloud)

Aquest document detalla el procés de configuració d'un sistema de base de dades en alta disponibilitat utilitzant la replicació nativa de PostgreSQL entre un node primari i un node de rèplica.

---

## 1. Configuració de la Infraestructura (VirtualBox)

Per permetre la comunicació entre els nodes i l'accés a internet, ambdues màquines virtuals han de tenir la següent configuració de xarxa:

* **Adaptador 1:** NAT (Proporciona accés a Internet per a la instal·lació de paquets).
* **Adaptador 2:** Adaptador d'un sol amfitrió (Host-Only). Crea una xarxa privada per a la replicació.

### Assignació d'IPs Estàtiques:

| Node | Rol | Adreça IP |
| :--- | :--- | :--- |
| **Node 1** | Actiu / Primari | `192.168.56.103` |
| **Node 2** | Passiu / Rèplica | `192.168.56.104` |

---

## 2. Configuració del Node 1 (Servidor Primari)

2.1. Creació de l'usuari de replicació
Accedim a PostgreSQL i creem el rol amb permisos específics per a la rèplica:

    sudo -u postgres psql -c "CREATE ROLE replica_user REPLICATION LOGIN PASSWORD '1234';"

2.2. Configuració del fitxer postgresql.conf

Editem el fitxer de configuració principal:

    sudo nano /etc/postgresql/16/main/postgresql.conf

Modifiquem els següents paràmetres (treient el símbol # si és necessari):

    listen_addresses = '*'

    wal_level = replica

    max_wal_senders = 10

2.3. Configuració d'accés (pg_hba.conf)

Hem de permetre que el Node 2 es connecti. 

Editem el fitxer d'autenticació:

    sudo nano /etc/postgresql/16/main/pg_hba.conf

Afegim la següent línia al final:

    host replication replica_user 192.168.56.104/32 md5

2.4. Reinici del servei
Apliquem els canvis:

    sudo systemctl restart postgresql

## 3. Configuració del Node 2 (Servidor de Rèplica)

3.1. Instal·lació de programari
Si el Node 2 és una instal·lació neta, instal·lem PostgreSQL:

            sudo apt update
            sudo apt install postgresql-16 postgresql-client-16 -y

3.2. Preparació del directori de dades
Aturem el servei i buidem el directori de dades:

    sudo systemctl stop postgresql
    sudo rm -rf /var/lib/postgresql/16/main/*

3.3. Clonació de la base de dades (Backup Base)
Sincronitzem les dades des del Node 1:

    sudo -u postgres pg_basebackup -h 192.168.56.103 -D /var/lib/postgresql/16/main/ -U replica_user -P -R

3.4. Posada en marxa
Iniciem el servei al Node 2:

    sudo systemctl start postgresql

## 4. Verificació de la Replicació
4.1: Escriptura al Node 1

          sudo -u postgres psql -c "CREATE TABLE comprobacio_final (id SERIAL PRIMARY KEY, missatge TEXT);"
          sudo -u postgres psql -c "INSERT INTO comprobacio_final (missatge) VALUES ('Replicacio funcionant correctament');"
4.2: Lectura al Node 2

    sudo -u postgres psql -c "SELECT * FROM comprobacio_final;"

## 5. Estratègia de Backups

5.1. Creació de l'Script de Backup
   
          mkdir -p ~/scripts
          nano ~/scripts/backup_bd.sh

Contingut de l'script:

    #!/bin/bash
    # Script de Backup - Hospital Santa Paciencia

    # Configuració
    DATE=$(date +%Y%m%d_%H%M%S)
    BACKUP_DIR="/var/backups/postgres"
    DB_NAME="hospital_santa_paciencia"
    KEEP_DAYS=5

    # Crear directori i assegurar permisos
    sudo mkdir -p $BACKUP_DIR
    sudo chown postgres:postgres $BACKUP_DIR

    # Execució del dump
    sudo -u postgres pg_dump $DB_NAME > $BACKUP_DIR/backup_$DATE.sql

    # Neteja de fitxers antics (més de 5 dies)
    sudo find $BACKUP_DIR -type f -mtime +$KEEP_DAYS -name "*.sql" -delete

5.2. Permisos i Prova Tècnica

    chmod +x ~/scripts/backup_bd.sh
    ~/scripts/backup_bd.sh
    ls -lh /var/backups/postgres

5.3. Automatització amb Crontab

Editem el crontab (crontab -e) i afegim:

    00 03 * * * /home/vicifu007/scripts/backup_bd.sh
