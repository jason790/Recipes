CREATE DATABASE recipes;

CREATE USER user WITH LOGIN;
CREATE ROLE user WITH LOGIN;
ALTER DATABASE recipes OWNER TO user;
GRANT ALL ON DATABASE recipes to user;
