Característiques Principals

Gestió i Manteniment : Alta i baixa de personal mèdic/infermeria i pacients, així com l'assignació de recursos.

Consultes i Informes: Visualització de dades clau com l'ocupació de plantes, operacions diàries i històrics de visites.

Estructura dels Fitxers (Explicació de com ho he muntat)
He dividit el codi en 4 scripts per tenir-ho tot ben organitzat i modular, que si no el profe es queixa:

1. main.py
És el fitxer principal. Desaixeca la primera finestra de Login on l'usuari posa el seu nom i contrasenya. Si tot és correcte i hi ha connexió amb la base de dades, amaga aquesta finestra (root.withdraw()) i obre el menú de manteniment. També té l'opció de registrar usuaris nous.

2. seguretat.py
Aquí m'he assegurat que ningú pugui xafardejar les contrasenyes:

Utilitzo Fernet (cryptography) per generar una clau simètrica (secret.key) i xifrar el fitxer on es guarden els usuaris (access.dat).

Per si de cas, les contrasenyes no es guarden en text pla; els hi faig un hash amb bcrypt abans de desar-les al JSON xifrat.

3. database.py
Aquest script gestiona la connexio cap a la base de dades utilitzant psycopg2.

He posat l'opció sslmode="require" per seguretat, ja que la npstra base de dades te un certificat ssl.

Al connectar-se, força el search_path cap a l'esquema hospital per no haver de posar-ho a cada línia de codi.

4. gui_manteniment.py (La xixa de la interfície)
Un cop passes el login, s'obre aquesta finestra plena de botons. Està partida en dues seccions:

Manteniment: Fa altes de personal (crida la funció hospital.alta_treballador_hospital de PostgreSQL amb un SELECT per agafar l'ID del SERIAL). També fa altes de pacients, consultes de quina planta té un infermer, operacions del dia i eliminacions.

Consultes i Informes: Fa llistats de la base de dades com el recompte de recursos d'una planta (COUNT), l'informe general de rols amb un CASE WHEN (per saber si són Metges, Infermers o Vari) i les visites totals.
