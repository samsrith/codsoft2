import random
import unittest

from game_logic import Choice, Game, Outcome, decide_winner, parse_choice


class RuleTests(unittest.TestCase):
    def test_every_choice_draws_with_itself(self) -> None:
        for choice in Choice:
            with self.subTest(choice=choice):
                self.assertEqual(decide_winner(choice, choice), Outcome.DRAW)

    def test_all_winning_pairs(self) -> None:
        pairs = (
            (Choice.ROCK, Choice.SCISSORS),
            (Choice.PAPER, Choice.ROCK),
            (Choice.SCISSORS, Choice.PAPER),
        )
        for player, computer in pairs:
            with self.subTest(player=player, computer=computer):
                self.assertEqual(decide_winner(player, computer), Outcome.WIN)

    def test_all_losing_pairs(self) -> None:
        pairs = (
            (Choice.ROCK, Choice.PAPER),
            (Choice.PAPER, Choice.SCISSORS),
            (Choice.SCISSORS, Choice.ROCK),
        )
        for player, computer in pairs:
            with self.subTest(player=player, computer=computer):
                self.assertEqual(decide_winner(player, computer), Outcome.LOSS)

    def test_choice_parser_is_case_insensitive(self) -> None:
        self.assertEqual(parse_choice(" Rock "), Choice.ROCK)

    def test_invalid_choice_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            decide_winner("water", Choice.ROCK)


class GameStateTests(unittest.TestCase):
    def test_scores_and_rounds_are_updated(self) -> None:
        game = Game()
        game.play(Choice.ROCK, Choice.SCISSORS)
        game.play(Choice.ROCK, Choice.PAPER)
        game.play(Choice.ROCK, Choice.ROCK)
        self.assertEqual(
            (game.player_score, game.computer_score, game.draws, game.rounds_played),
            (1, 1, 1, 3),
        )

    def test_reset_clears_all_state(self) -> None:
        game = Game()
        game.play(Choice.PAPER, Choice.ROCK)
        game.reset()
        self.assertEqual(
            (game.player_score, game.computer_score, game.draws, game.rounds_played),
            (0, 0, 0, 0),
        )

    def test_seeded_random_game_is_reproducible(self) -> None:
        first = Game().play_random(Choice.ROCK, random.Random(7))
        second = Game().play_random(Choice.ROCK, random.Random(7))
        self.assertEqual(first.computer_choice, second.computer_choice)


if __name__ == "__main__":
    unittest.main()
