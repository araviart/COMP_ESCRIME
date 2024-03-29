document.addEventListener("DOMContentLoaded", function() {
    console.log("Document is ready!");
    var participants_total = participants.length;

    $('#checkbox-valid-all').change(function() {
        var isChecked = $(this).prop('checked');
        $('.checkbox-participant').prop('checked', isChecked);
      
        if (isChecked) {
          // Si la case 'checkbox-valid-all' est cochée, ajoutez tous les participants à 'participants_present'
          participants_present = participants.slice();
          participants_absents = []
        } else {
          // Si la case 'checkbox-valid-all' est décochée, videz 'participants_present'
          participants_present = [];
          participants_absents = participants
        }
        $('#participants-count').text(participants_present.length + "/" + participants.length);
        $('#absents-count').text(participants_absents.length + "/" + participants_total);
      });

      $('.checkbox-participant').change(function() {
        var row = participants[$(this).closest('tr').data('id')];
        if (this.checked) {
          // Ajouter les informations de la ligne à la liste
          participants_present.push(row);
          participants_absents = participants_absents.filter(function(participant){
            return participant !== row;
          });
        } else {
          // Retirer les informations de la ligne de la liste
          participants_present = participants_present.filter(function(participant) {
            return participant !== row;
          });
          participants_absents.push(row)
        }
        $('#participants-count').text(participants_present.length + "/" + participants_total);
        $('#absents-count').text(participants_absents.length + "/" + participants_total);
      });

    $('button:has(.fa-solid.fa-check)').click(function() {
        participants_absents = [];
        $('.checkbox-participant').each(function() {
          console.log("Bouton cliqué")
          var row = participants[$(this).closest('tr').data('id')];
          if (!$(this).prop('checked')) {
            // Si la case à cocher n'est pas cochée, ajoutez le participant à la liste des participants absents
            participants_absents.push(row);
          
          }
        });
      
        // Ici, vous pouvez faire ce que vous voulez avec la liste des participants absents
        console.log(participants_absents);
        $('#absents-count').text(participants_absents.length + "/" + participants_total);
      });

      document.getElementById("bouton_valid").addEventListener("click", function(){
        var listeLicence = "";
        for (var part of participants_absents) {
            listeLicence += part.numeroLicenceE + ",";
        }
        listeLicence = listeLicence.slice(0, -1);
    
        // Mettre à jour la valeur du champ caché avec la liste des absents
        document.getElementById("listeAbsentsInput").value = listeLicence;
    
        // Soumettre le formulaire
        document.getElementById("validationForm").submit();
    });    
  });