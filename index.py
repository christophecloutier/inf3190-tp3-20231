# Copyright 2022 <Votre nom et code permanent>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask
from flask import render_template
from flask import g
from .database import Database
from flask import request
from flask import redirect
import random
import re

app = Flask(__name__, static_url_path="", static_folder="static")


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = Database()
    return g._database


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.disconnect()


@app.route('/')
def form():
    liste = get_animaux_en_vedette()
    return render_template('index.html', animaux_en_vedette=liste)


def get_nbr_animaux():
    db = get_db()
    animaux = db.get_animaux()
    return len(animaux)


def get_nbr_random():
    nbr = get_nbr_animaux()
    print(nbr)
    return random.sample(range(1, nbr + 1), 6)


def get_animaux_en_vedette():
    db = get_db()
    en_vedette = []
    liste = get_nbr_random()
    print(liste)
    for int in liste:
        en_vedette.append(db.get_animal(int))
    return en_vedette


@app.route('/listeChien')
def listeChien():
    db = get_db()
    animaux = db.get_animaux()
    return render_template('listeChien.html', les_animaux=animaux)


@app.route('/listeChat')
def listeChat():
    db = get_db()
    animaux = db.get_animaux()
    return render_template('listeChat.html', les_animaux=animaux)


@app.route('/listeOiseau')
def listeOiseau():
    db = get_db()
    animaux = db.get_animaux()
    return render_template('listeOiseau.html', les_animaux=animaux)


@app.route('/listeAutre')
def listeAutre():
    db = get_db()
    animaux = db.get_animaux()
    return render_template('listeAutre.html', les_animaux=animaux)


@app.route('/adoption')
def adoption():
    return render_template('adoption.html')


@app.route('/confirmation-adoption')
def confirmation():
    return render_template('confirmation_adoption.html')

@app.route('/erreur-adoption')
def erreur_adoption():
    return render_template('erreur_adoption.html')


@app.route('/animal/<idAnimal>')
def show_animal(idAnimal):
    db = get_db()
    animal = db.get_animal(idAnimal)
    return render_template('animal.html', animal=animal)


def verifier_nom_animal(nom_animal):
    regex = r'^[a-zA-Z]{3,20}$'
    return bool(re.match(regex, nom_animal))

def valider_courriel(courriel):
    regex = r'^[^\s@]+@[^\s@]+\.[^\s@]+$'
    return bool(re.match(regex, courriel))

def valider_ville_animal(ville_animal):
    regex = r'^[a-zA-Z]+$'
    return bool(re.match(regex, ville_animal))

def valider_code_postal_animal(code_postal):
    regex = r'^[A-Za-z]\d[A-Za-z]\s\d[A-Za-z]\d$'
    return bool(re.match(regex, code_postal))

def validation_formulaire(nom, espece, race, age, description, courriel, adresse, ville, code_postal):
    champs = [nom, espece, race, age, description, courriel, adresse, ville, code_postal]
    for i in range(len(champs)):
        if (champs[i] == "") or ("," in champs[i]) or (i == 0 and not verifier_nom_animal(nom)) or (i== 5 and not valider_courriel(courriel)) or (i == 7 and not valider_ville_animal(ville)) or (i == 8 and not valider_code_postal_animal(code_postal)):
            return False
        else:
            return True

@app.route('/submit', methods=['POST'])
def submit():
    db = get_db()
    nom = request.form.get('nom-animal')
    espece = request.form.get('espece-animal')
    race = request.form.get('race-animal')
    age = request.form.get('age-animal')
    description = request.form.get('description-animal')
    courriel = request.form.get('courriel-animal')
    adresse = request.form.get('adresse-animal')
    ville = request.form.get('ville-animal')
    code_postal = request.form.get('codepostal-animal')
    if not validation_formulaire(nom, espece, race, age, description, courriel, adresse, ville, code_postal):
        return redirect('/erreur-adoption')
    db.add_animal(nom, espece, race, age, description, courriel, adresse, ville, code_postal)
    return redirect('/confirmation-adoption')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, extra_files=['./static/js/script.js'])
