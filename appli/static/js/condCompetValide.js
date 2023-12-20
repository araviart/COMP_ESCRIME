document.addEventListener("DOMContentLoaded", function() {

  document.querySelector(".btn-publier").addEventListener("click", function (event) {
    event.preventDefault();
    var nbParticipants = nbParticipantsBlois + nbParticipantsOther;
    var nbArbitres = nbParticipantsArb;
    if (nbParticipants < 6 || nbArbitres < 1) {
    let errorMessage = "";
    if (nbParticipants < 6) {
      errorMessage += "Il doit y avoir au moins 6 participants pour créer 2 poules.\n";
    }
    if (nbArbitres < 1) {
      errorMessage += "Il doit y avoir au moins un arbitre associé à une poule.";
    }
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