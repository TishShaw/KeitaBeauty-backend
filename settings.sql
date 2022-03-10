-- settings.sql
CREATE DATABASE beauty;
-- DROP DATABASE beauty;
CREATE USER beautyuser WITH PASSWORD 'beauty';
-- DROP USER beautyuser;
GRANT ALL PRIVILEGES ON DATABASE beauty TO beautyuser;
