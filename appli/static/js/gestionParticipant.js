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
                        ajouterEscrimeurACompetition(escrimeur.id);
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
        fetch(`/ajouter_escrimeur_competition/${competitionId}/${escrimeurId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },

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
