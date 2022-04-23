DROP TABLE IF EXISTS trips;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS locations;

CREATE TABLE users ( 
    id SERIAL PRIMARY KEY,
    username VARCHAR(255),
    age INT,
    interests TEXT

);
CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    info TEXT,
    visited BOOLEAN
);

CREATE TABLE cities (
    id SERIAL PRIMARY KEY,
    name VARCHAR (255),
    location_id INT REFERENCES locations(id),
    info TEXT
);


CREATE TABLE trips (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    city_id INT REFERENCES cities(id) ON DELETE CASCADE,
    review TEXT,
    rating INT,
    date VARCHAR(255)
)