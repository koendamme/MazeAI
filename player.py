import random


class Player:
    def __init__(self, maze, chromosome):
        self.maze = maze
        self.x_position = 0
        self.y_position = 0
        self.fitness = 0
        self.chromosome = chromosome
        self.chromosome_length = 50

    def set_position(self, x, y):
        self.x_position = x
        self.y_position = y

    def move_right(self):
        vertical_array = self.maze.matrix[self.y_position]
        if vertical_array[self.x_position + 1] != 'X':
            vertical_array[self.x_position].remove(self)
            vertical_array[self.x_position + 1].append(self)
            self.x_position += 1
            self.fitness += 1
            # self.maze.print()
        else:
            self.fitness -= 1

    def move_left(self):
        vertical_array = self.maze.matrix[self.y_position]
        if vertical_array[self.x_position - 1] != 'X':
            vertical_array[self.x_position].remove(self)
            vertical_array[self.x_position - 1].append(self)
            self.x_position -= 1
            self.fitness += 1
            # self.maze.print()
        else:
            self.fitness -= 1

    def move_up(self):
        if self.maze.matrix[self.y_position - 1][self.x_position] != 'X':
            self.maze.matrix[self.y_position][self.x_position].remove(self)
            self.maze.matrix[self.y_position - 1][self.x_position].append(self)
            self.y_position -= 1
            self.fitness += 1
            # self.maze.print()
        else:
            self.fitness -= 1

    def move_down(self):
        if self.maze.matrix[self.y_position + 1][self.x_position] != 'X':
            self.maze.matrix[self.y_position][self.x_position].remove(self)
            self.maze.matrix[self.y_position + 1][self.x_position].append(self)
            self.y_position += 1
            self.fitness += 1
            # self.maze.print()
        else:
            self.fitness -= 1

    def mate(self, parent2):

        child_chromosome = []

        for par1, par2 in zip(self.chromosome, parent2.chromosome):
            prob = random.random()

            if prob < .45:
                child_chromosome.append(par1)
            elif prob < .90:
                child_chromosome.append(par2)
            else:
                child_chromosome.append(random.choice([1, 2, 3, 4]))

        return Player(self.maze, child_chromosome)
