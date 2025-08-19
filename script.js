const welcomeScreen = document.getElementById("welcome-screen");
const modeScreen = document.getElementById("mode-screen");
const gameScreen = document.getElementById("game-screen");
const statusText = document.getElementById("status");
const resetBtn = document.getElementById("reset-btn");
const cells = document.getElementsByClassName("cell");

let board = ["", "", "", "", "", "", "", "", ""];
let currentPlayer = "X";
let gameActive = false;
let gameMode = 2;

window.onload = () => {
  welcomeScreen.classList.add("active");
};

function showModeSelection() {
  welcomeScreen.classList.remove("active");
  modeScreen.classList.add("active");
}

function startGame(mode) {
  gameMode = mode;
  board = ["", "", "", "", "", "", "", "", ""];
  currentPlayer = "X";
  gameActive = true;
  statusText.textContent = "Player X's turn";

  modeScreen.classList.remove("active");
  gameScreen.classList.add("active");

  resetBtn.classList.add("hidden");
  Array.from(cells).forEach(cell => {
    cell.textContent = "";
    cell.classList.remove("winner");
    cell.innerHTML = "";
  });
}

function makeMove(index) {
  if (!gameActive || board[index] !== "") return;

  board[index] = currentPlayer;
  cells[index].textContent = currentPlayer;
  animateMove(cells[index], currentPlayer);

  if (checkWinner()) {
    statusText.textContent = `Player ${currentPlayer} wins!`;
    gameActive = false;
    resetBtn.classList.remove("hidden");
    return;
  }

  if (!board.includes("")) {
    statusText.textContent = "It's a tie!";
    gameActive = false;
    resetBtn.classList.remove("hidden");
    return;
  }

  currentPlayer = currentPlayer === "X" ? "O" : "X";
  statusText.textContent = `Player ${currentPlayer}'s turn`;

  if (gameMode === 1 && currentPlayer === "O") {
    setTimeout(computerMove, 300);
  }
}

function animateMove(cell, player) {
  const icon = document.createElement("div");
  icon.classList.add("player-icon", player === "X" ? "player-x" : "player-o");
  cell.appendChild(icon);
}

function computerMove() {
  let bestScore = -Infinity;
  let move = -1;

  for (let i = 0; i < 9; i++) {
    if (board[i] === "") {
      board[i] = "O";
      let score = minimax(board, 0, false);
      board[i] = "";
      if (score > bestScore) {
        bestScore = score;
        move = i;
      }
    }
  }

  makeMove(move);
}

function minimax(newBoard, depth, isMaximizing) {
  let result = getWinner(newBoard);
  if (result !== null) {
    const scores = { X: -10, O: 10, Tie: 0 };
    return scores[result];
  }

  if (isMaximizing) {
    let bestScore = -Infinity;
    for (let i = 0; i < 9; i++) {
      if (newBoard[i] === "") {
        newBoard[i] = "O";
        let score = minimax(newBoard, depth + 1, false);
        newBoard[i] = "";
        bestScore = Math.max(score, bestScore);
      }
    }
    return bestScore;
  } else {
    let bestScore = Infinity;
    for (let i = 0; i < 9; i++) {
      if (newBoard[i] === "") {
        newBoard[i] = "X";
        let score = minimax(newBoard, depth + 1, true);
        newBoard[i] = "";
        bestScore = Math.min(score, bestScore);
      }
    }
    return bestScore;
  }
}

function getWinner(b) {
  const wins = [
    [0,1,2], [3,4,5], [6,7,8],
    [0,3,6], [1,4,7], [2,5,8],
    [0,4,8], [2,4,6]
  ];

  for (let [a,b1,c] of wins) {
    if (b[a] && b[a] === b[b1] && b[a] === b[c]) {
      return b[a];
    }
  }

  if (!b.includes("")) return "Tie";
  return null;
}

function checkWinner() {
  const winner = getWinner(board);
  if (winner && winner !== "Tie") {
    const wins = [
      [0,1,2], [3,4,5], [6,7,8],
      [0,3,6], [1,4,7], [2,5,8],
      [0,4,8], [2,4,6]
    ];

    for (let win of wins) {
      const [a,b,c] = win;
      if (board[a] && board[a] === board[b] && board[a] === board[c]) {
        cells[a].classList.add("winner");
        cells[b].classList.add("winner");
        cells[c].classList.add("winner");
        break;
      }
    }

    return true;
  }
  return false;
}

function resetGame() {
  gameScreen.classList.remove("active");
  modeScreen.classList.add("active");
  statusText.textContent = "";
}

