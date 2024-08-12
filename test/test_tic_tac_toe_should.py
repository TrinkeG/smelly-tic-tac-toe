import unittest

from app.tic_tac_toe import TicTacToe


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = TicTacToe()

    def test_first_player_cannot_be_o(self):
        with self.assertRaises(Exception):
            self.game.play('O', 0, 0)

    def test_player_cannot_play_twice_in_a_row(self):
        self.game.play('X', 0, 0)
        with self.assertRaises(Exception):
            self.game.play('X', 1, 0)

    def test_player_cannot_play_in_last_played_position(self):
        self.game.play('X', 0, 0)
        with self.assertRaises(Exception):
            self.game.play('O', 0, 0)

    def test_player_cannot_play_in_any_played_position(self):
        self.game.play('X', 0, 0)
        self.game.play('O', 1, 0)
        with self.assertRaises(Exception):
            self.game.play('X', 0, 0)

    def test_player_x_wins_by_three_in_top_row(self):
        self.game.play('X', 0, 0)
        self.game.play('O', 1, 0)
        self.game.play('X', 0, 1)
        self.game.play('O', 1, 1)
        self.game.play('X', 0, 2)
        winner = self.game.winner()
        self.assertEqual(winner, "X")

    def test_player_o_wins_by_three_in_top_row(self):
        self.game.play('X', 1, 0)
        self.game.play('O', 0, 0)
        self.game.play('X', 1, 1)
        self.game.play('O', 0, 1)
        self.game.play('X', 2, 2)
        self.game.play('O', 0, 2)
        winner = self.game.winner()
        self.assertEqual(winner, "O")

    def test_player_x_wins_by_three_in_middle_row(self):
        self.game.play('X', 1, 0)
        self.game.play('O', 0, 0)
        self.game.play('X', 1, 1)
        self.game.play('O', 0, 1)
        self.game.play('X', 1, 2)
        winner = self.game.winner()
        self.assertEqual(winner, "X")

    def test_player_o_wins_by_three_in_middle_row(self):
        self.game.play('X', 0, 0)
        self.game.play('O', 1, 0)
        self.game.play('X', 2, 1)
        self.game.play('O', 1, 1)
        self.game.play('X', 2, 2)
        self.game.play('O', 1, 2)
        winner = self.game.winner()
        self.assertEqual(winner, "O")

    def test_player_x_wins_by_three_in_bottom_row(self):
        self.game.play('X', 2, 0)
        self.game.play('O', 0, 0)
        self.game.play('X', 2, 1)
        self.game.play('O', 0, 1)
        self.game.play('X', 2, 2)
        winner = self.game.winner()
        self.assertEqual(winner, "X")

    def test_player_o_wins_by_three_in_bottom_row(self):
        self.game.play('X', 0, 0)
        self.game.play('O', 2, 0)
        self.game.play('X', 1, 1)
        self.game.play('O', 2, 1)
        self.game.play('X', 0, 1)
        self.game.play('O', 2, 2)
        winner = self.game.winner()
        self.assertEqual(winner, "O")

if __name__ == '__main__':
    unittest.main()
