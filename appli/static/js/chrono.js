document.addEventListener("DOMContentLoaded", function() {
  const timeDisplay = document.querySelector('.time');
  const startButton = document.querySelector('.btn__start');
  const resetButton = document.querySelector('.btn__reset');

  let timer;
  let timeLeft = 3 * 60; // Initial time in seconds (3 minutes)

  function updateDisplay() {
    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;
    timeDisplay.textContent = `${minutes} : ${seconds < 10 ? '0' : ''}${seconds}`;
  }

  function startTimer() {
    timer = setInterval(() => {
      if (timeLeft > 0) {
        timeLeft--;
        updateDisplay();
      } else {
        clearInterval(timer);
        alert("Le minuteur est terminé !");
        resetButton.disabled = false; 
      }
    }, 1000);
  }

  startButton.addEventListener('click', function() {
    if (startButton.textContent === 'Start') {
      startTimer();
      startButton.textContent = 'Stop';
      resetButton.disabled = true; 
    } else if (startButton.textContent === 'Stop') {
      clearInterval(timer);
      startButton.textContent = 'Start';
      resetButton.disabled = false; 
    }
  });

  resetButton.addEventListener('click', function() {
    timeLeft = 3 * 60;
    updateDisplay();
    clearInterval(timer);
    startButton.textContent = 'Start';
    resetButton.disabled = false; 
  });

  updateDisplay();
});