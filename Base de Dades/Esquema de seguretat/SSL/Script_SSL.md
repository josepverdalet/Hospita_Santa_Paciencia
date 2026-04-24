```
sudo openssl req -x509 -nodes -days 365 -newkey rsa:4096 \
  -keyout /etc/postgresql/ssl/server.key \
  -out /etc/postgresql/ssl/server.crt \
  -subj "/CN=192.168.56.102"
```

```
sudo nano /etc/postgresql/16/main/postgresql.conf
```

```
ssl = on
ssl_cert_file = '/etc/postgresql/ssl/server.crt'
ssl_key_file = '/etc/postgresql/ssl/server.key'
```

```
sudo systemctl restart postgresql
```

```
sudo -u postgres psql
SQL
SHOW ssl;
```

```
sudo mkdir -p /etc/postgresql/ssl
sudo chown postgres:postgres /etc/postgresql/ssl
sudo chmod 700 /etc/postgresql/ssl
```

```
sudo nano /usr/local/bin/renovar-postgres-ssl.sh
```

```
#!/bin/bash
DIES=365
RUTA="/etc/postgresql/ssl"
IP_VM="192.168.56.102"
openssl req -x509 -nodes -days $DIES -newkey rsa:4096 \
  -keyout $RUTA/server.key \
  -out $RUTA/server.crt \
  -subj "/CN=$IP_VM"
chown postgres:postgres $RUTA/server.key $RUTA/server.crt
chmod 600 $RUTA/server.key
chmod 644 $RUTA/server.crt
sudo systemctl restart postgresql
```

```
sudo nano /etc/postgresql/16/main/postgresql.conf
```

```
ssl = on
ssl_cert_file = '/etc/postgresql/ssl/server.crt'
ssl_key_file = '/etc/postgresql/ssl/server.key'
```

```
sudo systemctl restart postgresql
```

```
sudo crontab -e
```

```
0 0 1 1 * /usr/local/bin/renovar-postgres-ssl.sh >> /var/log/renovacio-ssl-postgres.log 2>&1
```
