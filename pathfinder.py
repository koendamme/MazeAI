from maze import Maze

maze = Maze("maze.txt")

maze.print()
print(maze.get_player_position())

i = input()

if i == 'U':
    maze.move_up()
    maze.print()
elif i == 'L':
    maze.move_left()
    maze.print()
elif i == 'R':
    maze.move_right()
    maze.print()
elif i == 'D':
    maze.move_down()
    maze.print()
else:
    print("Invalid argument")
