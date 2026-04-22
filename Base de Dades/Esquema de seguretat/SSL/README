```
cd /etc/postgresql/15/main
```


```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:4096 \
  -keyout /etc/postgresql/ssl/server.key \
  -out /etc/postgresql/ssl/server.crt \
  -subj "/CN=192.168.56.102"
```


```
sudo mkdir -p /etc/postgresql/ssl
```

```
sudo chown postgres:postgres /etc/postgresql/ssl
```

```
sudo chmod 700 /etc/postgresql/ssl
```

```
sudo nano /usr/local/bin/renovar-postgres-ssl.sh
```

