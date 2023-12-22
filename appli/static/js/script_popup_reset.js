// Fonctions pour afficher et cacher la popup
function showVerificationPopup() {
    document.getElementById("verificationPopup").style.display = "block";
}

function hideVerificationPopup() {
    document.getElementById("verificationPopup").style.display = "none";
}



// Lire la valeur de l'attribut data-show-popup
const closeModalButton = document.getElementById('closeModalButton');
const verificationPopup = document.getElementById("verificationPopup");
var shouldShowPopup = verificationPopup.getAttribute("data-show-popup") === "true";


closeModalButton.addEventListener('click', function() {
    verificationPopup.style.display = 'none';
});
// Utiliser shouldShowPopup pour contrôler l'affichage de la popup
if (shouldShowPopup) {
    showVerificationPopup();
} else {
    hideVerificationPopup();
}
