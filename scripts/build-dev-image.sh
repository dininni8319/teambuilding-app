#!/usr/bin/env bash

script_dir=$( cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd )
app_name="app"
provisioning_dir="${script_dir}/.."
dockerfile="${provisioning_dir}/Docker/${app_name}/Dockerfile"
source_dir="${provisioning_dir}/Docker/${app_name}/source"
current_dir="${PWD}"

(
  set -o errexit
  set -o pipefail
  set -o nounset

  cd "${source_dir}"
  tag=$(git describe --exact-match --tags $(git log -n1 --pretty='%h'))
  cd "${current_dir}"

  docker build -f "${dockerfile}" \
    -t "netbuilderita/teambuilding-app-dev" \
    -t "netbuilderita/teambuilding-app-dev:${tag}" \
    --target dev \
    .
)

cd "${current_dir}"
