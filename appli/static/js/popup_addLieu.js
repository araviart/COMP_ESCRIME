document.addEventListener('DOMContentLoaded', (event) => {
  const openModalButton = document.getElementById('openModalButton');
  const modal = document.getElementById('modal');
  const editLieuIcon = document.getElementById('editLieuIcon');
  const closeModalButton = document.getElementById('closeModalButton');
  const saveButton = modal.querySelector('button[type="button"]');
  const lieuInfoSpan = document.getElementById('lieuInfo');

  openModalButton.addEventListener('click', function() {
    modal.style.display = 'block';
  });

  editLieuIcon.addEventListener('click', function() {
    modal.style.display = 'block';
  });
  
  closeModalButton.addEventListener('click', function() {
    modal.style.display = 'none';
  });

  saveButton.addEventListener('click', function() {
    // Retrieve the values from the input fields when the save button is clicked
    const nomLieuValue = document.getElementById('nomLieu').value;
    const adresseLieuValue = document.getElementById('adresseLieu').value;
    const villeLieuValue = document.getElementById('villeLieu').value;
    const codePostalLieuValue = document.getElementById('codePostalLieu').value;

    // Update the span with the location information
    lieuInfoSpan.innerHTML = `<p style="color: black; font-size: 15px; max-width: 300px;">${nomLieuValue}: ${adresseLieuValue}, ${villeLieuValue}, ${codePostalLieuValue}</p>`;
    
    // Update the hidden fields in the main form
    document.getElementById('hiddenNomLieu').value = nomLieuValue;
    document.getElementById('hiddenAdresseLieu').value = adresseLieuValue;
    document.getElementById('hiddenVilleLieu').value = villeLieuValue;
    document.getElementById('hiddenCodePostalLieu').value = codePostalLieuValue;
    
    editLieuIcon.style.display = 'inline-block';
    openModalButton.style.display = 'none';

    modal.style.display = 'none';
  });
});
