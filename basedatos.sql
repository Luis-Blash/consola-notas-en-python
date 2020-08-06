CREATE DATABASE IF NOT EXISTS master_python;
USE master_python;

CREATE TABLE usuarios(
    id INT(25) auto_increment NOT NULL,
    nombre VARCHAR(100),
    apellidos VARCHAR(255),
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    fecha DATE NOT NULL,
    -- llave primaria id
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    -- restriccion es un  campo unico no pueden tener dos el mismo email
    CONSTRAINT uq_email UNIQUE(email)
    -- Engine que va a manetener la identendad referencial
)ENGINE=InnoDb;

CREATE TABLE notas(
    id INT(25) auto_increment NOT NULL,
    usuario_id INT(25) NOT NULL,
    titulo VARCHAR(25) NOT NULL,
    descripcion MEDIUMTEXT,
    fecha DATE NOT NULL,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    -- su forey key
    CONSTRAINT fk_notas_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;