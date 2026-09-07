# Rock–Paper–Scissors

A beginner-friendly Rock–Paper–Scissors project implemented in two ways:

- a Python desktop application built with Tkinter;
- an accessible browser application built with HTML, CSS, and JavaScript.

The project demonstrates input validation, reusable game logic, state management,
responsive interface design, keyboard accessibility, and automated tests.

[![Validate project](https://github.com/samsrith/codsoft2/actions/workflows/ci.yml/badge.svg)](https://github.com/samsrith/codsoft2/actions/workflows/ci.yml)

## Features

- Play Rock, Paper, or Scissors against a random computer choice
- Track player, computer, draw, and round totals
- Reset a game without restarting the application
- Explain every round in plain language
- Use the browser version with a mouse or keyboard
- Test the Python rules independently from the graphical interface
- Run without third-party packages or online services

## Project structure

| Path | Purpose |
|---|---|
| `game_logic.py` | Reusable Python rules and score state |
| `rock_paper_scissors.py` | Tkinter desktop interface |
| `web/index.html` | Browser interface and semantic markup |
| `web/styles.css` | Responsive visual styling |
| `web/app.js` | Browser game state and interactions |
| `tests/test_game_logic.py` | Python unit tests for rules and scoring |

## Run the Python desktop version

Python 3.10 or newer is recommended. Tkinter is normally included with desktop
Python installations.

```bash
python rock_paper_scissors.py
```

No `pip install` command is required.

## Run the browser version

Open `web/index.html` directly in a modern browser, or start a local server:

```bash
python -m http.server 8000 --directory web
```

Then visit `http://localhost:8000`.

## Run validation

```bash
python -m py_compile game_logic.py rock_paper_scissors.py
python -m unittest discover -s tests -v
node --check web/app.js
```

## How the rules work

| Player choice | Beats | Loses to |
|---|---|---|
| Rock | Scissors | Paper |
| Paper | Rock | Scissors |
| Scissors | Paper | Rock |

A matching choice is a draw. The application uses Python's `random.choice` or
the browser's `Math.random` only for casual gameplay; neither is intended for
security-sensitive randomness.

## Portfolio scope

This is a small learning project rather than an online multiplayer service. It
does not collect personal information, require accounts, or send data to a
server. Scores exist only for the current session.

## Possible next improvements

1. Add best-of-three and best-of-five match modes.
2. Persist optional high scores locally.
3. Add end-to-end browser tests.
4. Package the Python application as a desktop executable.
