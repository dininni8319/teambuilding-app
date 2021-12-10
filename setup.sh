#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

repo_source="ssh://git-codecommit.eu-west-1.amazonaws.com/v1/repos/tb_taste_purchase"
repo_destination="${repo_destination}"
provisioning_dir="${PWD}"

echo "Installing application..."

cp -p "${provisioning_dir}/.env.dist" "${provisioning_dir}/.env"

echo "Edit the .env file with your variables"
read -n 1 -s -r -p "Press any key to continue when you are finished"
echo ""

set -o allexport; source .env; set +o allexport

echo "Do you want to pull code from a custom repo?"
read -n 1 -s -r -p "(Y/N): " confirm_custom_repo

echo "Cloning repository..."
rm -rf "${repo_destination}"
mkdir -p "${repo_destination}"
cd "${repo_destination}"
git clone "${repo_source}" .

echo "Available branches: "
git branch -a

read -p "Enter the starting branch name: " branch_name
git checkout "${branch_name}"

export COMPOSE_FILE="${provisioning_dir}/docker-compose.yml"

docker compose up --build --force-recreate -d
docker compose exec web python manage.py migrate

ping "${HTTP_HOST}":"${HTTP_PORT}"

xdg-open "http://${HTTP_HOST}:${HTTP_PORT}"
