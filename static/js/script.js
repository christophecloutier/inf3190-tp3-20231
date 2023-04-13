
//VALIDATION DU FORMULAIRE 'METTRE EN ADOPTION'
function validateFormAdoption() {
  var champs = ["nom-animal", "espece-animal", "race-animal", "age-animal", "description-animal", "courriel-animal", "adresse-animal", "ville-animal", "codepostal-animal"];
  var validation = true;
  for (var i = 0; i < champs.length; i++) {
    var valeur = document.getElementById(champs[i]).value;
    var erreur = document.getElementById("erreur-" + champs[i]);
    if (valeur === "") {
      erreur.style.display = "inline-block";
      validation = false;
    } else if (valeur.indexOf(",") !== -1) {
      erreur.textContent = "Erreur : Le champ ne doit pas contenir de virgule.";
      erreur.style.display = "inline-block";
      validation = false;
    } else if (champs[i] === "nom-animal" && !verifierNomAnimal(valeur)) {
      erreur.innerHTML = "Erreur : Le nom de l'animal doit contenir entre 3 et 20 caractères alphabétiques.";
      erreur.style.display = "inline-block";
      validation = false;
    } else if (champs[i] === "courriel-animal" && !validerEmail(valeur)) {
      erreur.style.display = "inline-block";
      validation = false;
    } else if (champs[i] === "ville-animal" && !validerVilleAnimal(valeur)) {
      erreur.style.display = "inline-block";
      validation = false;
    } else if (champs[i] === "codepostal-animal" && !validerCodePostalAnimal(valeur)) {
      erreur.style.display = "inline-block";
      validation = false;
    } else {
      erreur.style.display = "none";
    }
  }
  return validation;
}

function verifieromAnimal(nomAnimal) {
  var regex = /^[a-zA-Z]{3,20}$/;
  return regex.test(nomAnimal);
}

function validerEmail(email) {
  var regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return regex.test(email);
}

function validerVilleAnimal(villeAnimal) {
  var regex = /^[a-zA-Z]+$/;
  return regex.test(villeAnimal);
}

function validerCodePostalAnimal(codePostal) {
  var regex = /^[A-Za-z]\d[A-Za-z]\s\d[A-Za-z]\d$/;
  return regex.test(codePostal);
}



var form = document.getElementById('formulaire-adoption');
form.onsubmit = function() {
  // Empêchez le formulaire de se soumettre si les champs ne sont pas remplis
  return validateFormAdoption();
};