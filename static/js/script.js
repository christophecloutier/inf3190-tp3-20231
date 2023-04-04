
//VALIDATION DU FICHIER 'METTRE EN ADOPTION'
function validateFormAdoption() {
  var champs = ["nom-animal", "espece-animal", "race-animal", "age-animal", "description-animal", "courriel-animal", "adresse-animal"];
  var validation = true;
  for (var i = 0; i < champs.length; i++) {
    var valeur = document.getElementById(champs[i]).value;
    var erreur = document.getElementById("erreur-" + champs[i]);
    if (valeur === "") {
      erreur.style.display = "inline-block";
      validation = false;
    } else {
      erreur.style.display = "none";
    }
  }
  return validation;
}

var form = document.getElementById('formulaire-adoption');
form.addEventListener('submit', validateFormAdoption);
form.onsubmit = function() {
  // Empêchez le formulaire de se soumettre si les champs ne sont pas remplis
  return validateFormAdoption();
};