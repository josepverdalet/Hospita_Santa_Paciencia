Aquesta comanda crea el certificat (.crt) i la clau privada (.key) alhora:

```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:4096 \
  -keyout /etc/postgresql/ssl/server.key \
  -out /etc/postgresql/ssl/server.crt \
  -subj "/CN=192.168.56.102"
```


Guia de Configuració SSL per a PostgreSQL Aquest document detalla com preparar i automatitzar la seguretat SSL al servidor.
1. Preparació de carpetes i permisos Primer creem el directori on es guardaran els certificats i assignem la propietat a l'usuari
   postgres:
```bash
sudo mkdir -p /etc/postgresql/ssl sudo chown postgres:postgres /etc/postgresql/ssl sudo chmod 700 /etc/postgresql/ssl 
```
2. Script de renovació automàtica Aquest script generarà un nou certificat vàlid per a 365 dies cada cop que s'executi.Crea el fitxer /usr/local/bin/renovar-postgres-ssl.sh:
```bash
#!/bin/bash
DIES=365
RUTA="/etc/postgresql/ssl"
IP_VM="192.168.56.102"
#Generar certificat i clau
openssl req -x509-nodes -days $DIES -newkey rsa:4096 \ -keyout $RUTA/server.key \ -out $RUTA/server.crt \ -subj "/CN=$IP_VM"
#Ajustar permisos
chown postgres:postgres $RUTA/server.key $RUTA/server.crt chmod 600 $RUTA/server.key chmod 644 $RUTA/server.crt
#Reiniciar servei
systemctl restart postgresql 
```
Important: Recorda donar permisos d'execució a l'script:
```bash
sudo chmod +x /usr/local/bin/renovar-postgres-ssl.sh 
```
3. Configuració de PostgreSQL Modifica el fitxer de configuració (per exemple, la versió 16) per activar el SSL:
```bash
sudo nano /etc/postgresql/16/main/postgresql.conf 
```
Busca i edita aquestes línies:
```text
ssl = on ssl_cert_file = '/etc/postgresql/ssl/server.crt' ssl_key_file = '/etc/postgresql/ssl/server.key' 
```
4. Automatització amb CRON Perquè s'executi automàticament el primer dia de cada any:
```bash
sudo crontab -e 
```
Afegeix la línia següent al final:
```text
0 0 1 1 * /usr/local/bin/renovar-postgres-ssl.sh >> /var/log/renovacio-ssl-postgres.log 2>&1 
```
5. Verificació Entra a la consola de PostgreSQL  i executa:
```sql
SHOW ssl; 
```
