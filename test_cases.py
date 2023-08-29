import unittest
from incubyte import Chandrayaan_3


class TestChandrayaan(unittest.TestCase):
    def test_move_forward(self):
        craft = Chandrayaan_3(0, 0, 0, "N")
        craft.move_forward()
        assert craft.position == (0, 1, 0)

    def test_move_backward(self):
        craft = Chandrayaan_3(0, 0, 0, "N")
        craft.move_backward()
        assert craft.position == (0, -1, 0)

    def test_turn_left(self):
        craft = Chandrayaan_3(0, 0, 0, "N")
        craft.turn_left()
        assert craft.direction == "W"

    def test_turn_right(self):
        craft = Chandrayaan_3(0, 0, 0, "N")
        craft.turn_right()
        assert craft.direction == "E"

    def test_turn_up(self):
        craft = Chandrayaan_3(0, 0, 0, "N")
        craft.turn_up()
        assert craft.direction == "U"

    def test_turn_down(self):
        craft = Chandrayaan_3(0, 0, 0, "N")
        craft.turn_down()
        assert craft.direction == "D"


if __name__ == "__main__":
    unittest.main()
