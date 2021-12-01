#bin/sh
echo 'Installing application...'

cp .env.dist .env
docker compose up --build
