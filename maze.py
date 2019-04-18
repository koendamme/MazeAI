from termcolor import colored


class Maze:
    def __init__(self, file_name):
        self.matrix = []
        self.convert_to_map(file_name)

    def convert_to_map(self, file_name):
        file = open(file_name, "r")
        for row in file.readlines():
            chars = []
            for char in row:
                if char == 'X' or char == '_' or char == "F" or char == 'P':
                    chars.append(char)
            self.matrix.append(chars)

    def print(self):
        for row in self.matrix:
            for item in row:
                if item == 'X' or item == '_' or item == 'F' or item == 'P':
                    print(item, end=" ")
                else:
                    print(colored(item, 'red'), end=" ")
            print()

    def get_player_position(self):
        x, y = 0, 0

        for row in self.matrix:
            for item in row:
                if item == 'P':
                    return x, y
                else:
                    x += 1
            x = 0
            y += 1

    def move_right(self):
        player_x, player_y = self.get_player_position()

        vertical_array = self.matrix[player_y]

        if vertical_array[player_x + 1] != 'X':
            vertical_array[player_x] = '_'
            vertical_array[player_x + 1] = 'P'

    def move_left(self):
        player_x, player_y = self.get_player_position()

        vertical_array = self.matrix[player_y]

        if vertical_array[player_x - 1] != 'X':
            vertical_array[player_x] = '_'
            vertical_array[player_x - 1] = 'P'

    def move_up(self):
        player_x, player_y = self.get_player_position()

        if self.matrix[player_y - 1][player_x] != 'X':
            self.matrix[player_y][player_x] = '_'
            self.matrix[player_y - 1][player_x] = 'P'

    def move_down(self):
        player_x, player_y = self.get_player_position()

        if self.matrix[player_y + 1][player_x] != 'X':
            self.matrix[player_y][player_x] = '_'
            self.matrix[player_y + 1][player_x] = 'P'
