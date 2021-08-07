DROP DATABASE IF EXISTS cobify;
CREATE DATABASE cobify;
USE cobify;

CREATE TABLE gas_types (
gas_type_id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
gas_name VARCHAR(10) NOT NULL
);

CREATE TABLE consumes (
consume_id INT PRIMARY KEY,
distance FLOAT NOT NULL,
consume FLOAT NULL,
speed FLOAT NOT NULL,
temp_inside FLOAT NOT NULL,
temp_outside INT NOT NULL,
gas_type_id INT NOT NULL,
AC INT NOT NULL,
rain INT NOT NULL,
sun INT NOT NULL,
snow INT NOT NULL,
FOREIGN KEY (gas_type_id) REFERENCES gas_types (gas_type_id) ON DELETE CASCADE
);

CREATE TABLE refills (
route_id INT PRIMARY KEY,
refill_liters FLOAT NOT NULL,
refill_gas INT,
FOREIGN KEY (refill_gas) REFERENCES gas_types (gas_type_id) ON DELETE CASCADE
);

INSERT INTO gas_types VALUES
(1, 'SP98'),
(2, 'E10');

