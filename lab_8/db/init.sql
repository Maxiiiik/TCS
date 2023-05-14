-- CREATE EXTENSION hstore;
-- CREATE EXTENSION postgis;

CREATE TABLE features (
    id integer not null,
    name varchar(40),
    geometry geometry(geometry, 4326)
);