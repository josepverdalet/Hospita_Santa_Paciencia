# Prova de Recuperació davant Desastres (Disaster Recovery)

A continuació es detallen les comandes executades per verificar que el sistema de còpies de seguretat i restauració funciona correctament:

## 1. Generació del Backup inicial
Primer s'executa l'script de backup automatitzat per tenir una imatge actual de la base de dades:

      # Execució de l'script de backup
      sudo ~/scripts/backup_bd.sh

      # Verificació de la creació del fitxer SQL
       ls -lh /var/backups/postgres
       
2. Simulació de pèrdua de dades (El Desastre)
S'accedeix a la base de dades i s'elimina una taula crítica per simular un error humà o una fallada del sistema:

        # Accés a la base de dades de l'hospital
       sudo -u postgres psql -d hospital_santa_paciencia

        # Eliminació de la taula dins de l'esquema 'hospital'
        DROP TABLE hospital.reserva;

        # Comprovació que la taula ja no existeix
        \dt hospital.*
       \q
3. Execució de l'script de restauració
S'utilitza l'script de restauració total creat prèviament, indicant la ruta del fitxer de backup generat en el pas 1:


        # Restauració total de la base de dades
        # (Substituir 'backup_XXXX.sql' pel nom real del fitxer)
        sudo ~/scripts/restore_total.sh /var/backups/postgres/backup_XXXX.sql
4. Verificació final del sistema
Es comprova que la taula reserva s'ha tornat a crear amb tot el seu contingut original:

        # Consulta directa per verificar la recuperació de les dades
        sudo -u postgres psql -d hospital_santa_paciencia -c "SELECT * FROM hospital.reserva LIMIT 5;"
