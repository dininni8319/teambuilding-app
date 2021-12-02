#bin/sh
echo 'Installing application...'

echo 'Do you want to pull code from a custom repo?'
read -n 1 -s -r -p '(Y/N): ' confirm_custom_repo
if [[ $confirm_custom_repo == [yY] ]]
then
  read -p 'Enter a custom location: ' repo_location
else
  echo 'No remote repo... yet'
  exit 1
fi

current_dir=$PWD

rm -rf Docker/app/source
mkdir -p Docker/app/source
cd Docker/app/source
git clone $repo_location .
cd $current_dir

cp .env.dist .env
echo 'Edit the .env file with your variables'
read -n 1 -s -r -p 'Press any key to continue when you are finished'
echo ''
docker compose up --build -d
docker compose exec web python manage.py migrate
