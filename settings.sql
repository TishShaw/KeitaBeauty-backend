-- settings.sql
CREATE DATABASE shop;
DROP DATABASE shop;
CREATE USER shopuser WITH PASSWORD 'shop';
DROP USER shopuser;
GRANT ALL PRIVILEGES ON DATABASE shop TO shopuser;
