#!/usr/bin/env bash

script_dir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
app_name="app"
provisioning_dir="${script_dir}/.."
source_dir="${provisioning_dir}/Docker/${app_name}/source"
dockerfile="${provisioning_dir}/Docker/${app_name}/Dockerfile"
current_dir="${PWD}"
temp_pass_file="${HOME}/.docker/temp.txt"

(
  set -o errexit
  set -o pipefail
  set -o nounset

  stty -echo
  echo "Enter your Docker Hub password: "
  read -s docker_hub_password
  echo "${docker_hub_password}" | docker login --username "netbuilderita" --password-stdin
  docker_hub_password=""
  stty echo

  docker compose down --remove-orphans
  docker compose up --build --force-recreate -d
  docker compose exec --env DEBUG=False taste_purchase_web python manage.py test
  docker compose down --remove-orphans

  cd "${source_dir}"
  tag=$(git describe --exact-match --tags $(git log -n1 --pretty='%h'))
  cd "${current_dir}"

  docker build -f "${dockerfile}" \
    -t "netbuilderita/teambuilding-app" \
    -t "netbuilderita/teambuilding-app:${tag}" \
    --target prod \
    .

    read -n 1 -s -r -p "Do you want to publish this image to Docker Hub? (y/n)" response_publish
    echo ""
    if [[ "${response_publish}" == "y" || "${response_publish}" == "Y" ]]
    then
      docker push "netbuilderita/teambuilding-app"
      docker push "netbuilderita/teambuilding-app:${tag}"
    fi

  docker logout

  cd "${current_dir}"
)

docker_hub_password=""
docker logout
cd "${current_dir}"
