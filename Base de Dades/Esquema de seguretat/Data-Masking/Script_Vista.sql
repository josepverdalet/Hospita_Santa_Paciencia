--VISTA VARI

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

--VISTA ZELADOR

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
