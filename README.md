# TP 5 - MikroTik CHR v7 : API RESTful

Automatisation de la configuration d'un routeur MikroTik CHR avec Python.

## Prerequis

- Python 3
- VM MikroTik CHR v7 accessible (ici 192.168.56.10)
- pip install requests python-dotenv

## Configuration

Creer un fichier `.env` a la racine (jamais versionne, voir `.gitignore`) :

    DEVICE_HOST=192.168.56.10
    DEVICE_USER=api-user
    DEVICE_PASSWORD=motdepasse

Cote routeur :

    /ip service enable www-ssl
    /user add name=api-user password=... group=full

## Scriptss

- `crud_demo.py` : GET, PUT (creation), PATCH puis DELETE d'une adresse IP sur ether2.
- `configure_router.py` : cree les routes statiques de la liste ROUTES si elles n'existent pas deja (idempotent).

Lancement :

    py crud_demo.py
    py configure_router.py
    py configure_router.py   (2e lancement : uniquement des [SKIP])

## Remarques

- Dans l'API REST de RouterOS, la creation se fait avec PUT (et non POST).
- verify=False car le certificat du routeur est auto-signe (laboratoire uniquement).