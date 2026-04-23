    -- ============================================================
    -- CREACIÓ DE ROLS
    -- ============================================================

    CREATE ROLE dba;
    CREATE ROLE administracio;
    CREATE ROLE medic;
    CREATE ROLE infermeria;
    CREATE ROLE vari;
    CREATE ROLE zelador;

    -- ============================================================
    -- DBA
    -- ============================================================

    GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA hospital TO dba;
    GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA hospital TO dba;
    GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA hospital TO dba;

    -- ============================================================
    -- ADMINISTRACIO
    -- ============================================================

    GRANT SELECT, INSERT, UPDATE ON hospital.PACIENT   TO administracio;
    GRANT SELECT, INSERT, UPDATE ON hospital.RESERVA   TO administracio;
    GRANT SELECT, INSERT, UPDATE ON hospital.HABITACIO TO administracio;
    GRANT SELECT, INSERT, UPDATE ON hospital.PLANTA    TO administracio;
    GRANT SELECT ON hospital.TREBALLADOR TO administracio;

    -- ============================================================
    -- MEDIC
    -- ============================================================

    GRANT SELECT, INSERT, UPDATE ON hospital.VISITA   TO medic;
    GRANT SELECT, INSERT, UPDATE ON hospital.RECEPTE  TO medic;
    GRANT SELECT, INSERT, UPDATE ON hospital.OPERACIO TO medic;

    GRANT SELECT ON hospital.PACIENT    TO medic;
    GRANT SELECT ON hospital.MEDICAMENT TO medic;
    GRANT SELECT ON hospital.INFERMERIA TO medic;

    -- ============================================================
    -- INFERMERIA
    -- ============================================================

    GRANT SELECT, INSERT ON hospital.ASSISTEIX TO infermeria;

    GRANT SELECT ON hospital.OPERACIO   TO infermeria;
    GRANT SELECT ON hospital.VISITA     TO infermeria;
    GRANT SELECT ON hospital.PACIENT    TO infermeria;
    GRANT SELECT ON hospital.RESERVA    TO infermeria;
    GRANT SELECT ON hospital.MEDICAMENT TO infermeria;

    -- ============================================================
    -- VARI
    -- ============================================================

    GRANT SELECT, INSERT, UPDATE ON hospital.APARELL_MEDIC TO vari;
    GRANT SELECT, INSERT, UPDATE ON hospital.MEDICAMENT    TO vari;

    GRANT SELECT ON hospital.QUIROFAN TO vari;
    GRANT SELECT ON hospital.PLANTA   TO vari;

    -- ============================================================
    -- VISTA VARI
    -- ============================================================

    CREATE OR REPLACE VIEW hospital.v_pacient_vari AS
    SELECT 
    id_pacient,
    'XXXXX' || RIGHT(dni, 4) AS dni,
    '******' || RIGHT(telefon, 3) AS telefon,
    LEFT(email, 1) || '*******@' || SPLIT_PART(email, '@', 2) AS email,
    nom, 
    cognom
    FROM hospital.pacient;

    GRANT SELECT ON hospital.v_pacient_vari TO vari;

    -- ============================================================
    -- ZELADOR
    -- ============================================================

    GRANT SELECT ON hospital.RESERVA   TO zelador;
    GRANT SELECT ON hospital.HABITACIO TO zelador;
    GRANT SELECT ON hospital.OPERACIO      TO zelador;
    GRANT SELECT ON hospital.QUIROFAN      TO zelador;
    GRANT SELECT ON hospital.APARELL_MEDIC TO zelador;
    GRANT SELECT ON hospital.PLANTA TO zelador;

    -- ============================================================
    -- VISTA ZELADOR
    -- ============================================================

    CREATE OR REPLACE VIEW hospital.v_pacient_zelador AS
    SELECT 
    id_pacient,
    'XXXXX' || RIGHT(dni, 4) AS dni,
    '******' || RIGHT(telefon, 3) AS telefon,
    LEFT(email, 1) || '*******@' || SPLIT_PART(email, '@', 2) AS email,
    nom, 
    cognom
    FROM hospital.pacient;

    GRANT SELECT ON hospital.v_pacient_zelador TO zelador;

    -- ============================================================
    -- USUARIS
    -- ============================================================

    CREATE ROLE u_dba_exemple LOGIN PASSWORD 'Dba#Temp2024!';
    GRANT dba TO u_dba_exemple;

    CREATE ROLE u_administracio_exemple LOGIN PASSWORD 'Admin#Temp2024!';
    GRANT administracio TO u_administracio_exemple;

    CREATE ROLE u_medic_exemple LOGIN PASSWORD 'Medic#Temp2024!';
    GRANT medic TO u_medic_exemple;

    CREATE ROLE u_infermeria_exemple LOGIN PASSWORD 'Infer#Temp2024!';
    GRANT infermeria TO u_infermeria_exemple;

    CREATE ROLE u_vari_exemple LOGIN PASSWORD 'Vari#Temp2024!';
    GRANT vari TO u_vari_exemple;

    CREATE ROLE u_zelador_exemple LOGIN PASSWORD 'Zelad#Temp2024!';
    GRANT zelador TO u_zelador_exemple;

