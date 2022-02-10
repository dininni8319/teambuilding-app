# Provisioning for teambuilding-app
Provisioning repository for [teambuilding-app](https://github.com/Multidialogo/teambuilding-app)

### Requirements

- git
- docker-ce, docker-ce-cli, containerd.io, docker-compose (V2)

### Setup

Run *setup-provisioning.sh* and follow the on-screen instructions.

### Build the production image

Run *./scripts/build-prod-image.sh* and follow the on-screen instructions.

### Run commands on the containerized environment

```bash
docker compose exec teambuilding_web [CMD]
```

### Tests

```bash
docker compose exec --env DEBUG=False teambuilding_web python manage.py test
```

### Frequently used commands

```bash
# Collects the static files into STATIC_ROOT
docker compose exec teambuilding_web python manage.py collectstatic

# Creates new migrations based on the changes detected to your models.
docker compose exec teambuilding_web python manage.py makemigrations

# Synchronizes the database state with the current set of models and migrations.
docker compose exec teambuilding_web python manage.py migrate

# Outputs to a yaml file all data in the database
docker compose exec teambuilding_web python manage.py dumpdata --format yaml -o [FIXTURE_PATH]

# Loads the contents of the fixture file into the database
docker compose exec teambuilding_web python manage.py loaddata [FIXTURE_PATH]

# Runs over the entire source tree of the current directory and pulls out all strings marked for translation. 
docker compose exec teambuilding_web python manage.py makemessages -l it -e py,html

# Compiles .po files created by makemessages to .mo files for use with the built-in gettext support.
docker compose exec teambuilding_web python manage.py compilemessages
```
