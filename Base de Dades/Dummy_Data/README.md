# Generador de Dades de Prova - Hospital Santa Paciència

Aquest script en Python automatitza la generació i inserció massiva de dades fictícies per a la base de dades hospital_santa_paciencia en PostgreSQL. Utilitza la llibreria Faker configurada en espanyol per adaptar els formats de noms, adreces i DNIs.

---

## Requisits previs

Abans d'executar l'script, cal instal·lar les llibreries necessàries:


    pip install psycopg2-binary faker

## Configuració

Modifica les credencials de connexió directament al bloc DB_PARAMS dins de l'script si el teu servidor té uns paràmetres diferents:

    DB_PARAMS = {
    "host": "192.168.56.103",
    "database": "hospital_santa_paciencia",
    "user": "postgres",
    "password": "1234",
    "port": "5432"
    }
El script assumeix que l'esquema de la base de dades es diu hospital i hi accedeix automàticament mitjançant SET search_path TO hospital;.

## Volum de dades generat
L'script realitza una neteja inicial en cascada de les taules i insereix els següents registres de forma eficient en lots:

400 Treballadors (Metges, Infermeria i Personal Vari)

5 Plantes amb les seves corresponents habitacions i quiròfans

20 Aparells mèdics i un catàleg d'estoc de medicaments

50.000 Pacients

100.000 Visites mèdiques històriques amb diagnòstics

500 Operacions i 1.000 Reserves d'ingrés hospitalari

## Execució

Executa l'script des de la terminal amb el següent comandament:

    python dummy_data.py
