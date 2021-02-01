CREATE DATABASE myblogdbname;
CREATE USER myblog_adminuser WITH PASSWORD 'YfQ%7uG4yIDCiH@k!7v5Vf65mv8Pc!vjByPrgFCE@tLEe5Ebq%';
ALTER ROLE myblog_adminuser SET client_encoding TO 'utf8';
ALTER ROLE myblog_adminuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myblog_adminuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE myblogdbname TO myblog_adminuser;
