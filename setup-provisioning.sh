#!/usr/bin/env bash

app_name="app"
provisioning_dir="${PWD}"
source_dir="${provisioning_dir}/Docker/${app_name}/source"
repo_source="git@github.com:Multidialogo/teambuilding-app.git"

(
  set -o errexit
  set -o pipefail
  set -o nounset

  echo "Installing application..."

  if [ ! -f "${provisioning_dir}/.env" ]
  then
    read -n 1 -s -r -p "File .env does not exist. Do you want to copy it from .env.dist? (y/n)" response_copy
    echo ""
    if [[ "${response_copy}" == "y" || "${response_copy}" == "Y" ]]
    then
      cp -p "${provisioning_dir}/.env.dist" "${provisioning_dir}/.env"
    fi
  fi

  echo "Please, check variables in the .env file."
  read -n 1 -s -r -p "Press any key to continue when you are sure every variable is correct."
  echo ""

  set -o allexport
  source .env
  set +o allexport

  if [ -d "${source_dir}" ]; then
    rm -rf "${source_dir}"
  fi

  mkdir -p "${source_dir}"

  cd "${source_dir}"
  git clone "${repo_source}" .
  git switch develop

  cd "${provisioning_dir}"

  source ./scripts/build-dev-image.sh

  docker compose up --build --force-recreate -d
  docker compose exec --user root taste_purchase_web python manage.py collectstatic
  docker compose exec --user root  taste_purchase_web python manage.py migrate
  docker compose exec --user root  taste_purchase_web python manage.py compilemessages
  docker compose exec taste_purchase_web python manage.py test

  ping -c 3 "${HTTP_HOST}" || exit 1

  xdg-open "http://${HTTP_HOST}:${HTTP_PORT}"
)
