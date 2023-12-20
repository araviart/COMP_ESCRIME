document.addEventListener("DOMContentLoaded", function() {

  document.querySelector(".btn-publier").addEventListener("click", function (event) {
    event.preventDefault();
    var nbParticipants = nbParticipantsBlois + nbParticipantsOther;
    var nbArbitres = nbParticipantsArb;
    if (nbParticipants < 3 || nbArbitres < 1) {
      if (nbParticipants < 3 && nbArbitres > 0) {
        let errorMessage = "Vous devez ajouter au moins trois participants pour créer la compétition";
        showError(errorMessage);
      }
      else if (nbArbitres < 1 && nbParticipants > 2) {
      let errorMessage = "Vous devez ajouter au moins un arbitre pour créer la compétition";
      showError(errorMessage);
      }
      else if (nbParticipants < 3 && nbArbitres < 1) {
        let errorMessage = "Vous devez ajouter au moins trois participants et un arbitre pour créer la compétition";
        showError(errorMessage);
      }
    } else if ((nbParticipants / nbArbitres) < 3 || (nbParticipants / nbArbitres) > 7) {
      let errorMessage = "Le nombre de participants ne correspond pas au nombre d'arbitres pour faire des poules de 3 à 7 tireurs";
      showError(errorMessage);
    }
    else if ((nbParticipants / nbArbitres) < 3 || (nbParticipants / nbArbitres) > 7) {
    let errorMessage = "Le nombre de participants ne correspond pas au nombre d'arbitres pour faire des poules de 3 à 7 tireurs";
    showError(errorMessage);
  } else {
    window.location.href = "/gestion_poules/" + competitionId;
  }
  
  function showError(message) {
    var errorDiv = document.createElement("div");
    errorDiv.className = "error";
    errorDiv.innerText = message;
    document.body.appendChild(errorDiv);
    
    setTimeout(function () {
      errorDiv.style.opacity = "0";
    }, 2000);
    
    setTimeout(function () {
      document.body.removeChild(errorDiv);
    }, 4000);
  }
  
});
});