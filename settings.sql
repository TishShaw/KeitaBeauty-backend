-- settings.sql
CREATE DATABASE shop;

CREATE USER shopuser WITH PASSWORD 'shop';
GRANT ALL PRIVILEGES ON DATABASE shop TO shopuser;
