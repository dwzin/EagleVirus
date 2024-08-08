CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    ip VARCHAR,
    port INTEGER,
    geolocation VARCHAR,
    country VARCHAR,
    city VARCHAR,
    region VARCHAR,
    postal VARCHAR,
    timezone VARCHAR
);