CREATE DATABASE IF NOT EXISTS test_db;
USE test_db;

CREATE TABLE empleados (
    id INT PRIMARY KEY,
    nombre VARCHAR(100),
    salario DECIMAL(10,2)
);

INSERT INTO empleados (id, nombre, salario) VALUES 
(1, 'Ana', 3000), 
(2, 'Luis', 2500), 
(3, 'Carlos', 3200);

