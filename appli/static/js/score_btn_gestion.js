
document.querySelectorAll('.btn__ajt1, .btn__suppr1, .btn__ajt2, .btn__suppr2').forEach(button => {
  button.addEventListener('click', (event) => {
      console.log("click")
      const matchId = event.target.dataset.matchId; 
      let tireurNumber = event.target.classList.contains('btn__ajt1') || event.target.classList.contains('btn__suppr1') ? 1 : 2;
      let scoreElement;
      if (tireurNumber === 1) {
          scoreElement = event.target.closest('.escrimeurs').querySelector('.score__escrimeur1');
      } else if (tireurNumber === 2) {
          scoreElement = event.target.closest('.escrimeurs').querySelector('.score__escrimeur2');
      }
      let idTypeMatch = document.getElementById('idTypeMatch').value;
      let score = parseInt(scoreElement.textContent, 10);
      if ((event.target.classList.contains('btn__ajt1') || event.target.classList.contains('btn__ajt2')) && ((idTypeMatch != 1 && score < 15) || (idTypeMatch == 1 && score < 5))) {
        score += 1;
    } else if (score > 0) {
        score -= 1;
    }

      // Update the score in the DOM immediately
      scoreElement.textContent = score;

      updateScore(matchId, score, tireurNumber);
  });
});

function updateScore(matchId, score, tireurNumber, id_type_match) {
  fetch('/update_score_match', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ matchId, score, tireurNumber }),
  })
  .then(response => response.json())
  .then(data => {
      if(data.success) {
          console.log('maj du score');
      } else {
          console.error('echec maj du score');
      }
  });
}