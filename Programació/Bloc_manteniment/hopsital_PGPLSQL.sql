SET search_path TO hospital;

CREATE OR REPLACE PROCEDURE alta_treballador_hospital(
    p_dni VARCHAR, 
    p_nom VARCHAR, 
    p_cognom VARCHAR, 
    p_telf VARCHAR, 
    p_dir VARCHAR, 
    p_tipus VARCHAR, 
    p_extra VARCHAR
) AS $$
DECLARE
    v_id INT;
BEGIN
    INSERT INTO "TREBALLADOR" (dni, nom, cognom, telefon, direccio)
    VALUES (p_dni, p_nom, p_cognom, p_telf, p_dir) 
    RETURNING id_empleat INTO v_id;

    IF p_tipus = 'MEDIC' THEN
        INSERT INTO "MEDIC" (id_empleat, especialitat) VALUES (v_id, p_extra);
    ELSIF p_tipus = 'INFERMERIA' THEN
        INSERT INTO "INFERMERIA" (id_empleat, experiencia) VALUES (v_id, p_extra);
    ELSE
        INSERT INTO "VARI" (id_empleat, tipus_feina) VALUES (v_id, p_extra);
    END IF;
END;
$$ LANGUAGE plpgsql;
