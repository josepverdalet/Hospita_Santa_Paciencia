# Esquema d'Alta Disponibilitat (Hospital Santa Paciencia)

## Objectiu del Disseny
Assegurar la continuïtat assistencial de l'hospital 24x7, evitant qualsevol interrupció en l'accés a l'historial clínic o la gestió de visites. Es proposa una arquitectura de dos nodes en replicació física per suportar una càrrega de més de 100.000 visites i garantir la seguretat de les dades confidencials segons l'AGPD.

---

## 1. Node Actiu (Servidor de Producció - Hospital)
Aquest servidor estarà físicament al datacenter de l'hospital per minimitzar la latència en les consultes de metges i infermeres.

| Component | Detalls Tècnics | Preu Estimat |
| :--- | :--- | :--- |
| **CPU** | AMD EPYC 7232P (8 Cores / 16 Threads) | 480 € |
| **Memòria RAM** | 128 GB DDR4 ECC | 350 € |
| **Emmagatzematge** | 2x 1.92TB NVMe Enterprise | 650 € |
| **Connexió** | 1Gbps fibra | 45€/mes |
| **Sistema Operatiu** | Ubuntu Server 24.04 LTS | 0 € |
| **Base de Dades** | PostgreSQL 16 amb suport UTF-8 (Ciríl·lic) | 0 € |

### Justificació Tècnica:
* **Memòria Elevada:** Es trien 128 GB de RAM per permetre que tota la base de dades activa i els seus índexs (especialment els de caràcters ciríl·lics) resideixin en memòria cache, accelerant les consultes.
* **Volum de Dades:** Dissenyat per processar sense retards les 50.000 fitxes de pacients i els accessos simultanis dels 450 empleats del centre.

---

## 2. Node Passiu (Hot Standby - Cloud/Remot)
Ubicat fora de l'hospital per actuar com a node de recuperació davant desastres físics (incendis, inundacions o talls elèctrics prolongats).

| Component | Detalls Tècnics | Preu Estimat |
| :--- | :--- | :--- |
| **CPU** | Instància Cloud Equivalent (8 vCPUs) | 45 €/mes |
| **Memòria RAM** | 64 GB RAM | Inclòs |
| **Emmagatzematge** | 2 TB SSD Provisioned IOPS | Inclòs |
| **Connexió** | Enllaç xifrat via SSL/TLS obligatori | 0 € |
| **Estat** | Hot Standby (Llegible per a informes) | 0 € |

### Justificació Tècnica:
* **Replicació Asíncrona:** El node cloud rep els canvis en temps real des del node principal.
* **Reporting:** Tot i ser un node passiu per a escriptures, es pot utilitzar per generar els informes XML massius per a la Seguretat Social sense carregar el servidor principal.
* **SSL:** Tota la replicació es fa sota túnels SSL per complir amb el nivell alt de seguretat demanat.

---

## 3. Estratègia de Còpies de Seguretat (Backup & Recovery)
L'alta disponibilitat no substitueix les còpies de seguretat. Seguim la regla de l'enunciat:

1.  **Script de Backup (Python/Bash):** Un procés automatitzat realitzarà un `pg_dump` diari a les 03:00 AM.
2.  **Rotació Local:** Es mantenen les 5 darreres còpies al disc local del servidor.
3.  **Còpia Cloud:** Diàriament s'enviarà una còpia xifrada a un repositori extern (ex. S3 o Google Drive) per garantir la recuperació externa.
4.  **Data Masking:** Les còpies de seguretat destinades a entorns de proves (Dummy Data) s'executaran amb l'esquema de Data Masking ja aplicat per protegir la privacitat.

---

**Cost Total de Hardware Base:** ~1.600 €
