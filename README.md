## Requisiti

- git
- docker-ce, docker-ce-cli, containerd.io, docker-compose (V2)

## Installazione

1. Nel terminale, posizionarsi nella directory in cui e' presente il file *setup.sh*.
2. Eseguire *setup.sh* seguendo le istruzioni che compariranno sul terminale.
3. Nel terminale, posizionarsi nella directory contenente il progetto che si vuole modificare.

## Utilizzo

Per eseguire qualsiasi comando python sfruttando l'environment containerizzato, assicurarsi che il container sia in esecuzione, e digitare sul terminale il comando seguendo il sequente formato: 

```bash
docker compose exec SERVICE [CMD]
```

Ad esempio, se si volessero eseguire le migrazioni sul servizio *taste_purchase_web*, il comando da eseguire sarebbe il seguente:

```bash
docker compose exec taste_purchase_web python manage.py migrate
```