BANCO_DE_DADOs='agenda'
USUARIO='usuario_estudo'
SENHA='212223'


sudo -u postgres psql -c "CREATE DATABASE $BANCO_DE_DADOS;"
sudo -u postgres psql -c "CREATE USER $USUARIO WITH PASSWORD '$SENHA';"
sudo -u postgres psql -c "ALTER ROLE $USUARIO SET client_encoding TO 'utf8';"
sudo -u postgres psql -c "ALTER ROLE $USUARIO SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql -c "ALTER ROLE $USUARIO SET timezone TO 'America/Sao_Paulo';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE $BANCO_DE_DADOS TO $USUARIO;"