sudo openssl req -x509 -nodes -days 365 -newkey rsa:4096 \
  -keyout /etc/postgresql/ssl/server.key \
  -out /etc/postgresql/ssl/server.crt \
  -subj "/CN=192.168.56.102"

# Donem la propietat a l'usuari de la base de dades
sudo chown postgres:postgres /etc/postgresql/ssl/server.key /etc/postgresql/ssl/server.crt

# Només l'usuari postgres pot llegir la clau privada
sudo chmod 600 /etc/postgresql/ssl/server.key

# El certificat pot ser llegit per tothom
sudo chmod 644 /etc/postgresql/ssl/server.crt

sudo nano /etc/postgresql/16/main/postgresql.conf
ssl = on
ssl_cert_file = '/etc/postgresql/ssl/server.crt'
ssl_key_file = '/etc/postgresql/ssl/server.key'

sudo systemctl restart postgresql

sudo -u postgres psql
SQL
SHOW ssl;
