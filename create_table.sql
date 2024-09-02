-- create_table.sql
DROP TABLE IF EXISTS characters;
CREATE TABLE characters (
    id SERIAL PRIMARY KEY,
    birth_year VARCHAR(20),
    eye_color VARCHAR(16),
    films TEXT,
    gender VARCHAR(20),
    hair_color VARCHAR(20),
    height INTEGER,
    homeworld VARCHAR(100),
    mass INTEGER,
    name VARCHAR(100),
    skin_color VARCHAR(20),
    species TEXT,
    starships TEXT,
    vehicles TEXT
);
