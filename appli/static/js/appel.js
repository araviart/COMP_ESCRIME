document.addEventListener("DOMContentLoaded", function() {
    console.log("Document is ready!");
    var participants_total = participants.length;

    $('#checkbox-valid-all').change(function() {
        var isChecked = $(this).prop('checked');
        $('.checkbox-participant').prop('checked', isChecked);
      
        if (isChecked) {
          // Si la case 'checkbox-valid-all' est cochée, ajoutez tous les participants à 'participants_present'
          participants_present = participants.slice();
        } else {
          // Si la case 'checkbox-valid-all' est décochée, videz 'participants_present'
          participants_present = [];
        }
        $('#participants-count').text(participants_present.length + "/" + participants.length);
      });

    $('.checkbox-participant').change(function() {
      var row = participants[$(this).closest('tr').data('id')];
      if (this.checked) {
        // Ajouter les informations de la ligne à la liste
        participants_present.push(row);
      } else {
        // Retirer les informations de la ligne de la liste
        participants_present = participants_present.filter(function(participant) {
          return participant !== row;
        });
      }
      $('#participants-count').text(participants_present.length + "/" + participants_total);
    });

    $('.fa-solid.fa-check').click(function() {
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
  });