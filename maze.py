from player import Player


class Maze:
    def __init__(self, player_count):
        self.matrix = []
        self.players = []
        self.player_count = player_count
        self.convert_to_map()

    def convert_to_map(self):
        file = open("maze.txt", "r")
        x, y = 0, 0
        for row in file.readlines():
            chars = []
            x = 0
            for char in row:
                if char == 'X':
                    chars.append(char)
                    x += 1
                elif char == 'F':
                    array = [char]
                    chars.append(array)
                elif char == 'S':
                    players = []
                    for i in range(0, self.player_count):
                        player = Player(self, x, y)
                        players.append(player)
                        self.players.append(player)
                    chars.append(players)
                elif char == '_':
                    chars.append([])
                    x += 1
            self.matrix.append(chars)
            y += 1

    def print(self):
        for row in self.matrix:
            for item in row:
                if item == 'X' or item == 'F':
                    print(item, end=" ")
                elif item == [] and len(item) == 0:
                    print('_', end=" ")
                elif len(item) > 0 and item[0] == 'F':
                    print('F', end=" ")
                elif len(item) > 0:
                    print('P', end=" ")
                else:
                    raise ValueError(item)
            print()
