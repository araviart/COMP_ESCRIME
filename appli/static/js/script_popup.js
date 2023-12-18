document.addEventListener("DOMContentLoaded", function() {
  let popup = document.getElementById("popup");
  let overlay = document.getElementById("overlay");

  window.showPopup = function() {
      popup.classList.add("open-popup");
      overlay.style.display = "block";
  }

  window.closePopup = function() {
      popup.classList.remove("open-popup");
      overlay.style.display = "none";
  }
});