# inf3190-tp3-20231

## Description

* Ce projet a pour but de concevoir une application web servant a offrir un animal
  de compagnie en adoption.
* Ce travail est accompli pour le troisieme TP du cours introduction a la 
  programmation web - INF3190 donne a l'UQAM par M. Jacques Berger.

## Auteurs

- Etienne Dube (DUBE04079501)
- Christophe Cloutier (CLOC21119501)

## Dépendances

Voici la liste des dependances a installer avant de pouvoir compiler et lancer
le programme :
  - [Python 3](https://www.python.org/downloads/).
  - [Flask](https://flask.palletsprojects.com/en/2.2.x/).

## Fonctionnement

* En premier lieu, il est important de compiler le programme. Vous pouvez le faire
  avec la commande suivante lorsque que vous etes a la racine du projet dans le terminal
  (./chemin/vers/dossier) :

  ```sh
  $ cd ./chemin/vers/votre/dossier
  $ make
  ```
  Une fois que votre programme est compile, vous pouvez lancer le site web en copiant
  l'adresse http et en la collant dans votre fureteur :

  ```sh
  flask run
   *Serving Flask app "index.py"
   *Environment: production
   *WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
   *Debug mode: off
   *Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
  ```

## Plateformes supportées

Le site web a ete teste sur le fureteur Google Chrome.
