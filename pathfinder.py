from maze import Maze
from player import Player

maze = Maze(10)

maze.print()


# found = False
#
# while True:
#     genes = []
#     fitness = []
#     for i in maze.players:
#         for g in i.chromosome:
#             if g == 1:
#                 i.move_right()
#             elif g == 2:
#                 i.move_left()
#             elif g == 3:
#                 i.move_up()
#             elif g == 4:
#                 i.move_down()
#             else:
#                 print("That should not be here")
#
#         genes.append(i.chromosome)
#         fitness.append(i.fitness)
#
#     for idx in range(0, len(genes)):
#         print(genes[idx])
#         print(fitness[idx])
#
#     print("gen: " + maze.generation.__str__())
#     maze.create_new_generation()
#     print(maze.matrix)

maze.find_path()


