PROPOSTA DE SOLUCIÓ DEL PROJECTE

1. Objectius i Abast del Projecte

L'objectiu principal és informatitzar la gestió de l'hospital per substituir el sistema actual basat en paper. La solució se centrarà en:
* Gestió de dades: Manteniment de pacients, personal (mèdic, infermeria, administració) i visites.
* Seguretat i Confidencialitat: Protecció de dades sensibles i control d'accessos.
* Alta Disponibilitat: Garantir el funcionament 24x7 del sistema.
* Interoperabilitat: Exportació de dades en format XML per a la Seguretat Social.

2. Arquitectura del Sistema

D'acord amb la limitació de recursos i la preferència per tecnologies de baix cost de llicència, es proposa el següent:

* Servidor de Base de Dades (PostgreSQL): S'utilitzarà PostgreSQL per la seva robustesa i naturalesa de codi obert. Es configuraran dos nodes per garantir l'alta disponibilitat:
    * Configuració: Estructura Actiu-Actiu o Actiu-Passiu amb rèplica entre el centre de dades local i un lloc remot (cloud).
    * Còpies de seguretat: Scripts (Python o Bash) per a backups diaris amb emmagatzematge local de les darreres 5 còpies i una còpia diària al núvol.
* Aplicació (Python): Desenvolupada en Python, prioritzant una interfície de mode text o via navegador web per optimitzar recursos.
* Visualització: Ús de PowerBI per a la creació de quadres de comandament (visites, ràtio metge/pacient).

3. Disseny de la Base de Dades i Seguretat

* Model de Dades: El disseny inclourà entitats per a personal mèdic (amb estudis i especialitats), infermeria (assignats a metges o planta), pacients i visites.
* Suport Multi-idioma: Configuració per admetre caràcters cirílics.
* Seguretat de les Dades:
    * Assignació de permisos: Matriu de seguretat restrictiva basada en rols.
    * Xifratge: Connexions obligatòries mitjançant SSL.
    * Privacitat: Aplicació de Data Masking en dades personals d'alt nivell i registre de logs d'accés.
* Dades de Prova: Generació de 100.000 visites i 50.000 pacients mitjançant eines com `pgfaker` o llibreries de Python per validar el rendiment.

4. Funcionalitats de l'Aplicació

L'aplicació es dividirà en quatre mòduls principals.

* Mòdul d'Accés: Gestió de login amb credencials guardades de forma segura en fitxers separats i xifrats.
* Mòdul de Manteniment: Altes i modificacions de pacients, personal i programació de quiròfans.
* Mòdul de Consultes: Generació d'informes sobre ocupació per planta, personal en actiu i volum de visites.
* Mòdul d'Exportació: Transformació de dades de visites a format XML/JSON per a l'enviament a l'API de la Seguretat Social.

5. Metodologia de Desenvolupament

* Control de Versions: Ús de repositoris GitHub per al codi font i la documentació.
* Entorn de Treball: Ús d'entorns virtuals de Python i fitxers `requirements.txt` per assegurar la portabilitat.
* Documentació: Lliurament d'un manual d'instal·lació detallat i un manual d'usuari final.


Planificació Jira: https://sapalomera-team-ty16i4u.atlassian.net/?continue=https%3A%2F%2Fsapalomera-team-ty16i4u.atlassian.net%2Fwelcome%2Fsoftware%3FprojectId%3D10000&atlOrigin=eyJpIjoiNjljMjM5NGJiOTM1NGFlYmE5NDhkMTA2MDE2NzAzZDAiLCJwIjoiamlyYS1zb2Z0d2FyZSJ9

Diari de Sessions Alex: https://docs.google.com/spreadsheets/d/1wGJtMcrdDoTBQ4ITrkppQsXJUYFk2jB9/edit?usp=sharing&ouid=109898516658622937746&rtpof=true&sd=true
Diari de Sessions Josep: https://docs.google.com/spreadsheets/d/1XyuroRwlKfDCzt_e72mNTdLGLxWAIDvC/edit?gid=1097373687#gid=1097373687
