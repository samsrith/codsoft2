"""Tkinter desktop interface for Rock–Paper–Scissors."""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from game_logic import Choice, Game, Outcome


class RockPaperScissorsApp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.game = Game()

        self.title("Rock–Paper–Scissors")
        self.geometry("620x470")
        self.minsize(520, 420)
        self.configure(padx=24, pady=24)

        self.score_text = tk.StringVar()
        self.round_text = tk.StringVar(value="Choose a move to start.")
        self.status_text = tk.StringVar(value="Round 1")

        self._build_ui()
        self._refresh_score()

    def _build_ui(self) -> None:
        ttk.Label(self, text="Rock–Paper–Scissors", font=("Arial", 24, "bold")).pack(
            pady=(0, 12)
        )
        ttk.Label(self, textvariable=self.score_text, font=("Arial", 13)).pack()
        ttk.Label(self, textvariable=self.status_text).pack(pady=(6, 20))

        choices = ttk.Frame(self)
        choices.pack(fill="x")
        for column, (label, choice) in enumerate(
            (("Rock", Choice.ROCK), ("Paper", Choice.PAPER), ("Scissors", Choice.SCISSORS))
        ):
            ttk.Button(
                choices,
                text=label,
                command=lambda selected=choice: self.play(selected),
            ).grid(row=0, column=column, padx=6, sticky="ew")
            choices.columnconfigure(column, weight=1)

        result = ttk.Label(
            self,
            textvariable=self.round_text,
            font=("Arial", 14, "bold"),
            anchor="center",
            justify="center",
            wraplength=520,
        )
        result.pack(fill="x", expand=True, pady=30)

        actions = ttk.Frame(self)
        actions.pack()
        ttk.Button(actions, text="Reset scores", command=self.reset_game).pack(
            side="left", padx=6
        )
        ttk.Button(actions, text="Close", command=self.destroy).pack(side="left", padx=6)

        self.bind("<Key-r>", lambda _event: self.play(Choice.ROCK))
        self.bind("<Key-p>", lambda _event: self.play(Choice.PAPER))
        self.bind("<Key-s>", lambda _event: self.play(Choice.SCISSORS))

    def play(self, choice: Choice) -> None:
        result = self.game.play_random(choice)
        prefix = {
            Outcome.WIN: "✓",
            Outcome.LOSS: "×",
            Outcome.DRAW: "=",
        }[result.outcome]
        self.round_text.set(f"{prefix} {result.message.capitalize()}")
        self.status_text.set(f"Round {self.game.rounds_played + 1}")
        self._refresh_score()

    def reset_game(self) -> None:
        self.game.reset()
        self.round_text.set("Scores reset. Choose a move to start.")
        self.status_text.set("Round 1")
        self._refresh_score()

    def _refresh_score(self) -> None:
        self.score_text.set(
            f"You: {self.game.player_score}   Computer: {self.game.computer_score}   "
            f"Draws: {self.game.draws}"
        )


def main() -> None:
    app = RockPaperScissorsApp()
    app.mainloop()


if __name__ == "__main__":
    main()
