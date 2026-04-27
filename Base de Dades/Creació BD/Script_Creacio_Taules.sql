CREATE SCHEMA IF NOT EXISTS hospital;

SET search_path TO hospital;

CREATE TABLE IF NOT EXISTS TREBALLADOR (
id_empleat SERIAL PRIMARY KEY,
dni VARCHAR(9) NOT NULL UNIQUE,
nom VARCHAR(50), 
cognom VARCHAR(100),
telefon VARCHAR(15) NOT NULL,
direccio VARCHAR(150)
);

CREATE TABLE IF NOT EXISTS MEDIC (
id_empleat INT PRIMARY KEY,
especialitat VARCHAR(50),
estudi VARCHAR(100),
cv TEXT,
FOREIGN KEY (id_empleat) REFERENCES TREBALLADOR(id_empleat)
);

CREATE TABLE IF NOT EXISTS INFERMERIA (
id_empleat INT PRIMARY KEY,
experiencia VARCHAR(100),
disponibilitat VARCHAR(50),
FOREIGN KEY (id_empleat) REFERENCES TREBALLADOR(id_empleat)
);

CREATE TABLE IF NOT EXISTS VARI (
id_empleat INT PRIMARY KEY,
tipus_feina VARCHAR(50) NOT NULL,
FOREIGN KEY (id_empleat) REFERENCES TREBALLADOR(id_empleat)
);

CREATE TABLE IF NOT EXISTS PACIENT (
id_pacient SERIAL PRIMARY KEY,
dni VARCHAR(9) NOT NULL,
nom VARCHAR(50),
cognom VARCHAR(100),
email VARCHAR(50),
telefon VARCHAR(15) NOT NULL
);

CREATE TABLE IF NOT EXISTS PLANTA (
id_planta SERIAL PRIMARY KEY,
numero INT,
tipus VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS HABITACIO (
id_habitacio SERIAL PRIMARY KEY,
numero INT,
capacitat INT,
id_planta INT,
FOREIGN KEY (id_planta) REFERENCES PLANTA(id_planta)
);

CREATE TABLE IF NOT EXISTS QUIROFAN (
id_quirofan SERIAL PRIMARY KEY,
tipus VARCHAR(50),
id_planta INT,
FOREIGN KEY (id_planta) REFERENCES PLANTA(id_planta)
);

CREATE TABLE IF NOT EXISTS aparell_medic (
id_serie SERIAL PRIMARY KEY,
tipus VARCHAR(50),
quantitat INT,
id_quirofan INT,
FOREIGN KEY (id_quirofan) REFERENCES QUIROFAN(id_quirofan)
);

CREATE TABLE IF NOT EXISTS RESERVA (
id_reserva SERIAL PRIMARY KEY,
dia_ingres DATE,
hora_ingres TIME,
dia_sortida DATE,
hora_sortida TIME,
motiu TEXT,
id_habitacio INT,
id_pacient INT,
id_quirofan INT,
id_medic INT,
FOREIGN KEY (id_quirofan) REFERENCES QUIROFAN(id_quirofan),
FOREIGN KEY (id_medic) REFERENCES MEDIC(id_empleat),
FOREIGN KEY (id_habitacio) REFERENCES HABITACIO(id_habitacio),
FOREIGN KEY (id_pacient) REFERENCES PACIENT(id_pacient)
);

CREATE TABLE IF NOT EXISTS VISITA (
id_visita SERIAL PRIMARY KEY,
dia DATE,
hora TIME,
diagnostic TEXT,
id_pacient INT,
id_medic INT,
FOREIGN KEY (id_pacient) REFERENCES PACIENT(id_pacient),
FOREIGN KEY (id_medic) REFERENCES MEDIC(id_empleat)
);

CREATE TABLE IF NOT EXISTS OPERACIO (
id_operacio SERIAL PRIMARY KEY,
tipus VARCHAR(50),
id_quirofan INT,
id_pacient INT,
id_medic INT,
FOREIGN KEY (id_quirofan) REFERENCES QUIROFAN(id_quirofan),
FOREIGN KEY (id_pacient) REFERENCES PACIENT(id_pacient),
FOREIGN KEY (id_medic) REFERENCES MEDIC(id_empleat)
);

CREATE TABLE IF NOT EXISTS MEDICAMENT (
id_medicament SERIAL PRIMARY KEY,
nom VARCHAR(100),
stock INT
);

CREATE TABLE IF NOT EXISTS RECEPTE (
id_medicament INT,
id_visita INT,
PRIMARY KEY (id_medicament, id_visita),
FOREIGN KEY (id_medicament) REFERENCES MEDICAMENT(id_medicament),
FOREIGN KEY (id_visita) REFERENCES VISITA(id_visita)
);

CREATE TABLE IF NOT EXISTS ASSISTEIX (
id_empleat INT,
id_operacio INT,
PRIMARY KEY (id_empleat, id_operacio),
FOREIGN KEY (id_empleat) REFERENCES INFERMERIA(id_empleat),
FOREIGN KEY (id_operacio) REFERENCES OPERACIO(id_operacio)
);

CREATE TABLE IF NOT EXISTS ASSIGNA (
id_empleat INT,
id_planta INT,
PRIMARY KEY (id_empleat, id_planta),
FOREIGN KEY (id_empleat) REFERENCES INFERMERIA(id_empleat),
FOREIGN KEY (id_planta) REFERENCES PLANTA(id_planta)
);
