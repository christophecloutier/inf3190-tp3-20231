
//VALIDATION DU FORMULAIRE 'METTRE EN ADOPTION'
function validateFormAdoption() {
  var champs = ["nom-animal", "espece-animal", "race-animal", "age-animal", "description-animal", "courriel-animal", "adresse-animal", "ville-animal"];
  var validation = true;
  for (var i = 0; i < champs.length; i++) {
    var valeur = document.getElementById(champs[i]).value;
    var erreur = document.getElementById("erreur-" + champs[i]);
    if (valeur === "") {
      erreur.style.display = "inline-block";
      validation = false;
    } else if (valeur.indexOf(",") !== -1) {
      erreur.textContent = "Le champ ne doit pas contenir de virgule.";
      erreur.style.display = "inline-block";
      validation = false;
    } else if (champs[i] === "nom-animal" && !verifierNomAnimal(valeur)) {
      erreur.innerHTML = "Le nom de l'animal doit contenir entre 3 et 20 caractères alphabétiques.";
      erreur.style.display = "inline-block";
      validation = false;
    } else if (champs[i] === "courriel-animal" && !validerEmail(valeur)) {
      erreur.style.display = "inline-block";
      validation = false;
    } else if (champs[i] === "ville-animal" && !validerVilleAnimal(valeur)) {
      erreur.style.display = "inline-block";
      validation = false;
    } else {
      erreur.style.display = "none";
    }
  }
  return validation;
}

function verifierNomAnimal(nomAnimal) {
  var regex = /^[a-zA-Z]{3,20}$/;
  return regex.test(nomAnimal);
}

function validerEmail(email) {
  var re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
}

function validerVilleAnimal(villeAnimal) {
  var regex = /^[a-zA-Z]+$/;
  return regex.test(villeAnimal);
}

var form = document.getElementById('formulaire-adoption');
form.addEventListener('submit', validateFormAdoption);
form.onsubmit = function() {
  // Empêchez le formulaire de se soumettre si les champs ne sont pas remplis
  return validateFormAdoption();
};