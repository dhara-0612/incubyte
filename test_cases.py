import unittest
from incubyte import Chandrayaan_3  # Import the Chandrayaan_3 class from your module

# Define a test class that inherits from unittest.TestCase
class TestChandrayaan(unittest.TestCase):
    def setUp(self):
        # Create a new Chandrayaan_3 object before each test case
        self.craft = Chandrayaan_3(0, 0, 0, "N")

    # Define a test method for moving forward
    def test_move_forward(self):
        self.craft.move_forward()
        assert self.craft.position == (0, 1, 0)

    # Define a test method for moving backward
    def test_move_backward(self):
        self.craft.move_backward()
        assert self.craft.position == (0, -1, 0)

    # Define a test method for turning left
    def test_turn_left(self):
        self.craft.turn_left()
        assert self.craft.direction == "W"

    # Define a test method for turning right
    def test_turn_right(self):
        self.craft.turn_right()
        assert self.craft.direction == "E"

    # Define a test method for turning up
    def test_turn_up(self):
        self.craft.turn_up()
        assert self.craft.direction == "U"

    # Define a test method for turning down
    def test_turn_down(self):
        self.craft.turn_down()
        assert self.craft.direction == "D"


# Check if the script is run directly (not imported as a module)
if __name__ == "__main__":
    unittest.main()  # Run the unittest framework to execute the defined test cases
