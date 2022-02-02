Readme languages: ENG / ITA

## ENG

### Requirements

- git
- docker-ce, docker-ce-cli, containerd.io, docker-compose (V2)

### Setup

Run *setup-provisioning.sh* and follow the on-screen instructions.

### Build the production image

Run *./scripts/build-prod-image.sh* and follow the on-screen instructions.

### Run commands on the containerized environment

```bash
docker compose exec taste_purchase_web [CMD]
```

### Tests

```bash
docker compose exec --env DEBUG=False taste_purchase_web python manage.py test
```

### Frequently used commands

```bash
# Collects the static files into STATIC_ROOT
docker compose exec taste_purchase_web python manage.py collectstatic

# Creates new migrations based on the changes detected to your models.
docker compose exec taste_purchase_web python manage.py makemigrations

# Synchronizes the database state with the current set of models and migrations.
docker compose exec taste_purchase_web python manage.py migrate

# Outputs to a yaml file all data in the database
docker compose exec taste_purchase_web python manage.py dumpdata --format yaml -o [FIXTURE_PATH]

# Loads the contents of the fixture file into the database
docker compose exec taste_purchase_web python manage.py loaddata [FIXTURE_PATH]

# Runs over the entire source tree of the current directory and pulls out all strings marked for translation. 
docker compose exec taste_purchase_web python manage.py makemessages -l it -e py,html

# Compiles .po files created by makemessages to .mo files for use with the built-in gettext support.
docker compose exec taste_purchase_web python manage.py compilemessages
```

## ITA

### Requisiti

- git
- docker-ce, docker-ce-cli, containerd.io, docker-compose (V2)

### Installazione

Esegui *setup-provisioning.sh* e segui le istruzioni a schermo.

### Esportare l'immagine di produzione

Esegui *./scripts/build-prod-image.sh* e segui le istruzioni a schermo.

### Eseguire comandi nell'ambiente containerizzato

```bash
docker compose exec taste_purchase_web [CMD]
```

### Test

```bash
docker compose exec --env DEBUG=False taste_purchase_web python manage.py test
```

### Comandi degni di nota

```bash
# Colleziona i file statici in STATIC_ROOT
docker compose exec taste_purchase_web python manage.py collectstatic

# Crea nuove migrazioni in base alle modifiche riscontrate nei model.
docker compose exec taste_purchase_web python manage.py makemigrations

# Sincronizza lo stato del database con le migrazioni
docker compose exec taste_purchase_web python manage.py migrate

# Esporta in un file yaml i dati contenuti nel database
docker compose exec taste_purchase_web python manage.py dumpdata --format yaml -o [FIXTURE_PATH]

# Carica il contenuto delle fixture nel database
docker compose exec taste_purchase_web python manage.py loaddata [FIXTURE_PATH]

# Estrae tutte le stringhe taggate per la traduzione
docker compose exec taste_purchase_web python manage.py makemessages -l it -e py,html

# Compila i file .po creati dal comando makemessages in file .mo compatibili con gettext.
docker compose exec taste_purchase_web python manage.py compilemessages
```
