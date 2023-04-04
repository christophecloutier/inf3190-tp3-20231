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
from flask import url_for
from flask import request
import sqlite3

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
    return render_template('index.html')

@app.route('/adoption')
def adoption():
    return render_template('adoption.html')

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
    codePostal = request.form.get('codepostal-animal')
    db.add_animal(nom, espece, race, age, description, courriel, adresse, ville, codePostal)
    return 'Animal ajouté à la base de données avec succès!'

if __name__ == '__main__':
    app.run(debug=True, extra_files=['./static/js/script.js'])