Readme languages: ENG / ITA

## ENG

### Requirements

- git
- docker-ce, docker-ce-cli, containerd.io, docker-compose (V2)

### Setup

1. From the terminal, change to the directory where is *setup.sh*.
2. Run *setup.sh* following the on-screen instructions.

### Run commands on the containerized environment

To run commands on the environment, make sure that the container is up and running, change to the directory of the *docker-compose.yaml* file, then type the command using this format:

```bash
docker compose exec SERVICE [CMD]
```

For example, if you want to run migrations on the *taste_purchase_web* service, the command would be:

```bash
docker compose exec taste_purchase_web python manage.py migrate
```

### Test

To run tests:

```bash
docker compose exec taste_purchase_web python manage.py test
```

## ITA

### Requisiti

- git
- docker-ce, docker-ce-cli, containerd.io, docker-compose (V2)

### Installazione

1. Nel terminale, posizionarsi nella directory in cui e' presente il file *setup.sh*.
2. Eseguire *setup.sh* seguendo le istruzioni che compariranno sul terminale.

### Utilizzo

Per eseguire qualsiasi comando python sfruttando l'environment containerizzato, assicurarsi che il container sia in esecuzione, e che il terminale sia sulla directory in cui e' presente il file docker-compose.yml. Digitare sul terminale il comando seguendo il sequente formato: 

```bash
docker compose exec SERVICE [CMD]
```

Ad esempio, se si volessero eseguire le migrazioni sul servizio *taste_purchase_web*, il comando da eseguire sarebbe il seguente:

```bash
docker compose exec taste_purchase_web python manage.py migrate
```

### Test

Per eseguire i test, eseguire il seguente comando:

```bash
docker compose exec taste_purchase_web python manage.py test
```
