document.addEventListener('input', function(event) {
  if (event.target.classList.contains('textfield-score-ok')) {
    var classes = event.target.classList;

    var rowClass, colClass, licenseOpponent;
    for (var i = 0; i < classes.length; i++) {
      var cls = classes[i];
      if (cls.startsWith('row-')) {
        rowClass = cls;
      } else if (cls.startsWith('col-')) {
        colClass = cls;
      }
    }

    if (rowClass && colClass) {
      var row = parseInt(rowClass.split('-')[1]);
      var col = parseInt(colClass.split('-')[1]);

      // Obtenez la nouvelle valeur du textfield
      var newValue = event.target.value;

      // Récupérez le numéro de licence à partir de l'attribut data-license
      licenseOpponent = event.target.getAttribute('data-licence-opponent');
      license = event.target.getAttribute('data-license');


      // Affichez les valeurs dans la console
      console.log('Row:', row, 'Column:', col, 'licenseOpponent:', licenseOpponent, 'license:', license, 'New Value:', newValue);
    }
  }
});
