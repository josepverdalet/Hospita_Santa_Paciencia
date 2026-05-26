# Definició de Rols i Permisos del Sistema Hospitalari

Aquest document detalla la matriu de permisos i responsabilitats per a cada perfil d'usuari dins de la base de dades de l'hospital.


## 1. Administrador de Sistemes (DBA)
* **Permisos:** Control total (`ALL PRIVILEGES`) sobre totes les taules.
* **Responsabilitat:** Manteniment de l'estructura, gestió d'usuaris, seguretat i còpies de seguretat.

## 2. Personal Mèdic (MEDIC)
Enfocat en la part clínica, diagnòstica i tractament dels pacients.

* **Lectura i Escriptura (`SELECT`, `INSERT`, `UPDATE`):**
    * `VISITA`: Registrar diagnòstics i observacions.
    * `RECEPTA`: Prescriure medicaments.
    * `OPERACIO`: Planificar i documentar intervencions.
* **Lectura (`SELECT`):**
    * `PACIENT`: Historial i dades de contacte.
    * `MEDICAMENT`: Consultar stock disponible.
    * `INFERMERIA`: Consultar disponibilitat d'assistents.

## 3. Personal d'Infermeria (INFERMERIA)
Suport operatiu i cura directa del pacient.

* **Lectura i Escriptura (`SELECT`, `INSERT`):**
    * `ASSISTEIX`: Registrar la seva participació en operacions.
* **Lectura (`SELECT`):**
    * `OPERACIO` i `VISITA`: Consultar l'agenda d'intervencions.
    * `PACIENT` i `RESERVA`: Localització dels pacients assignats.
    * `MEDICAMENT`: Verificar la medicació a subministrar.

## 4. Gestió de Logística i Manteniment (VARI)
Responsables de l'equipament, instal·lacions i subministraments.

* **Lectura i Escriptura (`SELECT`, `INSERT`, `UPDATE`):**
    * `APARELL_MEDIC`: Control d'inventari i ubicació.
    * `MEDICAMENT`: Gestió de l'estoc general.
* **Lectura (`SELECT`):**
    * `QUIROFAN` i `PLANTA`: Localització d'equips.

## 5. Zelador
Responsable del trasllat de pacients i materials.

###  Tasques i Accessos
1.  **Gestió de Pacients i Trasllats:**
    * `SELECT` sobre `PACIENT` (Identificació), `RESERVA` (Habitació i dates) i `HABITACIO` (Localització).
2.  **Logística d'Intervencions:**
    * `SELECT` sobre `OPERACIO` (Horaris), `QUIROFAN` (Destí) i `APARELL_MEDIC` (Moure equips).
3.  **Infraestructura:**
    * `SELECT` sobre `PLANTA` per a orientació.

###  Restriccions de Seguretat
Per complir amb la protecció de dades (LOPD), es denega l'accés a:
* `VISITA (diagnostic)`: No poden conèixer patologies detallades.
* `RECEPTA` / `MEDICAMENT`: Sense competència en medicació.
* Dades de contacte privades (telèfon, adreça), excepte identificació bàsica.


###  Restriccions Crítiques
Accés molt limitat per privadesa clínica:
* **Sense accés** a la taula `VISITA` (Diagnòstics).
* **Sense accés** a la taula `OPERACIO` (Detalls quirúrgics).
* **Sense accés** a `MEDICAMENT` ni `RECEPTA`.
