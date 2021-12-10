#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

cp -p "${provisioning_dir}/.env.dist" "${provisioning_dir}/.env"
set -o allexport; source .env; set +o allexport

echo "Installing application..."

provisioning_dir=${PWD}

echo "Do you want to pull code from a custom repo?"
read -n 1 -s -r -p "(Y/N): " confirm_custom_repo
echo ""
if [[ $confirm_custom_repo == [yY] ]]
then
  read -p "Enter a custom location: " repo_location
else
  repo_location="ssh://git-codecommit.eu-west-1.amazonaws.com/v1/repos/tb_taste_purchase"
fi

rm -rf Docker/app/source
mkdir -p Docker/app/source
cd Docker/app/source
git clone $repo_location .

echo "Available branches: "
git branch -a

read -p "Enter the starting branch name: " branch_name
git checkout $branch_name

echo "Edit the .env file with your variables"
read -n 1 -s -r -p "Press any key to continue when you are finished"
echo ""

export COMPOSE_FILE="${provisioning_dir}/docker-compose.yml"

docker compose up --build -d
docker compose exec web python manage.py migrate

ping "${HTTP_HOST}":"${HTTP_PORT}"

xdg-open "http://${HTTP_HOST}:${HTTP_PORT}"
