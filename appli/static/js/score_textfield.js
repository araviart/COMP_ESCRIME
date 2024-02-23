var isDOMLoaded = false;

document.addEventListener("DOMContentLoaded", function () {
  if (isDOMLoaded) {
    return;
  }

  isDOMLoaded = true;
  // Sélectionnez tous les champs de texte avec la classe "textfield-score-ok"
  var textfields = document.querySelectorAll('.textfield-score-ok');

  // Ajoutez un écouteur d'événement à chaque champ de texte
  textfields.forEach(function (textfield) {
    textfield.addEventListener('input', function () {
      // Récupérez les données nécessaires pour la requête AJAX
      var license = textfield.getAttribute('data-license');
      var opponentLicense = textfield.getAttribute('data-licence-opponent');
      var score = textfield.value;
      var idPoule = textfield.getAttribute('data-id-poule');
      var idCompetition = textfield.getAttribute('data-id-competition');
      var idPiste = textfield.getAttribute('data-id-piste');
      var idArbitre = textfield.getAttribute('data-id-arbitre');
      var idTypeMatch = document.getElementById('id-type-match').value;


      // Construisez les données à envoyer dans la requête AJAX
      var data = {
        'license': license,
        'idTypeMatch': idTypeMatch,
        'opponentLicense': opponentLicense,
        'score': score,
        'idPoule': idPoule,
        'idCompetition': idCompetition,
        'idPiste': idPiste,
        'idArbitre': idArbitre,
        'idTypeMatch': idTypeMatch

      };

      // Envoyez une requête POST AJAX au serveur Flask pour mettre à jour la base de données
      fetch('/update_scores', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      })
        .then(response => response.text())
        .then(data => {
          console.log('Success:', data);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    });
  });
});
