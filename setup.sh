#!/usr/bin/env bash

(
  set -o errexit
  set -o pipefail
  set -o nounset

  provisioning_dir="${PWD}"
  repo_source="ssh://git-codecommit.eu-west-1.amazonaws.com/v1/repos/tb_taste_purchase"
  repo_destination="${provisioning_dir}/Docker/app/source"

  echo "Installing application..."

  cp -p "${provisioning_dir}/.env.dist" "${provisioning_dir}/.env"

  echo "Edit the .env file with your variables"
  read -n 1 -s -r -p "Press any key to continue when you are finished"
  echo ""

  set -o allexport
  source .env
  set +o allexport

  echo "Cloning repository..."
  rm -rf "${repo_destination}"
  mkdir -p "${repo_destination}"
  cd "${repo_destination}"
  git clone "${repo_source}" "${repo_destination}"

  echo "Available branches: "
  git fetch origin
  git branch -a

  read -p "Enter the starting branch name: " branch_name
  git checkout "${branch_name}"

  export COMPOSE_FILE="${provisioning_dir}/docker-compose.yml"

  docker compose up --build --force-recreate -d
  docker compose exec web python manage.py migrate

  ping -c 3 "${HTTP_HOST}" || exit 1

  xdg-open "http://${HTTP_HOST}:${HTTP_PORT}"
)