# Define a global list to keep track of directions
dir_list = []


# Define Chandrayaan 3 class
class Chandrayaan_3:

    # Initialize direction and position
    def __init__(self, x, y, z, direction):
        self.position = (x, y, z)
        self.direction = direction

    # Move forward in respective axis based on the current direction
    def move_forward(self):
        x, y, z = self.position
        if self.direction == "N":
            self.position = (x, y + 1, z)
            dir_list.append(self.direction)
        elif self.direction == "S":
            self.position = (x, y - 1, z)
            dir_list.append(self.direction)
        elif self.direction == "E":
            self.position = (x + 1, y, z)
            dir_list.append(self.direction)
        elif self.direction == "W":
            self.position = (x - 1, y, z)
            dir_list.append(self.direction)
        elif self.direction == "U":
            self.position = (x, y, z + 1)
        elif self.direction == "D":
            self.position = (x, y, z - 1)

    # Move backward in respective axis based on the current direction
    def move_backward(self):
        x, y, z = self.position
        if self.direction == "N":
            self.position = (x, y - 1, z)
            dir_list.append(self.direction)
        elif self.direction == "S":
            self.position = (x, y + 1, z)
            dir_list.append(self.direction)
        elif self.direction == "E":
            self.position = (x - 1, y, z)
            dir_list.append(self.direction)
        elif self.direction == "W":
            self.position = (x + 1, y, z)
            dir_list.append(self.direction)
        elif self.direction == "U":
            self.position = (x, y, z - 1)
        elif self.direction == "D":
            self.position = (x, y, z + 1)

    # Turn left based on the current direction
    def turn_left(self):
        directions = ["N", "W", "S", "E"]

        # if the current direction is Up or Down then retrieve the last direction
        # inserted (North, South, East or West)
        # from the dir_list to determine in which direction to move
        if self.direction == "U" or self.direction == "D":
            self.direction = dir_list[-1]
            current_index = directions.index(self.direction)
            new_index = (current_index + 1) % len(directions)
            self.direction = directions[new_index]
            dir_list.append(self.direction)

        else:
            current_index = directions.index(self.direction)
            new_index = (current_index + 1) % len(directions)
            self.direction = directions[new_index]
            dir_list.append(self.direction)

    # Turn right based on the current direction
    def turn_right(self):
        directions = ["N", "E", "S", "W"]

        # if the current direction is Up or Down then retrieve the last direction
        # inserted (North, South, East or West)
        # from the dir_list to determine in which direction to move
        if self.direction == "U" or self.direction == "D":
            self.direction = dir_list[-1]
            current_index = directions.index(self.direction)
            new_index = (current_index + 1) % len(directions)
            self.direction = directions[new_index]
            dir_list.append(self.direction)

        else:
            current_index = directions.index(self.direction)
            new_index = (current_index + 1) % len(directions)
            self.direction = directions[new_index]
            dir_list.append(self.direction)

    # Turn Up
    def turn_up(self):
        direction = "U"
        self.direction = direction

    # Turn Down
    def turn_down(self):
        direction = "D"
        self.direction = direction


if __name__ == "__main__":
    # Create the spacecraft object with initial position and direction
    craft = Chandrayaan_3(0, 0, 0, "N")

    # Example commands
    commands = ["f", "r", "u", "b", "l"]

    # Execute commands
    for cmd in commands:
        if cmd == "f":
            craft.move_forward()
        elif cmd == "b":
            craft.move_backward()
        elif cmd == "r":
            craft.turn_right()
        elif cmd == "l":
            craft.turn_left()
        elif cmd == "u":
            craft.turn_up()
        elif cmd == "d":
            craft.turn_down()

    # Display final position and direction
    print("Final Position:", craft.position)
    print("Final Direction:", craft.direction)
