#bin/sh
echo "Installing application..."

current_dir=${PWD}

echo "Do you want to pull code from a custom repo?"
read -n 1 -s -r -p "(Y/N): " confirm_custom_repo
echo ""
if [[ $confirm_custom_repo == [yY] ]]
then
  read -p "Enter a custom location: " repo_location
  echo ""
else
  repo_location="ssh://git-codecommit.eu-west-1.amazonaws.com/v1/repos/tb_taste_purchase"
fi

rm -rf Docker/app/source
mkdir -p Docker/app/source
cd Docker/app/source
git clone -b develop $repo_location .
cd $current_dir

cp .env.dist .env
echo "Edit the .env file with your variables"
read -n 1 -s -r -p "Press any key to continue when you are finished"
echo ""

export COMPOSE_FILE="${PWD}/docker-compose.yml"
cd Docker/app/source

docker compose up --build -d
docker compose exec web python manage.py migrate

xdg-open http://localhost:8000
