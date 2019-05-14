from player import Player
import random
import time


class Maze:
    def __init__(self, player_count):
        self.start_x = 0
        self.start_y = 0
        self.matrix = []
        self.initiate_empty_map()
        self.players = []
        self.player_count = player_count
        self.generation = 0
        self.finished = False
        self.finished_player = None
        self.finish_pos = (0, 0)

    def initiate_empty_map(self):
        self.matrix = []
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
                    self.finish_pos = (x, y)
                    array = [char]
                    chars.append(array)
                    x += 1
                elif char == 'S':
                    self.start_x = x
                    self.start_y = y
                    chars.append([])
                elif char == '_':
                    chars.append([])
                    x += 1
            self.matrix.append(chars)
            y += 1

    def populate(self, players):
        self.players = players
        for player in players:
            self.matrix[self.start_y][self.start_x].append(player)

    def find_path(self):
        # Generate initial population
        players = []
        for i in range(0, self.player_count):
            chromosome = [random.choice([1, 2, 3, 4]) for _ in range(50)]
            player = Player(self, chromosome)
            player.set_position(self.start_x, self.start_y)
            players.append(player)

        self.populate(players)

        while not self.finished:
            for i in self.players:
                for g in i.chromosome:
                    if g == 1:
                        i.move_right()
                    elif g == 2:
                        i.move_left()
                    elif g == 3:
                        i.move_up()
                    elif g == 4:
                        i.move_down()

                '''In case of using the finish position'''
                # i.fitness = self.calc_fitness(i)
                '''In case of NOT using the finish position'''
                i.fitness = self.calc_fitness_without_finish_pos(i)

            self.print()

            print("Generation: " + self.generation.__str__())
            # time.sleep(.2)
            self.create_new_generation()

        print("Finished with following path..")
        time.sleep(4)
        self.finished_player.finished = False
        self.initiate_empty_map()
        self.populate([self.finished_player])
        for g in self.finished_player.chromosome:
            if self.finished_player.finished:
                break
            else:
                if g == 1:
                    self.finished_player.move_right()
                elif g == 2:
                    self.finished_player.move_left()
                elif g == 3:
                    self.finished_player.move_up()
                elif g == 4:
                    self.finished_player.move_down()
            self.print()
            time.sleep(.2)

    def create_new_generation(self):
        self.initiate_empty_map()
        '''In case of using the finish position'''
        #population = sorted(self.players, key=lambda x: x.fitness)

        '''In case of NOT using the finish position'''
        population = sorted(self.players, key=lambda x: x.fitness, reverse=True)

        for player in population:
            player.set_position(self.start_x, self.start_y)

        new_generation = []

        for _ in range(self.player_count):
            parent1 = random.choice(population[:self.player_count])
            parent2 = random.choice(population[:self.player_count])
            child = parent1.mate(parent2)
            child.set_position(self.start_x, self.start_y)
            new_generation.append(child)

        self.generation += 1
        self.populate(new_generation)

    def calc_fitness(self, player):
        return (self.finish_pos[0] - player.x_position) + (self.finish_pos[1] - player.y_position) + player.penalties

    def calc_fitness_without_finish_pos(self, player):
        return (player.x_position - self.start_x) + (player.y_position - self.start_y) - player.penalties

    def print(self):
        '''In case of using the finish position'''
        # best_player = sorted(self.players, key=lambda x: x.fitness)[0]

        '''In case of NOT using the finish position'''
        best_player = sorted(self.players, key=lambda x: x.fitness, reverse=True)[0]

        for row in self.matrix:
            for item in row:
                if item == 'X' or item == 'F':
                    print(item, end=" ")
                elif type(item) == list and 'F' in item:
                    print('F', end=" ")
                elif type(item) == list and best_player not in item: # and len(item) == 0:
                    print('_', end=" ")

                # elif len(item) > 0 and item[0] == 'F':
                #     print('F', end=" ")
                elif best_player in item:
                    print('P', end=" ")
            print()
