"""Core rules and score state for Rock–Paper–Scissors."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from random import Random


class Choice(str, Enum):
    ROCK = "rock"
    PAPER = "paper"
    SCISSORS = "scissors"


class Outcome(str, Enum):
    WIN = "win"
    LOSS = "loss"
    DRAW = "draw"


WINNING_PAIRS = {
    (Choice.ROCK, Choice.SCISSORS),
    (Choice.PAPER, Choice.ROCK),
    (Choice.SCISSORS, Choice.PAPER),
}


def parse_choice(value: str | Choice) -> Choice:
    """Return a valid choice or raise a clear error."""
    if isinstance(value, Choice):
        return value
    try:
        return Choice(value.strip().lower())
    except (AttributeError, ValueError) as error:
        valid = ", ".join(choice.value for choice in Choice)
        raise ValueError(f"Choice must be one of: {valid}.") from error


def decide_winner(player: str | Choice, computer: str | Choice) -> Outcome:
    """Evaluate one round without changing any score state."""
    player_choice = parse_choice(player)
    computer_choice = parse_choice(computer)
    if player_choice == computer_choice:
        return Outcome.DRAW
    if (player_choice, computer_choice) in WINNING_PAIRS:
        return Outcome.WIN
    return Outcome.LOSS


@dataclass(frozen=True, slots=True)
class RoundResult:
    round_number: int
    player_choice: Choice
    computer_choice: Choice
    outcome: Outcome

    @property
    def message(self) -> str:
        if self.outcome == Outcome.DRAW:
            return f"Draw — both chose {self.player_choice.value}."
        if self.outcome == Outcome.WIN:
            return f"You win — {self.player_choice.value} beats {self.computer_choice.value}."
        return f"Computer wins — {self.computer_choice.value} beats {self.player_choice.value}."


@dataclass(slots=True)
class Game:
    player_score: int = 0
    computer_score: int = 0
    draws: int = 0
    rounds_played: int = 0

    def play(self, player: str | Choice, computer: str | Choice) -> RoundResult:
        player_choice = parse_choice(player)
        computer_choice = parse_choice(computer)
        outcome = decide_winner(player_choice, computer_choice)
        self.rounds_played += 1

        if outcome == Outcome.WIN:
            self.player_score += 1
        elif outcome == Outcome.LOSS:
            self.computer_score += 1
        else:
            self.draws += 1

        return RoundResult(
            round_number=self.rounds_played,
            player_choice=player_choice,
            computer_choice=computer_choice,
            outcome=outcome,
        )

    def play_random(self, player: str | Choice, random_source: Random | None = None) -> RoundResult:
        generator = random_source or Random()
        computer = generator.choice(list(Choice))
        return self.play(player, computer)

    def reset(self) -> None:
        self.player_score = 0
        self.computer_score = 0
        self.draws = 0
        self.rounds_played = 0
