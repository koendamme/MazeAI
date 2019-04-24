import random
import time


class Player:
    def __init__(self, maze, x_position, y_position):
        self.maze = maze
        self.x_position = x_position
        self.y_position = y_position

    def move_right(self):
        vertical_array = self.maze.matrix[self.y_position]
        if vertical_array[self.x_position + 1] != 'X':
            vertical_array[self.x_position].remove(self)
            vertical_array[self.x_position + 1].append(self)
            self.x_position += 1
            self.maze.print()

    def move_left(self):
        vertical_array = self.maze.matrix[self.y_position]

        if vertical_array[self.x_position - 1] != 'X':
            vertical_array[self.x_position].remove(self)
            vertical_array[self.x_position - 1].append(self)
            self.x_position -= 1
            self.maze.print()

    def move_up(self):
        if self.maze.matrix[self.y_position - 1][self.x_position] != 'X':
            self.maze.matrix[self.y_position][self.x_position].remove(self)
            self.maze.matrix[self.y_position - 1][self.x_position].append(self)
            self.y_position -= 1
            self.maze.print()

    def move_down(self):
        if self.maze.matrix[self.y_position + 1][self.x_position] != 'X':
            self.maze.matrix[self.y_position][self.x_position].remove(self)
            self.maze.matrix[self.y_position + 1][self.x_position].append(self)
            self.y_position += 1
            self.maze.print()

    def move_random(self):
        random_direction = random.randint(1, 4)

        if random_direction == 1:
            self.move_up()
        elif random_direction == 2:
            self.move_left()
        elif random_direction == 3:
            self.move_right()
        else:
            self.move_down()
        time.sleep(.3)
