"use strict";

const choices = ["rock", "paper", "scissors"];
const winningPairs = new Set(["rock:scissors", "paper:rock", "scissors:paper"]);

const score = { player: 0, computer: 0, draws: 0, rounds: 0 };
const playerScore = document.querySelector("#player-score");
const computerScore = document.querySelector("#computer-score");
const drawScore = document.querySelector("#draw-score");
const resultText = document.querySelector("#result");
const roundText = document.querySelector("#round");

function decideWinner(player, computer) {
  if (!choices.includes(player) || !choices.includes(computer)) {
    throw new Error("Invalid game choice.");
  }
  if (player === computer) return "draw";
  return winningPairs.has(`${player}:${computer}`) ? "win" : "loss";
}

function updateScoreboard() {
  playerScore.textContent = String(score.player);
  computerScore.textContent = String(score.computer);
  drawScore.textContent = String(score.draws);
  roundText.textContent = `Round ${score.rounds + 1}`;
}

function play(playerChoice) {
  const computerChoice = choices[Math.floor(Math.random() * choices.length)];
  const outcome = decideWinner(playerChoice, computerChoice);
  score.rounds += 1;

  if (outcome === "draw") {
    score.draws += 1;
    resultText.textContent = `Draw — both chose ${playerChoice}.`;
  } else if (outcome === "win") {
    score.player += 1;
    resultText.textContent = `You win — ${playerChoice} beats ${computerChoice}.`;
  } else {
    score.computer += 1;
    resultText.textContent = `Computer wins — ${computerChoice} beats ${playerChoice}.`;
  }
  updateScoreboard();
}

function resetGame() {
  Object.assign(score, { player: 0, computer: 0, draws: 0, rounds: 0 });
  resultText.textContent = "Scores reset. Choose a move to begin.";
  updateScoreboard();
}

document.querySelectorAll("[data-choice]").forEach((button) => {
  button.addEventListener("click", () => play(button.dataset.choice));
});
document.querySelector("#reset").addEventListener("click", resetGame);
