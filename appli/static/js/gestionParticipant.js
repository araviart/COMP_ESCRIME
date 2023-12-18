document.addEventListener('DOMContentLoaded', function () {
    const addButton = document.querySelector('.addp button');
    const submenu = document.getElementById('submenu');
    const escrimeursList = document.getElementById('escrimeurs-list');
    const searchInput = document.getElementById('search');

    addButton.addEventListener('click', function (event) {
        event.preventDefault();
        submenu.style.display = submenu.style.display === 'none' ? 'block' : 'none';
        fetch('/get_escrimeurs')
            .then(response => response.json())
            .then(escrimeurs => {
                escrimeursList.innerHTML = ''; // Clear the previous list
                escrimeurs.forEach(escrimeur => {
                    const listItem = document.createElement('div');
                    listItem.textContent = `${escrimeur.prenomE} ${escrimeur.nomE}`;
                    listItem.addEventListener('click', function () {
                        alert(`Selected: ${escrimeur.prenomE} ${escrimeur.nomE}`);
                        ajouterEscrimeurACompetition(escrimeur.id, competitionId);
                        submenu.style.display = 'none';
                    });
                    escrimeursList.appendChild(listItem);
                });
            })
            .catch(error => console.error('Error fetching escrimeurs:', error));
    });

    searchInput.addEventListener('input', function () {
    });

    function ajouterEscrimeurACompetition(escrimeurId) {
        fetch(`/ajouter_escrimeur_competition/${competitionId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ id_tireur: escrimeurId })
        })
        .then(response => {
            if (response.ok) {
                console.log('Escrimeur ajouté à la compétition avec succès.');
            } else {
                console.error('Erreur lors de l\'ajout de l\'escrimeur à la compétition.');
            }
        })
        .catch(error => {
            console.error('Erreur lors de la requête pour ajouter l\'escrimeur à la compétition:', error);
        });
    }
});

function editField(id) {
    var p = document.getElementById(id);
    var text = p.innerText;
    p.innerHTML = `<input type="text" id="${id}-input" value="${text}" style="width: 300px;"> <button onclick="validateField('${id}')">Valider</button>`;
  }
  
  function validateField(id) {
    var input = document.getElementById(id + '-input');
    var text = input.value;
    var p = document.getElementById(id);
    p.innerHTML = text;
    updateDatabase(id, text)
  }

  function updateDatabase(field, value) {
    fetch('/update_database', {
        method: 'POST',

        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ field: field, value: value, competitionId: competitionId }),
    })
    .then(response => {
        if (response.ok) {
            console.log('Champ mis à jour avec succès dans la base de données.');
            showConfirmation('Champ mis à jour avec succès');
        } else {
            console.error('Erreur lors de la mise à jour du champ dans la base de données.');
        }
    })
    .catch(error => {
        console.error('Erreur lors de la requête pour mettre à jour le champ dans la base de données:', error);
    });
}

function showConfirmation(message) {
    var confirmation = document.createElement('div');
    confirmation.className = 'confirmation';
    confirmation.innerText = message;
    document.body.appendChild(confirmation);

    setTimeout(function() {
        confirmation.style.opacity = '0';
    }, 2000);

    setTimeout(function() {
        document.body.removeChild(confirmation);
    }, 4000);
}