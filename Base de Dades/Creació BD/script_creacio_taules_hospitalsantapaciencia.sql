CREATE SCHEMA IF NOT EXISTS hospital;

SET search_path TO hospital;

CREATE TABLE TREBALLADOR (
    id_empleat SERIAL PRIMARY KEY,
    dni VARCHAR(9) NOT NULL UNIQUE,
    nom VARCHAR(50), 
    cognom VARCHAR(100),
    telefon VARCHAR(15) NOT NULL,
    direccio VARCHAR(150)
);

CREATE TABLE MEDIC (
    id_empleat INT PRIMARY KEY,
    especialitat VARCHAR(50),
    estudi VARCHAR(100),
    cv TEXT,
    FOREIGN KEY (id_empleat) REFERENCES TREBALLADOR(id_empleat)
);

CREATE TABLE INFERMERIA (
    id_empleat INT PRIMARY KEY,
    experiencia VARCHAR(100),
    disponibilitat VARCHAR(50),
    FOREIGN KEY (id_empleat) REFERENCES TREBALLADOR(id_empleat)
);

CREATE TABLE VARI (
    id_empleat INT PRIMARY KEY,
    tipus_feina VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_empleat) REFERENCES TREBALLADOR(id_empleat)
);

CREATE TABLE PACIENT (
    id_pacient SERIAL PRIMARY KEY,
    dni VARCHAR(9) NOT NULL,
    nom VARCHAR(50),
    cognom VARCHAR(100),
    telefon VARCHAR(15) NOT NULL
);

CREATE TABLE PLANTA (
    id_planta SERIAL PRIMARY KEY,
    numero INT,
    tipus VARCHAR(50)
);

CREATE TABLE HABITACIO (
    id_habitacio SERIAL PRIMARY KEY,
    numero INT,
    capacitat INT,
    id_planta INT,
    FOREIGN KEY (id_planta) REFERENCES PLANTA(id_planta)
);

CREATE TABLE QUIROFAN (
    id_quirofan SERIAL PRIMARY KEY,
    tipus VARCHAR(50),
    id_planta INT,
    FOREIGN KEY (id_planta) REFERENCES PLANTA(id_planta)
);

CREATE TABLE RESERVA (
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

CREATE TABLE VISITA (
    id_visita SERIAL PRIMARY KEY,
    dia DATE,
    hora TIME,
    diagnostic TEXT,
    id_pacient INT,
    id_medic INT,
    FOREIGN KEY (id_pacient) REFERENCES PACIENT(id_pacient),
    FOREIGN KEY (id_medic) REFERENCES MEDIC(id_empleat)
);

CREATE TABLE OPERACIO (
    id_operacio SERIAL PRIMARY KEY,
    tipus VARCHAR(50),
    id_quirofan INT,
    id_pacient INT,
    id_medic INT,
    FOREIGN KEY (id_quirofan) REFERENCES QUIROFAN(id_quirofan),
    FOREIGN KEY (id_pacient) REFERENCES PACIENT(id_pacient),
    FOREIGN KEY (id_medic) REFERENCES MEDIC(id_empleat)
);

CREATE TABLE MEDICAMENT (
    id_medicament SERIAL PRIMARY KEY,
    nom VARCHAR(100),
    stock INT
);

CREATE TABLE RECEPTE (
    id_medicament INT,
    id_visita INT,
    PRIMARY KEY (id_medicament, id_visita),
    FOREIGN KEY (id_medicament) REFERENCES MEDICAMENT(id_medicament),
    FOREIGN KEY (id_visita) REFERENCES VISITA(id_visita)
);

CREATE TABLE ASSISTEIX (
    id_empleat INT,
    id_operacio INT,
    PRIMARY KEY (id_empleat, id_operacio),
    FOREIGN KEY (id_empleat) REFERENCES INFERMERIA(id_empleat),
    FOREIGN KEY (id_operacio) REFERENCES OPERACIO(id_operacio)
);

CREATE TABLE ASSIGNA (
    id_empleat INT,
    id_planta INT,
    PRIMARY KEY (id_empleat, id_planta),
    FOREIGN KEY (id_empleat) REFERENCES INFERMERIA(id_empleat),
    FOREIGN KEY (id_planta) REFERENCES PLANTA(id_planta)
);
