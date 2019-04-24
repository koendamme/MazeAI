from maze import Maze


maze = Maze(2)

maze.print()


while True:

    # i = input()
    #
    # if i == 'R':
    #     maze.players[0].move_right()
    #     maze.print()
    # elif i == 'L':
    #     maze.players[0].move_left()
    #     maze.print()
    #
    # elif i == 'U':
    #     maze.players[0].move_up()
    #     maze.print()
    # elif i == 'D':
    #     maze.players[0].move_down()
    #     maze.print()
    # else:
    #     print("That should not be here!")

    for i in maze.players:
        i.move_random()

