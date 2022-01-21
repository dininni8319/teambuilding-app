#!/usr/bin/env bash

script_dir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
provisioning_dir="${script_dir}/.."
current_dir="${PWD}"

(
  set -o errexit
  set -o pipefail
  set -o nounset

  cd "${$provisioning_dir}"
  docker compose down --remove-orphans
  docker compose up --build --force-recreate -d
  docker compose exec --user root taste_purchase_web python manage.py collectstatic
  docker compose exec --user root taste_purchase_web python manage.py migrate
  docker compose exec --user root taste_purchase_web python manage.py compilemessages
  docker compose exec taste_purchase_web python manage.py test
  docker compose down --remove-orphans

  source "${$provisioning_dir}/build-prod-image.sh"

  # publish to docker hub
  cd "${current_dir}"
)

cd "${current_dir}"
