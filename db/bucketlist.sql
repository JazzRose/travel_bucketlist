DROP TABLE IF EXISTS trips;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS locations;
DROP TABLE IF EXISTS cities;

CREATE TABLE users ( 
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    age INT,
    interests TEXT

);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    info TEXT
);

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    city_id INT REFERENCES cities(id),
    type VARCHAR(255),
    visited BOOLEAN
);

CREATE TABLE trips (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    location_id INT REFERENCES locations(id) ON DELETE CASCADE,
    review TEXT,
    rating INT,
    date VARCHAR(255)
);