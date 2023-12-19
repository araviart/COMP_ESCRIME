document.addEventListener('DOMContentLoaded', function () {
    const addButtons = document.querySelectorAll('.addp button');
    const confirmation = localStorage.getItem('confirmation');
    if (confirmation) {
        showConfirmation(confirmation);
        localStorage.removeItem('confirmation');
    }
    
    addButtons.forEach(addButton => {
        addButton.addEventListener('click', function (event) {
            event.preventDefault();
            const submenu = addButton.nextElementSibling;
            submenu.style.display = submenu.style.display === 'none' ? 'block' : 'none';
            const escrimeursList = submenu.querySelector('.escrimeurs-list');
            const searchInput = submenu.querySelector('.search');

            let url;
            if (addButton.closest('.escrimeblois')) {
                url = '/get_escrimeurs';
            } else if (addButton.closest('.escrime-other')) {
                url = '/';
            } else if (addButton.closest('.escrime-arb')) {
                url = '/';
            }

            if (url) {
                fetchEscrimeurs(escrimeursList, url);
            }

            // Set up search input event listener for each submenu when it is opened
            searchInput.addEventListener('input', function () {
                const searchTerm = searchInput.value.toLowerCase();
                const listItems = Array.from(escrimeursList.children);

                listItems.forEach(item => {
                    const match = item.textContent.toLowerCase().includes(searchTerm);
                    item.style.display = match ? 'block' : 'none';
                });
            });
            
                // You should define fetchEscrimeurs and ajouterEscrimeurACompetition here or elsewhere that it is in scope
                function fetchEscrimeurs(escrimeursList, url) {
                    fetch(url)
                        .then(response => response.json())
                        .then(escrimeurs => {
                            escrimeursList.innerHTML = ''; // Clear the previous list
                            escrimeurs.forEach(escrimeur => {
                                const listItem = document.createElement('div');
                                listItem.setAttribute('data-prenom', escrimeur.prenomE.toLowerCase());
                                listItem.setAttribute('data-nom', escrimeur.nomE.toLowerCase());
                                listItem.setAttribute('data-licence', escrimeur.numeroLicenceE);
                                listItem.textContent = `${escrimeur.prenomE} ${escrimeur.nomE} ${escrimeur.numeroLicenceE}`;
                                listItem.addEventListener('click', function () {
                                    ajouterEscrimeurACompetition(escrimeur.numeroLicenceE);
                                    submenu.style.display = 'none';
                                });
                                escrimeursList.appendChild(listItem);
                            });
                        })
                        .catch(error => {
                            console.error('Erreur lors de la requête pour obtenir les escrimeurs:', error);
                        });
                }
            
                // … Rest of your functions (ajouterEscrimeurACompetition, edit, validateField, updateDatabase, showConfirmation) …
            });
                    
                    function ajouterEscrimeurACompetition(escrimeurId) {
                        fetch(`/ajouter_escrimeur_competition/${competitionId}`, {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                            body: JSON.stringify({ numeroLicenceE: escrimeurId })
                        })
                        .then(response => {
                            if (response.ok) {
                                console.log('Escrimeur ajouté à la compétition avec succès.');
                            localStorage.setItem('confirmation', 'Escrimeur ajouté à la compétition avec succès.');
                            location.reload();
                        } else {
                            console.error('Erreur lors de l\'ajout de l\'escrimeur à la compétition.');
                        }
                    })
                    .catch(error => {
                        console.error('Erreur lors de la requête pour ajouter l\'escrimeur à la compétition:', error);
                    });
                }
                
                const confirmation = localStorage.getItem('confirmation');
                if (confirmation) {
                    showConfirmation(confirmation);
                    localStorage.removeItem('confirmation');
                }
            });
            
            
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
            
            
            
            
            searchInput.addEventListener('input', function () {
                const searchTerm = searchInput.value.toLowerCase();
                const listItems = Array.from(escrimeursList.children);
                
                listItems.forEach(item => {
                    const prenom = item.getAttribute('data-prenom');
                    const nom = item.getAttribute('data-nom');
                    const licence = item.getAttribute('data-licence');
                    const isMatch = prenom.includes(searchTerm) || nom.includes(searchTerm) || licence.includes(searchTerm);
                    item.style.display = isMatch ? 'block' : 'none';
                });
            });
        });