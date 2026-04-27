-- ============================================================
-- NETEJA PRÈVIA (opcional, per re-execució segura)
-- ============================================================

-- Eliminar usuaris si existeixen
DROP ROLE IF EXISTS u_dba_exemple;
DROP ROLE IF EXISTS u_administracio_exemple;
DROP ROLE IF EXISTS u_medic_exemple;
DROP ROLE IF EXISTS u_infermeria_exemple;
DROP ROLE IF EXISTS u_vari_exemple;
DROP ROLE IF EXISTS u_zelador_exemple;

-- Eliminar rols si existeixen
DROP ROLE IF EXISTS dba;
DROP ROLE IF EXISTS administracio;
DROP ROLE IF EXISTS medic;
DROP ROLE IF EXISTS infermeria;
DROP ROLE IF EXISTS vari;
DROP ROLE IF EXISTS zelador;
