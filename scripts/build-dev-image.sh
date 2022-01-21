#!/usr/bin/env bash

script_dir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
app_name="app"
provisioning_dir="${script_dir}/.."
dockerfile="${provisioning_dir}/Docker/${app_name}/Dockerfile"
source_dir="${provisioning_dir}/Docker/${app_name}/source"
repo_source="git@github.com:Multidialogo/teambuilding-app.git"
current_dir="${PWD}"

(
  set -o errexit
  set -o pipefail
  set -o nounset

  cd "${source_dir}"
  tag=$(git describe --exact-match --tags $(git log -n1 --pretty='%h'))
  cd "${current_dir}"

  docker build -f "${dockerfile}" \
    -t "teambuilding/taste-and-purchase-dev" \
    -t "teambuilding/taste-and-purchase-dev:${tag}" \
    --target dev \
    .
)

cd "${current_dir}"
